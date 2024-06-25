# This code extracts turning point features from the '工步层' or the workstep layer file.
# In our publication: 5-50% SOC, 5s Pulse time or pulse width, U1-U21.
# This version contains illustration for case adjustment and relative implementation revision.
# 20240618 at TBSI.

import os
import pandas as pd

# Replace according to battery type !!!
cap_mat = '10Ah LMO'
# Replace according to your file path !!!
# Create the folder manually in advance !!!
source_folder = 'D:/BaiduSyncdisk/实验数据集合/力景数据代码上传/' + 'ProcessingData/' + 'step_1_extract workstep sheet/' + cap_mat + '/'
# Replace according to your file path !!!
# Create the folder manually in advance !!!
save_folder = 'D:/BaiduSyncdisk/实验数据集合/力景数据代码上传/' + 'ProcessingData/' + 'step_2_feature extraction_adjustable/' + cap_mat + '/'

# Adjustable turning point features extraction
# Must be consistent with the settings in step_3_feature collection.py !!!
soc_to_extract = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50] # In our publication: 5-50% SOC
    # Recommended within {5, 10, ..., 50}, as batteries with low SOH may not tested with 55% or higher SOC.
    # Adjustable within {5, 10, ..., 90}.
    # Can be non-adjacent.
    # Arranging in ascending order is recommended, but not mandatory.
    # Not including duplicate content is required.
pt_to_extract = [5] # In our publication: 5s
    # Adjustable within {0.03, 0.05, 0.07, 0.1, 0.3, 0.5, 0.7, 1, 3, 5}.
    # Can be non-adjacent.
    # Arranging in ascending order is recommended, but not mandatory.
    # Not including duplicate content is required.
U_to_extract = range(1,21 +1) # In our publication: U1-U21
    # Adjustable within {1, 2, ..., 41}.
    # Can be non-adjacent.
    # Arranging in ascending order is recommended, but not mandatory.
    # Not including duplicate content is required.
    # U1: steady state open cicrcuit voltage (OCV) after 10 mins rest
    # U2-U9: voltage at the beginning and end of 0.5C positive pulse, rest, 0.5C negative pulse and rest.
    # U10-U17: 1C. # U18-U25: 1.5C. # U26-U33: 2C. # U34-U41: 2.5C.

# ONLY files in .xlsx format will be read in.
# Temporary files in .xlsx format will NOT be read in.
xlsx_files = [f for f in os.listdir(source_folder) if f.endswith('.xlsx') and not f.startswith('~$')]
xlsx_file_num = len(xlsx_files)

i = 0

item = ['File_Name','Mat','No.','ID','Qn','Q','SOH','Pt','SOC','SOCR'] + ['U' + str(i) for i in U_to_extract]

for f in xlsx_files:
    # Progress bar
    # This process may be time consuming.
    # Please be patient.
    i = i + 1
    print(str(i) + '/' + str(xlsx_file_num) + ' ' + f + ' processing')

    # Read in
    df = pd.read_excel(source_folder + f).values

    ft = [None] * len(item)
    # Correspond to the item list
    ft[0] = f                                   # File_Name
    ft[1] = f.split('_')[0]                     # Mat
    ft[2] = int(f.split('_')[4])                # No.
    ft[3] = f.split('_')[10].split('.xlsx')[0]  # ID
    ft[4] = int(f.split('_')[2])                # Qn
    Q = - df[3][16]                             
    ft[5] = Q                                   # Q
    ft[6] = Q/ft[4]                             # SOH

    data = []

    # Feature extraction
    for soc_num in soc_to_extract:
        soc_ith = int(soc_num/5 -1)

        ft[8] = soc_num # SOC, state-of-charge.
            # The assumed value in ideal experiment.
            # Actually it is a category here, not a very accurate value.

        for pt_num in pt_to_extract:
            pt_ith = [0.03, 0.05, 0.07, 0.1, 0.3, 0.5, 0.7, 1, 3, 5].index(pt_num)

            ft[7] = pt_num  # Pt, i.e. pulse time or pulse width.

            soc_row_num = 5-1 + (10*5*4+2)*soc_ith + 2 + 5*4*pt_ith
            # 5-1: 5 steps SOH or Capacity measurement by CCCV charge - CC discharge, -1 due to start from 0 in python
                # rest, CCCV charge, rest, CC discharge, rest
            # 2: 2 steps to condition to assigned SOC
                # CC charge, rest
            # 10: 10 kinds of pulse time or pulse width
            # 5: 5 kinds of pulse current intensity
            # 4: 4 steps per pulse current intensity per pulse width
                # CC charge or positive pulse, rest, CC discharge or negative pulse, rest
            ft[9] = sum(df[5:(soc_row_num+1),18]) / ft[4]    # SOCR, state-of-charge in real at U1.
                # A more accurate value based on accumulated net charged capacity from statistics in the '工步层' or the workstep layer.
            
            ft[10:len(item)] = [None] * (len(item)-10)

            # Ensure that it will not read more than the actual number of rows or steps
            U_row_num_max = 5-1 + (10*5*4+2)*soc_ith + 2 + 5*4*pt_ith + max(U_to_extract) // 2
                # Due to security concern and voltage protection, some batteries failed to complete all planed pulse tests with various SOC, pulse time and pulse current amplitude.
                # If the experiemnt stop at step i corresponding to U(j) and U(j+1) with certain SOC, pulse time and pulse current amplitude:
                # In this version for adjustability:
                    # If all U(k) in U_to_extract satisfies k <= j+1, all required features in U_to_extract at this SOC, pulse time and pulse current amplitude will be recorded.
                    # If U_to_extract contains U(k) where j+1 < k, all required features in U_to_extract at this SOC, pulse time and pulse current amplitude will NOT be recorded.

            # Ensure that it will not read more than the actual number of rows or steps
            if U_row_num_max < df.shape[0]:
                for U_num in U_to_extract:
                    U_ith = U_to_extract.index(U_num) + 1

                    U_row_num = 5-1 + (10*5*4+2)*soc_ith + 2 + 5*4*pt_ith + U_num // 2
                    # 5-1: 5 steps SOH or Capacity measurement by CCCV charge - CC discharge, -1 due to start from 0 in python
                        # rest, CCCV charge, rest, CC discharge, rest
                    # 2: 2 steps to condition to assigned SOC
                        # CC charge, rest
                    # 10: 10 kinds of pulse time or pulse width
                    # 5: 5 kinds of pulse current intensity
                    # 4: 4 steps per pulse current intensity per pulse width
                        # CC charge or positive pulse, rest, CC discharge or negative pulse, rest
                    ft_ith = 9 + U_ith # ft[0]-ft[9]
                    
                    if U_num == 1:
                        ft[ft_ith] = df[U_row_num][12]  # U1.
                    elif U_num % 2 == 0:
                        ft[ft_ith] = df[U_row_num][10]  # Beginning point: U2, U4, ..., U40.
                    elif U_num % 2 == 1:
                        ft[ft_ith] = df[U_row_num][12]  # End point: U3, U5, ..., U41.
                    
                data.append(list(ft))

    # Save
    save_data = pd.DataFrame(data)
    save_data.to_excel(save_folder + f, index=False, header=item)

# Progress bar
print('Finished.')
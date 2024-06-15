# This code extracts turning point features from the '工步层' or the workstep layer file.
# 5s Pulse time or pulse width
# U1-U21
# SOC 5-50%

import os
import pandas as pd

# Replace according to battery type !!!
cap_mat = '10Ah LMO'
# Replace according to your file path !!!
# Create the folder manually in advance !!!
source_folder = 'D:/BaiduSyncdisk/实验数据集合/力景数据代码上传/' + 'Processing/' + 'step_1_extract workstep sheet/' + cap_mat + '/'
# Replace according to your file path !!!
# Create the folder manually in advance !!!
save_folder = 'D:/BaiduSyncdisk/实验数据集合/力景数据代码上传/' + 'Processing/' + 'step_2_feature extraction/' + cap_mat + '/'

# ONLY files in .xlsx format will be read in.
# Temporary files in .xlsx format will NOT be read in.
xlsx_files = [f for f in os.listdir(source_folder) if f.endswith('.xlsx') and not f.startswith('~$')]
xlsx_file_num = len(xlsx_files)

i = 0

item = ['File_Name','Mat','No.','ID','Qn','Q','SOH','Pt','SOC','SOE'] + ['U' + str(i) for i in range(1, 22)] # U1-U21

for f in xlsx_files:
    # Progress bar
    # This process may be very time consuming.
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
    for soc_ith in range(0,10):
        soc_num = int((soc_ith+1)*5)
        
        pt_num = 5 # 5s
        pt_ith = 9 # 9th in [0.03, 0.05, 0.07, 0.1, 0.3, 0.5, 0.7, 1, 3, 5]. Index start from 0 in python.

        ft[7] = pt_num                      # Pt, i.e. pulse time or pulse width.
        ft[8] = soc_num                     # SOC, a category here, not a very accurate value.
        ft[9] = soc_num * ft[6]             # SOE, here it means another SOC definition normalized with SOH.

        for current_ith in range(0,3):
            # U1-U21 correspond to the first 3 pulse current intensity, i.e. 0.5C, 1C, 1.5C.

            base_ft_num = 9 + current_ith * 8
            # A positive and a negative pulse contain 8 features.

            base_row_num = 5-1 + (10*5*4+2)*soc_ith + 2 + 5*4*pt_ith + 4*current_ith
            # 4: 4 steps per pulse current intensity per pulse width
                # CC charge or positive pulse, rest, CC discharge or negative pulse, rest
            # 5: 5 kinds of pulse current intensity
            # 10: 10 kinds of pulse time or pulse width
            # 2: 2 steps to condition to assigned SOC
                # CC charge, rest
            # 5-1: SOH or Capacity measurement by CCCV charge - CC discharge, -1 due to start from 0 in python
                # rest, CCCV charge, rest, CC discharge, rest

            ft[base_ft_num + 1] = df[base_row_num][12]          # U1, U9, U17.
            ft[base_ft_num + 2] = df[base_row_num + 1][10]      # U2, U10, U18.
            ft[base_ft_num + 3] = df[base_row_num + 1][12]      # U3, U11, U19. 
            ft[base_ft_num + 4] = df[base_row_num + 2][10]      # U4, U12, U20. 
            ft[base_ft_num + 5] = df[base_row_num + 2][12]      # U5, U13, U21. 
            if current_ith < 2:
                ft[base_ft_num + 6] = df[base_row_num + 3][10]  # U6, U14.
                ft[base_ft_num + 7] = df[base_row_num + 3][12]  # U7, U15. 
                ft[base_ft_num + 8] = df[base_row_num + 4][10]  # U8, U16.S 

        data.append(list(ft))

    # Save
    save_data = pd.DataFrame(data)
    save_data.to_excel(save_folder + f, index=False, header=item)

# Progress bar
print('Finished.')
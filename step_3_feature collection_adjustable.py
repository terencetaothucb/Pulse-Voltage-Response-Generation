# This code aggregates turning point features scattered in different files together.
# 20240618 at TBSI.

import os
import pandas as pd

# Replace according to battery type !!!
cap_mat = '10Ah LMO'
mat_inf = 'LMO_10Ah_W_'
# Replace according to your file path !!!
# Create the folder manually in advance !!!
source_folder = 'D:/BaiduSyncdisk/实验数据集合/力景数据代码上传/' + 'ProcessingData/' + 'step_2_feature extraction_adjustable/' + cap_mat + '/'
# Replace according to your file path !!!
# Create the folder manually in advance !!!                    # To be created               # 3 Subfolders to be created
save_folder = 'D:/BaiduSyncdisk/实验数据集合/力景数据代码上传/' + 'ProcessedData_adjustable/' + cap_mat + '/'

# Must be consistent with the settings in step_2 !!!
soc_to_extract = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
pt_to_extract = [5]
U_to_extract = range(1,21 +1)
    # U1: steady state open cicrcuit voltage (OCV) after 10 mins rest
    # U2-U9: voltage at the beginning and end of 0.5C positive pulse, rest, 0.5C negative pulse and rest.
    # U10-U17: 1C. # U18-U21: 1.5C positive pulse and rest.

# ONLY files in .xlsx format will be read in.
# Temporary files in .xlsx format will NOT be read in.
xlsx_files = [f for f in os.listdir(source_folder) if f.endswith('.xlsx') and not f.startswith('~$')]
xlsx_file_num = len(xlsx_files)

item = ['File_Name','Mat','No.','ID','Qn','Q','SOH','Pt','SOC','SOCR'] + ['U' + str(i) for i in U_to_extract]

sheet_num = len(soc_to_extract) + 1 # With features under all SOC collected together

# Features with same pulse time or pulse width are collected in a file
for pt_num in pt_to_extract:
    pt_ith = pt_to_extract.index(pt_num)
    # Progress bar
    # This process may be time consuming.
    # Please be patient.
    print(str(pt_ith+1) + '/' + str(len(pt_to_extract)) + ' pulse time ' + str(pt_num) + 's processing')

    data = [[] for _ in range(sheet_num)]

    i = 0

    # Collection
    for f in xlsx_files:
        # Progress bar
        # This process may be time consuming.
        # Please be patient.
        i = i + 1
        print(str(pt_ith+1) + '/' + str(len(pt_to_extract)) + ' pulse time ' + str(pt_num) + 's ' + str(i) + '/' + str(xlsx_file_num) + ' ' + f + ' processing')

        df = pd.read_excel(source_folder + f).values

        # Row by row
        for row_ith in range(0,df.shape[0]):
            # Pulse time or pulse width match
            if float(df[row_ith][7]) == float(pt_num):
                data[0].append(list(df[row_ith])) # All SOC collected together
                data[soc_to_extract.index(df[row_ith][8]) + 1].append(list(df[row_ith])) # Specific SOC category

    # Save
    save_file_name = mat_inf + str(int(pt_num*1000)) + '.xlsx' # Using ms as time unit here.

    with pd.ExcelWriter(save_folder + save_file_name) as writer:

        # All SOC collected together
        save_data = pd.DataFrame(data[0])
        save_data.to_excel(writer, sheet_name='SOC ALL', index=False, header=item)

        # Specific SOC category
        for soc_num in soc_to_extract:
            soc_ith = soc_to_extract.index(soc_num)

            if not data[soc_ith+1]:
                data[soc_ith+1].append([None]*len(item))
            save_data = pd.DataFrame(data[soc_ith+1])
            save_data.to_excel(writer, sheet_name='SOC'+str(soc_num), index=False, header=item)

# Progress bar
print('Finished.')
# This code aggregates turning point features scattered in different files together.
# 5s Pulse time or pulse width
# U1-U21
# SOC 5-50%

import os
import pandas as pd

# Replace according to battery type !!!
cap_mat = '10Ah LMO'
mat_inf = 'LMO_10Ah_W_'
# Replace according to your file path !!!
# Create the folder manually in advance !!!
source_folder = 'D:/BaiduSyncdisk/实验数据集合/力景数据代码上传/' + 'Processing/' + 'step_2_feature extraction/' + cap_mat + '/'
# Replace according to your file path !!!
# Create the folder manually in advance !!!
save_folder = 'D:/BaiduSyncdisk/实验数据集合/力景数据代码上传/' + 'ProcessedData/' + cap_mat + '/'

# ONLY files in .xlsx format will be read in.
# Temporary files in .xlsx format will NOT be read in.
xlsx_files = [f for f in os.listdir(source_folder) if f.endswith('.xlsx') and not f.startswith('~$')]

item = ['File_Name','Mat','No.','ID','Qn','Q','SOH','Pt','SOC','SOE'] + ['U' + str(i) for i in range(1, 22)]

soc_max = 50 # SOC: 5-50
pt_num = 5 # 5s
pt_ith = 9

sheet_num = int(50/5) + 1
data = [[] for _ in range(sheet_num)]

for f in xlsx_files:
    df = pd.read_excel(source_folder + f).values

    for row_ith in range(0,df.shape[0]):
        data[0].append(list(df[row_ith]))
        data[int(df[row_ith][8]/5)].append(list(df[row_ith]))

# Save
save_file_name = mat_inf + str(int(pt_num*1000)) + '.xlsx'
with pd.ExcelWriter(save_folder + save_file_name) as writer:
    # ALL SOC
    save_data = pd.DataFrame(data[0])
    save_data.to_excel(writer, sheet_name='SOC ALL', index=False, header=item)
    # Each SOC
    for soc_ith in range(1,sheet_num):
        save_data = pd.DataFrame(data[soc_ith])
        save_data.to_excel(writer, sheet_name='SOC'+str(int(5*soc_ith)), index=False, header=item)

# Progress bar
print('Finished.')
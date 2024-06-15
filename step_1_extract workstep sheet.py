# This code extracts the '工步层' or the workstep layer from raw data file.

# A single raw data file can be very large, with dozens of MB, depending on the measurement requirement.
# Processing tools such as Pandas package and Microsoft Office have limited speed in loading files.
# Several minutes needed for loading a whole complete raw data file once.
# All turning point features used in this article can be found in the workstep layer.
# Therefore, there is no need to read the '记录层' or the record layers with ultra large file size.
# Here, this code extract the '工步层' or the workstep layer from raw data file, shorting the time consumption for subsequent processing steps.

# For future research focusing on time-series ML methods, the '记录层' or the record layers are still needed.

import os
import pandas as pd

# Replace according to battery type !!!
cap_mat = '15Ah NMC'
# Replace according to your file path !!!
# Create the folder manually in advance !!!
source_folder = 'D:/BaiduSyncdisk/实验数据集合/力景数据代码上传/' + 'RawData/' + cap_mat + '/'
# Replace according to your file path !!!
# Create the folder manually in advance !!!
save_folder = 'D:/BaiduSyncdisk/实验数据集合/力景数据代码上传/' + 'Processing/' + 'step_1_extract workstep sheet/' + cap_mat + '/'

# Specify the worksheet to extract.
# '工步层' means the workstep layer.
# This code need to be edited when we want to extract the '记录层' or the record layers.
sheet_name = '工步层'
# In case you want to extract other layers and you do not know how to type in Chinese letters, you can use sheet index rather than sheet name.
# For example, sheet_name = 2 to extract the workstep layer or sheet_name = 6 to extract the first record layer.

# ONLY files in .xlsx format will be read in.
# Temporary files in .xlsx format will NOT be read in.
xlsx_files = [f for f in os.listdir(source_folder) if f.endswith('.xlsx') and not f.startswith('~$')]
xlsx_file_num = len(xlsx_files)

i = 0

for f in xlsx_files:
    # Progress bar
    # This process may be very time consuming.
    # Please be patient.
    i = i + 1
    print(str(i) + '/' + str(xlsx_file_num) + ' ' + f + ' processing')

    # Sometimes the raw data is split into 2 parts due to the ultra long measurement time and ultra large file size.
    # In this case, the workstep layer will be placed in the first part.
    # Only several record layers will be placed in the second part.
    # Here, only the first part will be read in, ensuring 1 extracted workstep layer file corresponds to 1 battery cell.
    if f.split('_')[8].split('-')[0] == '1':
        # Read in & extract
        data = pd.read_excel(source_folder + f, sheet_name=sheet_name)
        # Save
        data.to_excel(save_folder + f, index = False)

# Progress bar
print('Finished.')
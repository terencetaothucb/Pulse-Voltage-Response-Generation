# Pulse Voltage Response Generation: PulseBat Dataset
Retired batteries have been presenting a severe sustainability challenge worldwide. One promising sustainable solution is reuse and recycling, but state of health (SOH) information for residual value evaluation retrieved from charge-discharge approaches are still time-consuming and energy-intensive. Developing a data-driven, rapid, and sustainable SOH estimation method for reuse and recycling decision-making is crucial. Here we open-source the collected PulseBat dataset for pulse voltage response generation of retired batteries across random retirement conditions, i.e., state of charge (SOC) conditions, facilitating downstream SOH estimation tasks. The PulseBat dataset was collected from diversified cathode material types, historical usages, physical formats and capacity designs to deliberately introduce data heterogeneities, which is a common challenge in retired battery reuse and recycling scenarios. Xiamen Lijing New Energy Technology Co., Ltd., (Xiamen Lijing) collected the dataset. The collaboration team at Tsinghua Berkeley Shenzhen Institute (TBSI) processed this dataset. AI and battery community will find the PulseBat dataset useful for SOH estimation of retired batteries under transfer learning, continual learning, and generative learning settings.

# 1. Publication
[Generative-learning-assisted Rapid State-of-Health Estimation for Sustainable Battery Recycling with Random Retirement Conditions](To be published)
# 2. Description
## 2.1. Overview
Retired batteries exhibit considerable heterogeneities in cathode material types, historical usages, physical formats and capacity designs. We physically tested 270 retired lithium-ion batteries, covering 3 cathode types, 4 historical usages, 3 physical formats, and 4 capacity designs.
#### Battery Types
|Cathode Material|Nominal Capacity (Ah)|Physical Format|Historical Usage|Quantity|
|:--|:--|:--|:--|:--|
|NMC|2.1|Cylinder|Lab Accelerated Aging|67 (from 12 physical batteries)|
|LMO|10|Pouch|HEV1|95|
|NMC|21|Pouch|BEV1|52|
|LFP|35|Square Aluminum Shell|HEV2|56|

NMC stands for lithium nickel manganese cobalt oxide. LMO stands for lithium manganese oxide. LFP stands for lithium iron phosphate.
#### SOH Distribution
<p align="center">
  <img src="SOH Distribution.png" alt="SOH Distribution">
</p>  

## 2.2. Experiment Details
Tests were performed with BAT-NEEFLCT-05300-V010, NEBULA, Co, Ltd, and the air conditioner temperature was set at 25℃.  
Only EV-retired batteries (LMO 10 Ah, NMC 15 Ah, NMC 21 Ah and LFP 35Ah) were subject to this test procedure. Refer to Supplementary Note 3 in Supplementary Information for experiment details of Lab Accelerated Aging batteries (NMC 2.1 Ah).  
The experiment is divided into the following three steps: capacity calibration, SOC conditioning, and pulse injection.  
### Step 1 : Capacity Calibration
We use the widely-adopted constant current (CC) discharge method as the gold standard for determining the capacity of retired batteries. Even considering the different initial state of charge (SOC) distributions of retired batteries, we use a unified method of first constant current constant voltage (CCCV) charging and then CC discharging to determine the capacity of retired batteries.  
First, the retired batteries are charged to the upper cut-off voltage using a 1C constant current, then charged using constant voltage until the current drops to 0.05 C.  The batteries are then discharged to the lower cut-off voltage using a 1C constant current. We use the actual discharge capacity as the calibrated (true) battery capacity and then let the battery rest for 20 minutes before SOC conditioning and pulse injection. Here the term C refers to the C-rate, determined by the current value required by a 1h full charge or discharge of a battery. The sampling frequency during step 1 is 1 Hz.  
Cathode Material|Nominal Capacity (Ah)|Cut-Off Voltage for Dis/Charging (V)|
|:--|:--|:--|
|LMO|10|2.0/4.2|
|NMC|15|2.7/4.2|
|NMC|21|2.7/4.2|
|LFP|35|2.5/3.65|
### Step 2 : SOC Conditioning
SOC conditioning refers to adjusting the battery SOC to a desired level, necessitated by the fact that retired batteris are of random SOC distributions upon the collection. When the capacity calibration is finished, the battery is at its zero SOC. When a 5% SOC is desired, we use a 1C constant current for 3 minutes to adjust the calibrated battery to a 5% SOC level. The battery is then left to stand for 10 minutes to rest, expecting the battery to return to a steady state in preparation for subsequent pulse injection. Notice that SOC here is defined as the ratio of charged or dischargeable capacity to the nominal capacity. The sampling frequency during step 2 is 1 Hz.  
### Step 3 : Pulse Injection
We perform multiple consecutive pulse injections with different pulse widths and amplitudes. The pulse width and pulse resting time are shown in the following Table, that is, for each pulse width and resting time (each row of the table), we consecutively perform pulse injection with pulse amplitude being 0.5-1-1.5-2-2.5(C) in order, including positive and negative pulse injections. Note that positive and negative pulses alternate to cancel the equivalent energy injection, thus the stored energy inside the battery does not change. Take pulse injection at 5% SOC for an example, at the 30ms pulse width, we inject 0.5C positive current pulse, then let the battery rest for 450ms, and then inject 0.5C negative current pulse, then again let the battery rest for 450ms. Still at 5% SOC, other remaining pulses with different amplitudes follow the rest of the previous pulse injections. Repetitive experiments are performed until the remaining pulse widths are exhausted. Then we charge the retired battery with a constant current of 1C for another 3 minutes to 10% SOC (refer to the SOC conditioning step), followed by the same procedure as explained above.  
|Pulse Width|Pulse Rest Time|Pulse Amplitude (±C)|
|:--|:--|:--|
|30ms|450ms|0.5-1-1.5-2-2.5|
|50ms|750ms|0.5-1-1.5-2-2.5|
|70ms|1.05s|0.5-1-1.5-2-2.5|
|100ms|1.5s|0.5-1-1.5-2-2.5|
|300ms|4.5s|0.5-1-1.5-2-2.5|
|500ms|7.5s|0.5-1-1.5-2-2.5|
|700ms|10.5s|0.5-1-1.5-2-2.5|
|1s|15s|0.5-1-1.5-2-2.5|
|3s|45s|0.5-1-1.5-2-2.5|
|5s|75s|0.5-1-1.5-2-2.5|

Repeat Step 2 and Step 3 until the SOC conditioning region is exhausted. The sampling frequency during step 3 is 100 Hz.  
#### SOC Conditioning Range Determination
The range of SOC conditioning is determined by a calibrated SOH of the retired battery. Specifically, the upper bound of the SOC conditioning region is lower than the calibrated SOH value of the retired battery by 0.05. For instance, when the retired battery has a previous calibrated SOH between 0.5 and 0.55, then the SOC conditioning region will be 5% to 45%, with a grain of 5%. Detailed information is shown in the table below.  
|SOH|SOC Range (%), 5% Grain|
|:--|:--|
|>0.95|[5,90]|
|0.90-0.95|[5,85]|
|0.85-0.90|[5,80]|
|0.80-0.85|[5,75]|
|0.75-0.80|[5,70]|
|0.70-0.75|[5,65]|
|0.65-0.70|[5,60]|
|0.60-0.65|[5,55]|
|0.55-0.60|[5,50]|
|0.50-0.55|[5,45]|
|0.45-0.50|[5,40]|
|0.40-0.45|[5,35]|
|0.35-0.40|[5,30]|
|<0.35|Not Found|

The planned SOC range is recorded with a [fixed format on the file name](#31-file-name) of each battery.  
#### Protection Voltage
We set protection voltage during pulse injection to ensure safety. The specific protection voltage parameters are consistent with those in the following Table.  
Cathode Material|Nominal Capacity (Ah)|Discharge/Charge (V)|
|:--|:--|:--|
|LMO|10|1.95/4.3|
|NMC|15|2.65/4.25|
|NMC|21|2.65/4.3|
|LFP|35|2.45/3.7|

If the oscillation voltage during pulse injection exceeds the protection range, the current charging or discharging workstep will be immediately terminated for physical security check. If the security check is passed, no time will be made up for the already terminated workstep, but the remaining worksteps in test procedure will be continued. In our test, voltage is mainly possible to exceed the protection range during charging, and no cases of below the protection range during discharge have been found.
#### SOC Deviation
The unequal charged and discharged capacity in adjacent positive and negative pulses with the same pulse intensity and planned pulse width caused by voltage protection will lead to an accumulatable deviation in SOC to subsequent pulse test. Fortunately, this SOC deviation is usually very slight due to the extremely short pulse width with no more than 5s. Moreover, the voltage may exceed the protection range generally when the tested SOC is close to the SOH value of the battery. In [our publication](To be published), we only used data from 5-50% SOC. Considering that the SOH of the vast majority of batteries is above 0.6, the SOC deviation used in [our publication](To be published) can be ignored for simplicity. However, if you want to use data at higher SOC level, you may need to pay attention to this SOC deviation issue to avoid introducing unnecessary errors into machine-learning models.
## 3. Raw Data
### 3.1. File Name
#### Raw Data File Name Format
mat_C_cap_B_no._SOC_soc range lower bound-soc range upper bound_Part_part i-of j parts in total_ID_id.xlsx
#### Example
LMO_C_10_B_1_SOC_5-55_Part_1-1_ID_PIP15828A00225770.xlsx  
NMC_C_21_B_14_SOC_5-90_Part_1-2_ID_02LCC02100101A87Y0026421.xlsx  
NMC_C_21_B_14_SOC_5-90_Part_2-2_ID_02LCC02100101A87Y0026421.xlsx  
LFP_C_35_B_56_SOC_5-90_Part_1-2_ID_56号.xlsx  

**Instance:** LMO_C_10_B_1_SOC_5-55_Part_1-1_ID_PIP15828A00225770.xlsx refer to the testing of LMO 10Ah battery with index 1 (also indexed by the unique ID: PIP15828A00225770), where the testing SOC region is from 5% to 55%. The testing have 1 out of 1 file.

#### File Split Explanation
Sometimes the raw data is split into 2 parts due to the ultra long measurement time and ultra large file size.

**Instance:** NMC_C_21_B_14_SOC_5-90_Part_1-2_ID_02LCC02100101A87Y0026421.xlsx refer to the testing of NMC 21Ah battery with index 14 (also indexed by the unique ID: 02LCC02100101A87Y0026421), where the testing SOC region is from 5% to 90%. The testing file is the first file 1 out of 2 files.

If the raw data is split into 2 parts, the workstep layer (i.e., '工步层'), which is used in [our publication](To be published), will always be placed in the first part.  
## 4. Feature Engineering
### 4.1. Features Selection Dimensions
#### 4.1.1. SOC
We performed pulse injections at different SOC levels. Selectable SOC levels include 5%, 10%, 15%, ..., 90%, which are consistent with as described in [Experimental Details](#soc-conditioning-range-determination).
#### 4.1.2. Pulse Width
We performed multiple consecutive pulse injections with different pulse widths. Selectable pulse widths include 30ms, 50ms, 70ms, 100ms, 300ms, 500ms, 700ms, 1s, 3s, 5s, which are consistent with as described in [Experimental Details](#step-3--pulse-injection). Rest time between pulses is 15 times the pulse width, which are 450ms, 750ms, 1.05s, 1.5s, 4.5s, 7.5s, 1.05s, 15s, 45s, 75s.  
#### 4.1.3. Pulse Amplitude
We performed multiple consecutive pulse injections with different pulse amplitudes. Selectable pulse amplitudes include 0.5C, 1C, 1.5C, 2C, 2.5C, which are consistent with as described in [Experimental Details](#step-3--pulse-injection). Features are extracted from turning points, i.e., the points at the beginning and end of pulse injection and rest workstep on the voltage response curve. For simplicity, we use U1-U41 to represent pulse amplitudes. U1 is the steady state open cicrcuit voltage (OCV) after 10 mins rest. U2-U9 refers to voltage at the beginning and end of 0.5C positive pulse, rest, 0.5C negative pulse, rest, respectively. Similarly, U10-U17, U18-U25, U26-U33 and U34-U41 refers to that of 1C, 1.5C, 2C and 2.5C, respectively. Note that the term C stands for charge (discharge) rate when a 1 hour of charge (discharge) is performed. The ambient temperature is controlled at 25 ℃.  
### 4.2. Features Used in our Publication
We extracted U1-U21 features under 5-50% SOC, 5s pulse width for [our publication](To be published). The rest time between each pulse is 75s. U1 is the steady state open cicrcuit voltage (OCV) after 10 mins rest. U2-U9 refers to voltage at the beginning and end of 0.5C positive pulse, rest, 0.5C negative pulse, rest, respectively. Similarly, U10-U17 refers to voltage at the beginning and end of 1C positive pulse, rest, 1C negative pulse, rest, respectively. U18-U21 refers to voltage at the beginning and end of 1C positive pulse, rest, respectively.  
### 4.3. Reproduction
Feature engineering starting from raw data requires three steps. For reproduction, download the [raw data](https://zenodo.org/uploads/11671216) and programs for [Step 1](https://github.com/terencetaothucb/Pulse-Voltage-Response-Generation/blob/main/step_1_extract%20workstep%20sheet.py), [Step 2](https://github.com/terencetaothucb/Pulse-Voltage-Response-Generation/blob/main/step_2_feature%20extraction_adjustable.py), [Step 3](https://github.com/terencetaothucb/Pulse-Voltage-Response-Generation/blob/main/step_3_feature%20collection_adjustable.py) in this repository.  
Manually create folders for each step and subfolders for each battery type to store processing and processed data. Update folder addresses in each program. Adjust the cap_mat variable in the program and run to reproduce the feature engineering results of different battery types. All possible adjustments are listed at the top of each program.  
#### Recommanded Folder Sturcture
- yourplace/
  - RawData/
    - 10Ah LMO/
    - 21Ah NMC/
    - 35Ah LFP/
  - ProcessingData/
    - step_1_extract workstep sheet/
      - 10Ah LMO/
      - 21Ah NMC/
      - 35Ah LFP/
    - step_2_feature extraction_adjustable/
      - 10Ah LMO/
      - 21Ah NMC/
      - 35Ah LFP/
  - ProcessedData/
    - 2.1Ah NMC/
    - 10Ah LMO/
    - 21Ah NMC/
    - 35Ah LFP/

Then you will have [extracted features](https://github.com/terencetaothucb/Pulse-Voltage-Response-Generation/blob/main/ProcessedData_adjustable_2.1Ah%2010Ah%2021Ah%2035Ah.zip) from 10Ah LMO, 21Ah NMC and 35Ah LFP.  

Specificly,  

#### 4.3.1. Step 1 : Extract Workstep Sheet
**Step 1** is to extract the workstep layer (i.e., '工步层') or sheet from the raw data of each battery. Step 1 takes a long time and may take several hours or days to complete. If step 1 is correctly completed, you will get one workstep layer file for each battery. The size of each workstep layer file is several hundred KB and is strongly positively correlated with experimental duration, or the range of SOC conditioning. As the workstep layer will be placed in the first part when the raw data is split into two parts, the workstep layer file of each battery is named to be same with the first part of the raw data. A correctly reproduced example file can be seen [here](https://github.com/terencetaothucb/Pulse-Voltage-Response-Generation/blob/main/Processing%20Data%20Example/NMC_C_21_B_6_SOC_5-90_Part_1-2_ID_02LCC02100101A87Y0052124.xlsx).  
#### Workstep Layer Filename Format (Almost same with Raw Data)
mat_C_cap_B_no.\_SOC_soc range lower bound-soc range upper bound_Part\_**1**-of j parts in total_ID_id.xlsx
#### Example
LMO_C_10_B_1_SOC_5-55_Part_**1**-1_ID_PIP15828A00225770.xlsx  
NMC_C_21_B_14_SOC_5-90_Part_**1**-2_ID_02LCC02100101A87Y0026421.xlsx  
LFP_C_35_B_56_SOC_5-90_Part_**1**-2_ID_56号.xlsx  
#### Notice
Due to unknown reasons, the raw data of battery PIP15827A00221240 (10Ah LMO, No.2) has one more rest (i.e., '静置') step than normal. This issue will not affect reproduction, so you can temporarily skip the following operations in this notice. 
However, to ensure the correctness of further adjustable feature extraction, please manually merge row 2020 (the first rest (i.e., '静置') step) and 2021 (the second rest (i.e., '静置') step) in the extracted workstep layer file LMO_C_10_B_2_SOC_5-55_Part_1-1_ID_PIP15827A00221240.xlsx after completing step 1 and before step 2. In detail, copy the column K element (3.9837) of row 2020 to replace the column K element of row 2021, then delete row 2020. If you feel that doing so is too troublesome, you can replace the local file with [this edited version](https://github.com/terencetaothucb/Pulse-Voltage-Response-Generation/blob/main/Unexpected%20Situations%20Handling/LMO_C_10_B_2_SOC_5-55_Part_1-1_ID_PIP15827A00221240.xlsx). Or you can choose to discard battery PIP15827A00221240 directly by deleteing the raw data file before step 1 or the workstep layer file after step 1, both named LMO_C_10_B_2_SOC_5-55_Part_1-1_ID_PIP15827A00221240.xlsx.  

#### 4.3.2. Step 2 : Feature Extraction
**Step 2** is to extract required features from the workstep layer of each battery. Step 2 can be completed within one hour. If step 2 is correctly completed, you will get one file for each battery. There are 10 samples (5-50% SOC, in ascending order) from each battery. The information record format for each sample for each sample is listed in the following table. The size of each file after step 2 is 7 KB. The name of each file after step 2 is same with the file after step 1. A correctly reproduced example file can be seen [here](https://github.com/terencetaothucb/Pulse-Voltage-Response-Generation/blob/main/Processing%20Data%20Example/LMO_C_10_B_2_SOC_5-55_Part_1-1_ID_PIP15827A00221240.xlsx).  

#### 4.3.3. Step 3 : Feature Collection
**Step 3** is to integrate features from different batteries with same pulse width and same type into one file. Step 3 can be completed almost immediately. If step 3 is correctly completed, you will get 3 files. Each file you receive will contain 11 worksheets. The first worksheet 'SOC ALL' contains features under all SOC condition. Subsequent 10 worksheets 'SOCi' include features under a single SOC condition, separately. In each worksheets, there are as many samples as the quantity of batteries of that type. The size of each file after step 3 is several hundred KB and is strongly positively correlated with the battery quantity of that type. To verify the correctness of reproduction, use our processed features [here](https://zenodo.org/uploads/11671216).  
### 4.4. Adjustability: Features of Different Hyperparameters
We extracted U1-U21 features under 5-50% SOC, 5s pulse width for [our publication](To be published). Moreover, our feature engineering codes have strong scalability. You can adjust the settings at the top of programs of step 2 and step 3 to extract different features. No need to perform step 1 again if reproduction completed once. Remember to keep the settings in the programs of step 2 and step 3 consistent.
#### 4.4.1. SOC
~~~python
soc_to_extract = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50] # In our publication: 5-50% SOC
    # Recommended within {5, 10, ..., 50}, as batteries with low SOH may not tested with 55% or higher SOC.
    # Adjustable within {5, 10, ..., 90}.
    # Can be non-adjacent.
    # Arranging in ascending order is recommended, but not mandatory.
    # Duplicate content must be avoided.
    # The order of samples recording in the processing file after step 2
    # and the order of worksheet 'SOCi' in the processed data file
    # are decided by element order here.
~~~
In this dataset, each battery has completed pulse test at 5-50% SOC level. However, considering the SOH distribution and our SOC definition for 10Ah LMO, 21Ah NMC and 35Ah LFP batteries, the higher the SOC level, the fewer samples can be extracted.  
#### 4.4.2. Pulse Width
~~~python
pt_to_extract = [5] # In our publication: 5s
    # Adjustable within {0.03, 0.05, 0.07, 0.1, 0.3, 0.5, 0.7, 1, 3, 5}.
    # Can be non-adjacent.
    # Arranging in ascending order is recommended, but not mandatory.
    # Duplicate content must be avoided.
    # The order of samples recording in the processing file after step 2
    # is decided by element order here.
~~~
#### 4.4.3. Pulse Amplitude
~~~python
U_to_extract = range(1,21 +1) # In our publication: U1-U21
    # Adjustable within {1, 2, ..., 41}.
    # Can be non-adjacent.
    # Arranging in ascending order is recommended, but not mandatory.
    # Duplicate content must be avoided.
    # The order of features recording within each samples
    # is decided by element order here.
    # U1: steady state open circuit voltage (OCV) after 10 mins rest
    # U2-U9: voltage at the beginning and end of 0.5C positive pulse, rest, 0.5C negative pulse and rest.
    # U10-U17: 1C. # U18-U25: 1.5C. # U26-U33: 2C. # U34-U41: 2.5C.
~~~
#### 4.4.4. Compared with Reproduction
Compared with [Reproduction](#431-step-1-extract-workstep-sheet), the results of feature engineering will change due to adjustability. Assume there are X elements in `soc_to_extract` and Y elements in `pt_to_extract`. There will be at most X * Y samples from a battery in each file after step 2. The size of each file after step 2 may also be different. After step 3, you will receive Y files. The naming convention is as follows. Each file you receive will contain X + 1 worksheets. The first worksheet 'SOC ALL' contains features under all SOC conditions. Subsequent X worksheets 'SOCi' include features under a single SOC condition, separately. In each worksheets, there are as many samples as the quantity of batteries of that type at most.  
#### Processed Data Filename Format
mat_cap_Ah_W_pulse width(ms unit).xlsx  
#### Example
LMO_10Ah_W_700.xlsx  
NMC_21Ah_W_3000.xlsx  
LFP_35Ah_W_5000.xlsx
# 5. Access
Access the raw data and processed features [here](https://zenodo.org/uploads/11671216) under the [MIT licence](https://github.com/terencetaothucb/Pulse-Voltage-Response-Generation/blob/main/LICENSE). Correspondence to [Terence (Shengyu) Tao](mailto:terencetaotbsi@gmail.com) and CC Prof. [Xuan Zhang](mailto:xuanzhang@sz.tsinghua.edu.cn) and [Guangmin Zhou](mailto:guangminzhou@sz.tsinghua.edu.cn) when you use, or have any inquiries.
# 6. Acknowledgements
[Guangyuan Ma](mailto:magy23@mails.tsinghua.edu.cn) at Tsinghua Berkeley Shenzhen Institute revised the testing experiment plan, unified the original file naming, completed adjustable feature engineering code based on preliminary data processing code, executed feature engineering, uploaded feature engineering code and results, and wrote this instruction document based on supplementary materials.  

We extend our sincere gratitude to Xiamen Lijing New Energy Technology Co., Ltd. for their invaluable contribution to this dataset. The raw data provided by Xiamen Lijing has been instrumental to our research, enriching data resources and providing a solid foundation for analysis. We express our deepest respect and appreciation for the generous support and professionalism of Xiamen Lijing. The completion of this dataset would not have been possible without their assistance. We look forward to future opportunities for collaboration to further advance the field of battery, carbon neutrality and sustainability.  

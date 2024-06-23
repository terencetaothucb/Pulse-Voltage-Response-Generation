# Pulse Voltage Response Generation: PulseBat Dataset
Retired batteries have been presenting a severe sustainability challenge worldwide. One promising sustainable solution is reuse and recycling, but state of health (SOH) information for residual value evaluation retrieved from charge-discharge approaches are still time-consuming and energy-intensive. Developing a data-driven, rapid, and sustainable SOH estimation method for reuse and recycling decision-making is crucial. Here we open-source the collected PulseBat dataset for pulse voltage response generation of the retired batteries across random retirement conditions, i.e., state of charge (SOC) conditions, facilitating downstream SOH estimation tasks. The PulseBat dataset was collected on diversified cathode material types, historical usages, physical formats and capacity designs to deliberately introduce data heterogeneities, which is a common challgenge in retired battery reuse and recycling scenarios. Xiamen Lijing New Energy Technology Co., Ltd., collected the dataset. The collaboration team at Tsinghua Berkeley Shenzhen Institute (TBSI) processed this dataset. AI and battery community will find the PulseBat dataset useful for SOH estimation of retired batteries under transfer learning, continual learning, and generative learning settings.

# 1. Publication
[Generative-learning-assisted Rapid State-of-Health Estimation for Sustainable Battery Recycling with Random Retirement Conditions](To be published)
# 2. Description
## 2.1. Overview
Distinct from the electric vehicle use scenarios, retired batteries exhibit considerable heterogeneities in cathode material types, historical usages, physical formats and capacity designs. We physically tested 270 retired lithium-ion batteries, covering 3 cathode types, 4 historical usages, 3 physical formats, and 4 capacity designs.
#### Battery Types
|Cathode Material|Nominal Capacity (Ah)|Physical Format|Historical Usage|Quantity|
|:--|:--|:--|:--|:--|
|NMC|2.1|Cylinder|Lab Accelerated Aging|67 (from 12 physical batteries)|
|LMO|10|Pouch|HEV1|95|
|NMC|21|Pouch|BEV1|52|
|LFP|35|Square Aluminum Shell|HEV2|56|
## 2.2. Experiment Details
Tests are performed with BAT-NEEFLCT-05300-V010, NEBULA, Co, Ltd, and the air conditioner temperature is set at 25℃.  
Only EV-retired batteries (LMO 10 Ah, NMC 15 Ah, NMC 21 Ah and LFP 35Ah) were subject to this test procedure. Go to Supplementary Note 3 in Supplementary Information for experiment details of Lab Accelerated Aging batteries (NMC 2.1 Ah).  
The experiment is divided into the following three steps: capacity calibration, SOC conditioning, and pulse injection.  
### Step 1 : Capacity Calibration
We use the widely-adopted constant current (CC) discharge method as the gold standard for determining the capacity of retired batteries. Even considering the different initial state of charge (SOC) distributions of retired batteries, we use a unified method of first constant current constant voltage (CCCV) charging and then CC discharging to determine the capacity of retired batteries.  
First, the retired batteries are charged to the upper cut-off voltage using a 1C constant current, then charged using constant voltage until the current drops to 0.05 C.  The batteries are then discharged to the lower cut-off voltage using a 1C constant current. We use the actual discharge capacity as the calibrated (true) battery capacity and then let the battery rest for 20 minutes before SOC conditioning and pulse injection. Here the term C refers to the C-rate, determined by the current value required by a 1h full charge or discharge of a battery.
Cathode Material|Nominal Capacity (Ah)|Cut-Off Voltage for Dis/Charging (V)|
|:--|:--|:--|
|LMO|10|2.0/4.2|
|NMC|15|2.7/4.2|
|NMC|21|2.7/4.2|
|LFP|35|2.5/3.65|
### Step 2 : SOC Conditioning
SOC conditioning refers to adjust the battery SOC to a desired level, necessitated by the fact that retired batteris are of random SOC distributions upon the collection. When the capacity calibration is finished, the battery is at its zero SOC. When a 5% SOC is desired, we use a 1C constant current for 3 minutes to adjust the calibrated battery to a 5% SOC level. The battery is then left to stand for 10 minutes to rest, expecting the battery to return to a steady state in preparation for subsequent pulse injection. 
### Step 3 : Pulse Injection
We perform multiple consecutive pulse injections with different amplitudes, pulse widths and polarizations. The pulse width and pulse resting time are as shown in the following Table, that is, for each pulse width and resting time (each row of the table), we consecutively perform pulse injection with pulse amplitude being 0.5-1-1.5-2-2.5(C) in order, including positive and negative pulse injections. Note that positive and negative pulses alternate to cancel the equivalent energy injection, thus the stored energy inside the battery does not change. Take pulse injection at 5% SOC for an example, at the 30ms pulse width, we inject 0.5C positive current pulse, then let the battery rest for 450ms, and then inject 0.5C negative current pulse, then again let the battery rest for 450ms. Still at 5% SOC, other remaining pulses with different amplitudes follow the rest of the previous pulse injections. Repetitive experiments are performed until the remaining pulse widths are exhausted. Then we charge the retired battery with a constant current of 1C for another 3 minutes to 10% SOC (refer to the SOC conditioning step), followed by the same procedure as explained above.  
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

Repeat Step 2 and Step 3 until the SOC conditioning region is exhausted.
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

The planned SOC range is recorded with a [fixed format on the filename](#31-filename) of each battery. 
#### Protection Voltage
We set protection voltage during pulse injection to ensure the safety of the experiment. The specific protection voltage parameters are consistent with those in the following Table. 
Cathode Material|Nominal Capacity (Ah)|Discharging/Charging (V)|
|:--|:--|:--|
|LMO|10|1.95/4.3|
|NMC|15|2.65/4.25|
|NMC|21|2.65/4.3|
|LFP|35|2.45/3.7|

If the oscillation voltage during pulse injection exceeds the protection range, the current charging or discharging workstep will be immediately terminated. The remaining worksteps in the test procedure will be continued.
#### SOC Deviation
The unequal charged and discharged capacity in adjacent positive and negative pulses with the same pulse intensity and planned pulse time caused by voltage protection will lead to an accumulatable deviation in SOC to subsequent pulse test. Fortunately, this SOC deviation is usually very slight due to the extremely short pulse time with no more than 5s. Moreover, the voltage may exceed the protection range generally when the tested SOC is close to the SOH value of the battery. In [our publication](To be published), we only used data from 5-50% SOC. Considering that the SOH of the vast majority of batteries is above 0.6, the SOC deviation used in [our publication](To be published) can be ignored for simplicity. However, if you want to use data at higher SOC level, you may need to pay attention to this SOC deviation issue to avoid introducing unnecessary errors into machine-learning models.
## 3. Raw Data
### 3.1. Filename
#### Raw Data Filename Format
mat_C_cap_B_no._SOC_soc range lower bound-soc range upper bound_Part_1/2-1/2_ID_id.xlsx
#### Example
LMO_C_10_B_1_SOC_5-55_Part_1-1_ID_PIP15828A00225770.xlsx  
NMC_C_21_B_14_SOC_5-90_Part_1-2_ID_02LCC02100101A87Y0026421.xlsx  
NMC_C_21_B_14_SOC_5-90_Part_2-2_ID_02LCC02100101A87Y0026421.xlsx  
LFP_C_35_B_56_SOC_5-90_Part_1-2_ID_56号.xlsx  

**Instance:** LMO_C_10_B_1_SOC_5-55_Part_1-1_ID_PIP15828A00225770.xlsx refer to the testing of LMO 10Ah battery with index 1 (also indexed by the unique ID: PIP15828A00225770), where the testing SOC region is from 5% to 55%. The testing have 1 out of 1 file.
#### File Part Split Explanation
Sometimes the raw data is split into 2 parts due to the ultra long measurement time and ultra large file size. In this case, only several record layers (i.e. '记录层') will be placed in the second part.  

**Instance:** NMC_C_21_B_14_SOC_5-90_Part_1-2_ID_02LCC02100101A87Y0026421.xlsx refer to the testing of NMC 21Ah battery with index 14 (also indexed by the unique ID: 02LCC02100101A87Y0026421), where the testing SOC region is from 5% to 90%. The testing file is the first file 1 out of 2 files.
## 4. Feature Engineering
We extracted U1-U21 features under 5-50% SOC, 5s pulse width for [our publication](To be published). The features are extracted from turning points, i.e., the points at the beginning and end of pulse injection and rest workstep on the voltage response curve. U1 is the steady state open cicrcuit voltage (OCV) after 10 mins rest. U2-U9 refers to voltage at the beginning and end of 0.5C positive pulse, rest, 0.5C negative pulse, rest, 1C positive pulse, rest, 1C negative pulse, rest, 1.5C positive pulse respectively. The rest time is 25 seconds between each pulse in C-rate. Note that the term C stands for charge (discharge) rate when a 1 hour of charge (discharge) is performed. The recording frequency for step 3 in the raw data is 100 Hz. The ambient temperature is controlled at 25 ℃. 

<p align="center">
  <img src="Feature U1-U21 Description.png" alt="示例图片">
</p>

## 5. Feature Engineering Method
### 5.1. Reproduction
Feature engineering starting from raw data requires three steps.

**Step 1** is to extract the workstep layer (i.e. '工步层') from the raw data of each battery. Step 1 takes a long time and may take several hours or days to complete. If step 1 correctly completed, you will get workstep layer files of each batteries. The file size of each step layer is several hundred KBs. The workstep layer file of each battery is named to be same with the 1st part of the raw data.  
#### Workstep Layer Filename Format
mat_C_cap_B_no.\_SOC_soc range lower bound-soc range upper bound_Part\_**1**-1/2_ID_id.xlsx
#### Example
LMO_C_10_B_1_SOC_5-55_Part_1-1_ID_PIP15828A00225770.xlsx  
NMC_C_21_B_14_SOC_5-90_Part_1-2_ID_02LCC02100101A87Y0026421.xlsx  
LFP_C_35_B_56_SOC_5-90_Part_1-2_ID_56号.xlsx  

**Step 2** is to extract the required features from the step layers of each battery. Step 2 can be completed within one hour. If step 2 correctly completed, you will get 10 features from each battery:  

**Step 3** is to integrate features from different batteries with same type into one file. Step 3 can be completed almost immediately. If step 3 correctly completed, you will obtain proccesed features. The first worksheet 'SOC ALL' contains features under all SOC condition. Subsequent worksheets 'SOCi' include features under a single SOC condition, separately.  

For reproduction, download the [raw data](https://zenodo.org/uploads/11671216) and programs for [Step 1](https://github.com/terencetaothucb/Pulse-Voltage-Response-Generation/blob/main/step_1_extract%20workstep%20sheet.py), [Step 2](https://github.com/terencetaothucb/Pulse-Voltage-Response-Generation/blob/main/step_2_feature%20extraction_adjustable.py), [Step 3](https://github.com/terencetaothucb/Pulse-Voltage-Response-Generation/blob/main/step_3_feature%20collection_adjustable.py) in this repository. Manually create folders for each step and each battery type to store processing and processed data. Update folder addresses in each program. Adjust the cap_mat variable in the program and run to reproduce the feature engineering results of different battery types. All possible adjustments are listed at the top of each code.
#### Notice
Due to unknown reasons, the raw data of battery PIP15827A00221240 (10Ah LMO) has one more rest (i.e. '静置') step than normal. To ensure the correctness of feature extraction, please manually merge row 2020 (the first rest (i.e. '静置') step) and 2021 (the second rest (i.e. '静置') step) in the extracted workstep layer file LMO_C_10_B_2_SOC_5-55_Part_1-1_ID_PIP15827A00221240.xlsx after completing the first step and before the second step. In detail, copy the column K element (3.9837) of row 2020 to replace the column K element of row 2021, then delete row 2020. If you feel that doing so is too troublesome, you can choose to discard battery PIP15827A00221240 directly by deleteing file LMO_C_10_B_2_SOC_5-55_Part_1-1_ID_PIP15827A00221240.xlsx.
### 5.2. Adjustability: Extract Other Features
We extracted U1-U21 features under 5-50% SOC, 5s pulse time or pulse width for [our publication](To be published). Moreover, our feature engineering codes have strong scalability. You can adjust the settings at the top of programs of step 2 and step 3 to extract different features. Remember to keep the settings of the second and third steps consistent.
# Access
Access the raw data and processed features [here](https://zenodo.org/uploads/11671216) under the [MIT licence](https://github.com/terencetaothucb/Pulse-Voltage-Response-Generation/blob/main/LICENSE). Correspondence to [Terence (Shengyu) Tao](terencetaotbsi@gmail.com) and CC Prof. [Xuan Zhang](xuanzhang@sz.tsinghua.edu.cn) and [Guangmin Zhou](guangminzhou@sz.tsinghua.edu.cn) when you use, or have any inquiries.

# Pulse Voltage Response Generation: TBSI-Lijing Battery Dataset
In the retired batteries sustainable utilization scenario, preprocessing steps such as capacity grading and consistency matching is essential to determine how a battery should be reused or recycled. The conventional approach of measuring battery state of health (SOH), charge-discharge profiles, and other related properties through long-time charge-discharge cycle is both time-consuming and energy-intensive. Therefore, developing rapid, non-invasive, and sustainable preprocessing methods for randomly retired batteries is crucial. However, actual measured data in this field are very limited, both in terms of the quantity of retired batteries and the diversity of battery chemistries and materials. To address this gap, we open-source this Pulse Voltage Response Generation: TBSI-Lijing Battery Dataset to foster further academic research and industrial applications in the field of battery SOH fast estimation and consistency fast assessment. Xiamen Lijing New Energy Technology Co., Ltd., collected this dataset. The collaboration team at Tsinghua Berkeley Shenzhen Institute (TBSI) processed this dataset and utilized generative models for data augmentation, significantly enhancing the economic feasibility of large-scale battery repurposing.
# Publication
[Generative-learning-assisted Rapid State-of-Health Estimation for Sustainable Battery Recycling with Random Retirement Conditions](To be published)
# Description
## Overview
Retired batteries exhibit high heterogeneities in cathode material types, physical formats, capacity designs, and historical usages. Here we tested 353 retired lithium-ion batteries, covering 5 capacity designs, 3 cathode types, 3 physical formats, and 5 historical usages.
### Battery Types
Nominal Capacity (Ah)|Cathode Material|Physical Format|Historical Usage|Quantity|
|:--|:--|:--|:--|:--|
|NMC|2.1|Cylinder|Lab Accelerated Aging|67 (12 in different aging stage)|
|LMO|10|Pouch|HEV1|95|
|NMC|15|Pouch|BEV1|83|
|NMC|21|Pouch|BEV2|52|
|LFP|35|Square Aluminum Shell|HEV2|56|
## Experiment Details
Tests are performed with BAT-NEEFLCT-05300-V010, NEBULA, Co, Ltd, and the air conditioner temperature is set at 25℃.  
Only EV-retired batteries (LMO 10 Ah, NMC 15 Ah, NMC 21 Ah and LFP 35Ah) were subject to this test procedure. Go to Supplementary Note 3 in Supplementary Information for experiment details of Lab Accelerated Aging batteries (NMC 2.1 Ah).  
The experiment is divided into the following three steps: capacity calibration, SOC conditioning, and pulse injection.  
### Step 1 : Capacity Calibration
We use the constant current (CC) discharge method as the gold standard for determining the capacity of retired batteries. Even considering the different initial state of charge (SOC) distributions of retired batteries, we use a unified method of first constant current constant voltage (CCCV) charging and then CC discharging to determine the capacity of retired batteries.  
First, the retired batteries are charged to the upper cut-off voltage using a 1C constant current, then charged using constant voltage until the current drops to 0.05 C. Third, they are then discharged to the lower cut-off voltage using a 1C constant current. We use the actual discharge capacity as the calibrated battery capacity and then let the battery stand for 20 minutes before SOC conditioning and pulse injection.
Cathode Material|Nominal Capacity (Ah)|Cut-Off Voltage for Dis/Charging (V)|
|:--|:--|:--|
|LMO|10|2.0/4.2|
|NMC|15|2.7/4.2|
|NMC|21|2.7/4.2|
|LFP|35|2.5/3.65|
### Step 2 : SOC Conditioning
After completing the rest of the calibrated battery, SOC conditioning is performed to inject pulses at the desired SOC levels. Charge the retired battery with a constant current of 1C for 3 minutes to 5% SOC, and then cut off the charging current. The battery is then left to stand for 10 minutes to rest, expecting the battery to return to a steady state in preparation for subsequent pulse injection. 
### Step 3 : Pulse Injection
Then, perform multiple consecutive pulse injections with different pulse widths. The pulse width and pulse resting time are as shown in the following Table, that is, for each pulse width and resting time (each row of the table), we consecutively perform pulse injection with pulse amplitude being 0.5-1-1.5-2-2.5(C) in order, including positive and negative pulses. Note that positive and negative pulses alternate to cancel the equivalent energy injection. For instance, at the 30ms pulse width, we inject 0.5C positive current pulse, then let the battery rest for 450ms, and then inject 0.5C negative current pulse, then again let the battery rest for 450ms. Other remaining pulses with different amplitudes follow the rest of the previous pulse injections. When the last pulse and rest are finished, all the required experiments at 30ms pulse width are finished. Repetitive experiments are performed until the remaining pulse widths are exhausted, indicating all pulse injections at 5% SOC are completed. Then charge the retired battery with a constant current of 1C for another 3 minutes to 10% SOC, followed by the same procedure as explained above.  
|Pulse Width t1|Pulse Rest Time t2|Pulse Amplitude (±C)|
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
#### SOC Range for Test
The range of SOC conditioning is determined by a previously simply estimated SOH of the retired battery. Specifically, the upper bound of the SOC conditioning region is lower than the previously simply estimated SOH value of the retired battery for at least 0.05. For instance, when the retired battery has a previous simply estimated SOH between 0.5 and 0.55, then the SOC conditioning region will be 5% to 45%, with a grain of 5%. The mapping of determing SOC conditioning region determined by previously simply estimated SOH is shown in the table below.  
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

The planned SOC range is recorded with a [fixed format on the filename](#filename-format) of each battery. 
#### Protection Voltage
In addition, we set protection voltage during pulse injection to ensure the safety of the experiment. The specific protection voltage parameters are consistent with those in the following Table.
Cathode Material|Nominal Capacity (Ah)|Protection Voltage for Dis/Charging (V)|
|:--|:--|:--|
|LMO|10|1.95/4.3|
|NMC|15|2.65/4.25|
|NMC|21|2.65/4.3|
|LFP|35|2.45/3.7|

If the oscillation-eliminated voltage during pulse injection exceeds the protection range, the current charging or discharging workstep will be immediately terminated. The remaining worksteps in the test procedure will be continued.
##### SOC Deviation
The unequal charged and discharged capacity in adjacent positive and negative pulses with the same pulse intensity and planned pulse time caused by voltage protection will lead to an accumulatable deviation in SOC to subsequent pulse test. Fortunately, this SOC deviation is usually very slight due to the extremely short pulse time with no more than 5s. Moreover, the voltage may exceed the protection range generally when the tested SOC is close to the SOH value of the battery. In [our publication](To be published), we only used data from 5-50% SOC. Considering that the SOH of the vast majority of batteries is above 0.6, the SOC deviation used in [our publication](To be published) can be ignored for simplicity. However, if you want to use data at higher SOC level, you may need to pay attention to this SOC deviation issue to avoid introducing unnecessary errors into machine-learning models.
## Raw Data
### Filename Format
mat_C_cap_B_no._SOC_soc range lower bound-soc range upper bound_Part_1/2-1/2_ID_id.xlsx
#### Example
LMO_C_10_B_1_SOC_5-55_Part_1-1_ID_PIP15828A00225770.xlsx  
NMC_C_21_B_14_SOC_5-90_Part_1-2_ID_02LCC02100101A87Y0026421.xlsx  
NMC_C_21_B_14_SOC_5-90_Part_2-2_ID_02LCC02100101A87Y0026421.xlsx  
LFP_C_35_B_56_SOC_5-90_Part_1-2_ID_56号.xlsx
##### Part Split Explanation
Sometimes the raw data is split into 2 parts due to the ultra long measurement time and ultra large file size. In this case, only several record layers (i.e. '记录层') will be placed in the second part.
## Processed Data
We extracted U1-U21 features under 5-50% SOC, 5s pulse time or pulse width for [our publication](To be published). Here, U1 is the steady state open cicrcuit voltage (OCV) after 10 mins rest. U2-U9 refers to voltage at the beginning and end of 0.5C positive pulse, rest, 0.5C negative pulse, rest, 1C positive pulse, rest, 1C negative pulse, rest, 1.5C positive pulse respectively.
![Feature extraction description](https://github.com/terencetaothucb/Pulse-Voltage-Response-Generation/assets/161430150/5a67ef25-baae-4e86-926e-ee6c64607800)  
The pulse voltage response features (from U1 to U21) of hybrid electric vehicle driving aging batteries (LMO, 10Ah). Each subplot shares an identical voltage and state of health (SOH) value scale, with the state of charge (SOC) indicated by a color bar.  
![Processed data for 10Ah LMO in general](https://github.com/terencetaothucb/Pulse-Voltage-Response-Generation/assets/161430150/92c9e484-56dd-487a-975c-3cc2066028c5)
## Reproducing Feature Engineering Results with our code
Feature engineering starting from raw data requires three steps. The first step is to extract the workstep layer (i.e. '工步层') from the raw data of each battery. The second step is to extract the required features from the step layers of each battery. The third step is to integrate the features from different batteries with the same material into one or several files.  
For reproducing, download the [raw data](https://zenodo.org/uploads/11671216) and programs in this repository. Manually create folders to store processing and processed data. Update folder addresses in each program. Adjust the cap_mat variable in the program and run to reproduce the feature engineering results of different batteries. All possible adjustments are listed at the top of the code.  
The first step takes a long time and may take several hours or days to complete. The second step can be completed within one hour. The third step can be completed almost immediately.
##### Notice
Due to unknown reasons, the raw data of battery PIP15827A00221240 (10Ah LMO) has one more rest (i.e. '静置') step than normal. To ensure the correctness of feature extraction, please manually merge row 2020 (the first rest (i.e. '静置') step) and 2021 (the second rest (i.e. '静置') step) in the extracted workstep layer file LMO_C_10_B_2_SOC_5-55_Part_1-1_ID_PIP15827A00221240.xlsx after completing the first step and before the second step. In detail, copy the column K element (3.9837) of row 2020 to replace the column K element of row 2021, then delete row 2020. If you feel that doing so is too troublesome, you can choose to discard battery PIP15827A00221240 directly by deleteing file LMO_C_10_B_2_SOC_5-55_Part_1-1_ID_PIP15827A00221240.xlsx.
### Adjustablity: Extract Other Features 
We extracted U1-U21 features under 5-50% SOC, 5s pulse time or pulse width for [our publication](To be published). Moreover, our feature engineering code has strong scalability. You can adjust the settings at the top of the second and third step programs to extract different features. Remember to keep the settings of the second and third steps consistent.
# Access
Access the raw data and processed features [here](https://zenodo.org/uploads/11671216) under the [MIT licence](https://github.com/terencetaothucb/Pulse-Voltage-Response-Generation/blob/main/LICENSE). Correspondence to [Terence (Shengyu) Tao](terencetaotbsi@gmail.com) and CC to Prof. [Xuan Zhang](xuanzhang@sz.tsinghua.edu.cn) and [Guangmin Zhou](guangminzhou@sz.tsinghua.edu.cn) when you use, or have any inquiries.

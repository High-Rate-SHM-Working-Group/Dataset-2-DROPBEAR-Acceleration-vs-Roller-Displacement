# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import IPython as IP
IP.get_ipython().magic('reset -sf')

import numpy as np
import sklearn as sk
import json as json
import matplotlib.pyplot as plt
plt.close('all')


#%% Plot data

#D = json.load('../data/DROPBEAR_dataset.json')



with open('../data/DROPBEAR_dataset.json') as f:
  data = json.load(f)
  
# acceleration_data_tt = np.arange(len(data['acceleration_data']))*1/data['accelerometer_sample_rate']


# data_2={'measured_pin_location_tt':data['measured_pin_location_tt'],
#         'measured_pin_location':data['measured_pin_location'],
#         'acceleration_data':data['acceleration_data']}  
  
# with open('../data/DROPBEAR_dataset.json', 'w') as outfile:
#     json.dump(data, outfile)  
  
plt.figure(figsize=(6.5,4))
plt.plot(data['measured_pin_location_tt'],data['measured_pin_location'])  
plt.xlabel('time (s)')
plt.ylabel('pin_location')
  
  

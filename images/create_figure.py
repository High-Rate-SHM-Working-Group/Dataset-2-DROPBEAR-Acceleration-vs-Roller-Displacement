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


with open('../data/DROPBEAR_dataset.json') as f:
  data = json.load(f)
  
measured_pin_location_tt = np.asarray(data['measured_pin_location_tt'])
measured_pin_location = np.asarray(data['measured_pin_location'])
acceleration_data_tt = np.asarray(data['acceleration_data_tt'])
acceleration_data = np.asarray(data['acceleration_data'])

plt.figure(figsize=(6.5,3))
plt.plot(measured_pin_location_tt,measured_pin_location)  
plt.xlabel('time (s)')
plt.ylabel('pin location (m)')
plt.grid(True)
plt.xlim([0,44])
plt.tight_layout()
plt.savefig('pin_locatoin_data')



plt.figure(figsize=(6.5,3))
plt.plot(acceleration_data_tt,acceleration_data,lw=0.1)  
plt.xlabel('time (s)')
plt.ylabel('acceleration (m/s$^2$)')
plt.grid(True)
plt.xlim([0,44])
plt.tight_layout()
plt.savefig('acceleration_data')















  

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 22:26:14 2020

@author: Asif
"""

from GCM import GCM
from formats import FORMAT
from features import FEATURE
from CSV import CSV
import numpy as np
import os

for filename in os.listdir(os.getcwd()+"\\raw_data"):
    #print(filename)
    csv = CSV(filename)
    csv.generate_csv()

for filename in os.listdir(os.getcwd()+"\\csv"):
    #print(filename)
    frmt = FORMAT(filename)
    frmt.format()

ctr = 0
data = np.array([[]])
for filename in os.listdir(os.getcwd()+"\\graph"):
    ctr = ctr + 1
    print(filename)
    feature = FEATURE(filename)
    dt = feature.generate_feature()
    print(dt.shape)
    if ctr == 1:
        data = dt
    else:
       data =  np.concatenate((data,dt))
       data = np.delete(data, ctr, 0)
      
   
    
    
    
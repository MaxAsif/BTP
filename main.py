# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 22:26:14 2020

@author: Asif
"""

from GCM import GCM
from formats import FORMAT
from features import FEATURE
from CSV import CSV

import os

filename = r'co2a0000364.csv'
fm = FORMAT(filename)
f = fm.format()

gcm = GCM(f)
f1 = gcm.generate_graph()

ftr = FEATURE(f1)
data = ftr.generate_feature()

import os
for filename in os.listdir(os.getcwd()+"\\raw_data"):
    #print(filename)
    csv = CSV(filename)
    csv.generate_csv()

for filename in os.listdir(os.getcwd()+"\\csv"):
    #print(filename)
    frmt = FORMAT(filename)
    frmt.format()
    
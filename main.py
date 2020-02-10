# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 22:26:14 2020

@author: Asif
"""

from GCM import GCM
from format import FORMAT
from features import FEATURE

import os

filename = r'co2a0000364.csv'
fm = FORMAT(filename)
f = fm.format()

gcm = GCM(f)
f1 = gcm.generate_graph()

ftr = FEATURE(f1)
data = ftr.generate_feature()

input_file = open('co2a0000364.rd.028', 'r')
output_file = open("sds.csv", 'w')
input_file.readline() # skip first line 
input_file.readline()
input_file.readline()
input_file.readline()
input_file.readline()
lst = ['Trial','chan','Time','Voltage']
output_file.write(','.join([lst[0], lst[1], lst[2], lst[3]]) + '\n')
for line in input_file:
    lst = line.strip().split(' ')
    output_file.write(','.join([lst[0], lst[1], lst[2], lst[3]]) + '\n')
input_file.close()
output_file.close()
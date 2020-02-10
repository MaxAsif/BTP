# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 22:26:14 2020

@author: Asif
"""

from GCM import GCM
from format import FORMAT
from features import FEATURE

filename = r'co2a0000364.csv'
fm = FORMAT(filename)
f = fm.format()

gcm = GCM(f)
f1 = gcm.generate_graph()

ftr = FEATURE(f1)


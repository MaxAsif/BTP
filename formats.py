# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from GCM import GCM

class FORMAT:
    filename = ''
    
    def __init__(self,f):
        self.filename = f;
        
    def format(self):        
        # READING CSV FILES
        print(self.filename)
        df = pd.read_csv("csv/"+self.filename)
        
        """# REMOVING UNNECESSARY COLUMNS
        df = df[df.columns[1:4]]
        
        # REMOVE HEADERFILES
        df = df.drop(df.index[0])
        df = df.drop(df.index[0])
        df = df.drop(df.index[0])
        
        # RENAME COLUMNS
        df = df.rename(columns={"co2a0000364.rd":"chan", "Unnamed: 2":"Time", "Unnamed: 3":"Voltage"})
        """
        # REEMOVE ROWS IN BETWEEN
        df = df[df.Time != 'chan']
        
        # RESET INDEX 
        df = df.reset_index()
        df = df[df.columns[1:5]]
        
        df.count()
        # ALL CHANNELS NAME LIST
        channels = df.chan.unique().tolist()
        
        # LOOP TO ORIENT DATA
        i = 0
        for chn in channels:
            df1 = df.loc[[*range(i,i+256,1)],['Voltage']].reset_index()
            df1 = df1[df1.columns[1:]]
            df[chn] = df1
            i = i+256
        
        # DROPS ROWS after    
        df = df.drop(df.index[256:])
        
        df = df.drop(["chan","Voltage"],axis = 1)
        
        # EXPORT TO CSV FILES
        ret = 'output/'+self.filename
        df.to_csv(ret, encoding='utf-8', index=False)
        return ret
        
#obj = FORMAT("co2a0000364.csv")
#obj.format()
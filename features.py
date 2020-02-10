# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:41:06 2019

@author: Asif
"""
from numpy import genfromtxt
import numpy as np
import networkx as nx
import pandas as pd

class FEATURE:
    
    filename = ''
    
    def __init__(self,f):
        self.filename = f
    
    def generate_feature(self):
        mydata = genfromtxt("graph/"+self.filename, delimiter=',')
        
        adjacency = mydata[1:,:]
        
        G = nx.from_numpy_matrix(adjacency, create_using=nx.DiGraph())
        
        # INitialize Data set
        data = np.array([[]])
        k = []
        v = []
        #wCC
        wCC_dict = nx.clustering(G)
        wCC_k = ['wCC_'+str(x) for x in list(wCC_dict.keys())]
        wCC_v = list(wCC_dict.values())
        
        #wAND
        wAND_dict = nx.average_neighbor_degree(G)
        wAND_k = ['wAND_'+str(x) for x in list(wAND_dict.keys())]
        wAND_v = list(wAND_dict.values())
        
        #wNBC
        wNBC_dict = nx.betweenness_centrality(G)
        wNBC_k = ['wAND_'+str(x) for x in list(wNBC_dict.keys())]
        wNBC_v = list(wNBC_dict.values())
        
        # Merge
        k = wNBC_k + wAND_k + wCC_k
        v = wNBC_v + wAND_v + wCC_v
        #Insert
        data = np.append(data,[k], axis = 1)
        data = np.append(data,[v], axis = 0)
        return data
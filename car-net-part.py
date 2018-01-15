# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 17:46:53 2018

@author: yexin
"""

import jieba

'''    
from sklearn import metrics 
#import sklearn   
import pickle as pickle    
import pandas as pd
'''

#映射表 
car_net={}
with open('car-net-part.csv','r') as stop_word:
    lines = stop_word.readlines()#所有行读出
    #print "mapmapmapmap******",lines[0],lines[1]
    #print len(lines)
    #循环遍历
    #print('******************* %s ***' % lines[0],lines[1]) 

    #print (type (lines[0]))

    #print('******************* %s ******' % len(lines)) 
    
    
    list=[]
    i=1
    while i<len(lines):
       sss=lines[i].split(",")
       k=sss[0]
       v=sss[1]
       #print('******************* %s ***' % v) 
       seg_list=jieba.lcut(v.strip(),cut_all=True)
       list.append(seg_list)
       #print (type (seg_list))
       #print (seg_list)
       #car_net[sss[0]]=seg_list
       #print('字典字典字典',car_net)
       i +=1
print(list)    
    
'''    
    sss=lines[1].split(",")
    v1=sss[1]
    seg_list=jieba.cut(v1,cut_all=True)
    
    print ( ','.join(seg_list))
'''    


   
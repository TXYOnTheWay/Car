# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 09:16:43 2018

@author: yexin
"""
import jieba
import re


#定义函数，将文本进行切词，然后生成列表
#i=源数据中的开始列数，例如i=1为‘车型’列，i=2为‘标题’列
#j=源数据中的行数，例如j=1为表头，j=2业务数据
#m=源数据中的时间列
def seg_list(filepath2,i,j,m):
    wlist=[]
    relist=[]
    list1=filetolist(filepath2)
    r=j
    while r<len(list1):
        sentence=list1[r].strip().split(',')#生成列表
        sentence1=sentence[i]#结巴分词
        wordlist=seg_sentence(sentence1)
        wlist.append(wordlist)
        sentence2=sentence[m]#正则表达式，处理时间列 
        relist.append(sentence2)
        r +=1
    return wlist,relist

#读取文本文件，并生成列表
def filetolist(filepath1):
    list = [line.strip() for line in open(filepath1, 'r',encoding='UTF-8').readlines()]  
    return list
#正则表达式
def re_regular(relist):
    re_list=[]
    for regular_words in relist:
        re_words = re.sub("\D", "",regular_words)
        print (regular_words)
        re_list.append(re_words)
    return re_list    

#通过jieba进行分词    
def seg_sentence(sentence):
    word_list=[]
    sentence_seged = jieba.cut(sentence.strip())  
    stopwords = filetolist(filepath3)  # 这里加载停用词的路径    
    #print(stopwords)    
    for word in sentence_seged:  
        if word not in stopwords:  
            word_list.append(word)
    return word_list


filepath2='car-net2.csv'
wlist1,relist1=seg_list(filepath2,1,1,5)
relist_name=re_regular(relist1)
print (wlist1,relist_name)









  
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 17:23:20 2018

@author: tianx
"""
import jieba

#读入文件，并存成词典
#i指的是最后截去几位
def filetodict(filepath1,filename1,i):
    filedict = {}
    contentlist = [line.strip() for line in open(filepath1+filename1, 'r',encoding='UTF-8').readlines()]  
    filedict[filename1[0:len(filename1)-i]]=contentlist
    return filedict

'''
#测试
dict1=filetodict('E://电信/项目/外部数据挖掘项目/质量协会/指标/','一发动机.txt',4)
print(dict1)
'''

#标签集
def dictlist(filepath1,filename1,filename2,filename3,filename4,filename5,filename6,filename7,filename8,filename9,filename10,filename11,i):
    dict_list=[]
    dict1=filetodict(filepath1,filename1,i)
    dict_list.append(dict1)
    dict2=filetodict(filepath1,filename2,i)
    dict_list.append(dict2)
    dict3=filetodict(filepath1,filename3,i)
    dict_list.append(dict3)
    dict4=filetodict(filepath1,filename4,i)
    dict_list.append(dict4)
    dict5=filetodict(filepath1,filename5,i)
    dict_list.append(dict5)
    dict6=filetodict(filepath1,filename6,i)
    dict_list.append(dict6)
    dict7=filetodict(filepath1,filename7,i)
    dict_list.append(dict7)
    dict8=filetodict(filepath1,filename8,i)
    dict_list.append(dict8)
    dict9=filetodict(filepath1,filename9,i)
    dict_list.append(dict9)
    dict10=filetodict(filepath1,filename10,i)
    dict_list.append(dict10)
    dict11=filetodict(filepath1,filename11,i)
    dict_list.append(dict11)
    return dict_list

labeldictlist=dictlist('E://电信/项目/外部数据挖掘项目/质量协会/指标v2/','一安全.txt','一变速箱与传动.txt','一车内空间.txt','一车身外观.txt','一电子设备.txt','一发动机.txt','一驾驶操控和视野.txt','一空调.txt','一零部件.txt','一内饰.txt','一座椅.txt',4)   
#print(labeldictlist)

#读取文本文件，并生成列表
def filetolist(filepath1):
    list = [line.strip() for line in open(filepath1, 'r',encoding='UTF-8').readlines()]  
    return list

#对每一行进行分词，filepath3是停用词路径
def seg_sentence(sentence,filepath3):
    word_list=[]
    sentence_seged = jieba.cut(sentence.strip())  
    stopwords = filetolist(filepath3)  # 这里加载停用词的路径    
    #print(stopwords)    
    for word in sentence_seged:  
        if word not in stopwords:  
            word_list.append(word)
    return word_list

    
#读入待分类文本，分词并存成字典
#filepath2是待分类文本的路径及文件名，filepath3是停用词的路径及文件名
#i=源数据中的开始列数，例如i=1为‘车型’列，i=2为‘标题’列
#j=源数据中的行数，例如j=1为表头，j=2业务数据
def classifyfile(filepath2,filepath3,i,j):
    wdict={}
    list1=filetolist(filepath2)
    r=j
    while r<len(list1):
        sentence=list1[r].strip().split(',')#生成列表
        sentence1=sentence[i]#结巴分词
        wordlist=seg_sentence(sentence1,filepath3)
        wdict[sentence1]=wordlist
        r +=1
    return wdict

worddict=classifyfile('E://电信/项目/外部数据挖掘项目/质量协会/项目预研/cardata.csv','E://电信/项目/外部数据挖掘项目/质量协会/项目预研/stopwords.txt',2,1)
#print(worddict)

#给文本打标签
def sentencelabel(labeldictlist,worddict):    
    sentencelabeldict={}
    for sentence in worddict.keys():
        stlabel=[]
        for i in range(len(labeldictlist)):
            for labelkey in labeldictlist[i].keys():
                for word in worddict[sentence]:
                    for label in labeldictlist[i][labelkey]:
                        if word==label:
                            stlabel.append(labelkey)
        sentencelabeldict[sentence]=stlabel
    return sentencelabeldict

test=sentencelabel(labeldictlist,worddict)                
#print (test)       

#查找字典中value是空的
def selectnull(test):
    test1={}
    for i in test.keys():
        if test[i]==[]:
            test1[i]=[]
    return test1

test1=selectnull(test)
print (test1)



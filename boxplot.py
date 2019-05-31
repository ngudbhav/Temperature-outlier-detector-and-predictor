import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy
from matplotlib.cbook import boxplot_stats
data = [None] * 3
data[0] = pd.read_csv('JAFARPUR.csv')
data[1] = pd.read_csv('AYANAGAR.csv')
data[2] = pd.read_csv('NAJAFGARH.csv')
data[0].head(10)
data[1].head(10)
data[2].head(10)
for index1, i in enumerate(data):
    newarrdata = [0] * len(data)
    for ij, ji in enumerate(data):
        newarrdata[ij] = ji['TEMP'].values
    #print(newarrdata)
    #newarrdata[0] = i['TEMP'].values;
    #newarrdata
    index=0
    tips = sns.boxplot(x=i["TEMP"])
    plt.show()
    outliers = [y for stat in boxplot_stats(i['TEMP']) for y in stat['fliers']]
    #deletedData = [[0 for x in range(len(outliers))] for y in range(3)]
    deletedData= []
    for i1 in range(3):
        tmp1= []
        deletedData.append(tmp1)
    #print(deletedData)
    print(outliers)
    #tmp = []
    for j in outliers:
        #print(j)#i se match nhi krna...newarrdata se match krna hai... ye algo galat hai
        con = i[i['TEMP'] == j]
        #print(newarrdata[newarrdata == j])
        #print(i.index[i['TEMP'] == j].tolist())
        indexf = int(con.index.values.astype(int)[0])
        #print(indexf)
        x = con['S NO.'].values[0] - 1
        index = 0
        #x is the index of every outlier
        #print(x)
        #delete the entry from the original file
        #print(index1)
        inde = np.argwhere(newarrdata[index1]==j)
        newarrdata[index1]=np.delete(newarrdata[index1], inde, axis=0)
        print(newarrdata[index1])
        for index2, k in enumerate(data):
            #print(k)
            if index2!=index1:
                #print(index)
                #newarrdata[index2]=k['TEMP'].values
                nd = k[k['TIME'] == con['TIME'].values[0]]
                if not nd.empty:
                    indexOfArray = int(nd.index.values.astype(int)[0])
                    #print(indexOfArray)
                    val1 = nd['TEMP'].values[0]
                    teh = nd['S NO.'].values[0]
                    #tmp.append(newarrdata[index][teh - 1])
                    #Distance calculation between 2 np arrays!
                    #print(index2)
                    deletedData[index2].append(newarrdata[index2][indexOfArray])
                    newarrdata[index2] = np.delete(newarrdata[index2], indexOfArray, axis=0)
            index+=1
            if(index == len(data)):
                break
    #print(tmp)
    #print(newarrdata[0])
    #print(newarrdata[1])
    #print(newarrdata[2])
    if(len(outliers)>0):
        print(deletedData)
        cor = []
        for i2 in range(10):
            cor.append(0)
        for i3 in range(1, len(newarrdata)):
            print(i3)
            if(type(newarrdata[i3]) != int):
                if(newarrdata[0].shape == newarrdata[i3].shape):
                    t = scipy.spatial.distance.correlation(newarrdata[0],newarrdata[i3])
                    cor[i3] = 1-t
                    print(i3)
                    print(newarrdata[0])
                    print(newarrdata[1])
                    print(1-t)
        maxi= -1
        pos = -1
        print(cor)
        for i in range(1,len(data)):
            if maxi < cor[i]:
                maxi = cor[i]
                pos = i
        print(maxi)
        for num in deletedData[pos]:
            print(num*maxi)
    #print()
    #Correlation is 1 minus the distance between them!
    #cor1 = 1-cor1
    #cor2 = 1-cor2
    #print(cor1)
    #print(cor2)
        # x index pr value delete ho gyi
        
    #newarrdata is final array without outliars
#print(data['TEMP'])
#print("Getting outliars")
#print(con['S NO.'].values[0])

#print(newarrdata)

#Working on neighbouring stations
#timestamp pr temp nikaal rhi hai dusri file se


val1 = 0
cor1 = 0
#teh=0

#print(teh)
#print(newarrdata1)

#print((cor1)*val1)

#print((val1+val2)/2)
#plt.show()

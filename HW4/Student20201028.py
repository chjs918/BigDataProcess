#!/usr/bin/pyton3

import sys
import numpy as np
import operator
from os import listdir

train = sys.argv[1]
test = sys.argv[2]
testDigits = listdir(test)
trainDigits = listdir(train)

def classify0(inX, dataSet, labels, k): 
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2 
    sqDistances = sqDiffMat.sum(axis = 1) 
    distances = sqDistances ** 0.5 
    sortedDistIndicies = distances.argsort() 
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]] 
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key= operator.itemgetter(1), reverse=True) 
    return sortedClassCount[0][0]     


def fileToMatrix(filename): 
    initMat = np.zeros((1, 1024)) 

    with open(filename) as f:
        for i in range(32):
            line = f.readline()
            for j in range(32):
                initMat[0, 32*i + j] = int(line[j])

        return initMat   


def createDataSet(dataset):
    group = np.zeros((len(trainDigits), 1024))
    labels = []
    
    for i in range(len(trainDigits)): 
        fileName = trainDigits[i]
        realNum = fileName.split('_')[0] 
        labels.append(int(realNum))
        group[i, :] = fileToMatrix(dataset + '/' + fileName)

    return group, labels 
	
	
group, labels = createDataSet(train)

for k in range(1, 21):
    error = 0
    cnt = 0 
    
    for i in range(len(testDigits)): 
        testData = fileToMatrix(test + '/' + testDigits[i])
        answer = int(testDigits[i].split('_')[0])
        classifyData = classify0(testData, group, labels, k)
        if classifyData != answer :
            error += 1
        cnt += 1
    rst = int((error / cnt) * 100)
    print(rst)  
   



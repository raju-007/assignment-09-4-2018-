# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 09:50:53 2018

@author: rajashekhar
"""

def maxSubArray(ls):
    lk=[]
    if len(ls) == 0:
       raise Exception("Array empty") 
      
    runSum = maxSum = ls[0]
    i = 0
    start = finish = 0

    for j in range(1, len(ls)):
        if ls[j] > (runSum + ls[j]):
            runSum = ls[j]
            
            i = j
            
        else:
            runSum += ls[j]
            

        if runSum > maxSum:
            
            maxSum = runSum
            start = i
            finish = j

    print ("maxSum =>", maxSum)
    print ("start =>", start, "; finish =>", finish)
    k=start
    while k<=finish:
        lk+=[ls[k]]
        k+=1
    print(lk)
    
maxSubArray([-2, 11, -4, 13, -5, 2])

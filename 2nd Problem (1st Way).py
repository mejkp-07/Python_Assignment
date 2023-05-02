# -*- coding: utf-8 -*-
"""
Created on Mon May  1 14:30:48 2023

@author: Jay Kumar
"""

def result(arr, n, N):
    count = 0
    size = 1
    while(size <= n):
        i = 0
        j = i + size
        while(j <= n):
            sum = 0
            k = i
            while(k < j):
                sum = sum + arr[k]
                k +=1
            if(sum == N):
                count += 1
            i += 1
            j += 1
        size += 1
    return count
                

N = int(input("Enter the Number"))
arr = []
for i in range(1, N + 1, 2):
    arr.append(i)
print(arr)


res = result(arr, len(arr), N)
print(res)
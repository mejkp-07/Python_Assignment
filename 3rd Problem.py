# -*- coding: utf-8 -*-
"""
Created on Mon May  1 15:42:26 2023

@author: Jay Kumar
"""

from threading import Thread 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def threaded_factorial(n):
    result = 0
    def threaded_initiate():
        nonlocal result
        result = factorial(n)
    t = Thread(target=threaded_initiate)
    t.start()
    t.join()
    return result

print(factorial(5))
print(threaded_factorial(5))

    
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 13:45:19 2021

@author: Chris Chiang
"""
import random
pwd= random.sample(range(0,10),4)
print(pwd)

A=0
B=0

while A != 4:
    num = input("Plz wnter 4 numbers: ")
    while len(num) !=4 or len(set(num)) !=4:
        num = input("Plz wnter 4 numbers and don't repeat: ")
    list1 = list(map(int,list(num)))
    print(list1)
    A = 0
    B = 0
    for i in list1:
        if i in pwd:
            if list1.index(i) == pwd.index(i):
                A += 1
            else:
                B += 1
    print(num,":",A,"A",B,"B",sep="")

print ("Correct! The PW is",num)
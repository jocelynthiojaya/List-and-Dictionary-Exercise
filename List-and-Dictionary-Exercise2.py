# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:58:05 2019

@author: jocel
"""

#Exercise 2
prices = {
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}

stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

for i in prices:
    print(i)
    print("price: ", prices[i])
    print("stock: ", stock[i])
    
total = 0
for i in prices: 
    total += prices[i] * stock[i]
print(total)
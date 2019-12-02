# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:58:49 2019

@author: jocel
"""

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

groceries = ['banana', 'orange', 'apple']
def compute_bill(fruit: [str]):
    total = 0
    for i in fruit:
        if stock[i] > 0:
            stock[i] -= 1
            total += prices[i]
    return total

print(compute_bill(groceries))
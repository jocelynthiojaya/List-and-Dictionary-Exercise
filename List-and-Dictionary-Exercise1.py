# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:55:47 2019

@author: jocel
"""

#Exercise 1
inventory = {
 'gold' : 500,
 'pouch' : ['flint', 'twine', 'gemstone'],
 'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

inventory['pocket'] = 'seashell','strange berry','lint'
print(inventory)

inventory['backpack'].sort()
print(inventory)

inventory['backpack'].remove('dagger')
print(inventory)

inventory['gold'] = inventory['gold'] + 50
print(inventory['gold'])
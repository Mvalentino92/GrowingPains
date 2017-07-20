# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 15:15:51 2017

@author: michael
"""

from __future__ import division
from time import sleep

print 'Please put in numbers as militers, not microliters'
print '\n'
Original_Sample = input('How much is your orignal sample? ')

Working_Sample = input('How much are you going to use for the dilutions? ')

Final_Sample = Original_Sample - Working_Sample

Dilution_Factor = input('What is your dilution factor? Type like 1e-6: ')

Drop_Volume = input('How much did you use for your drop? ' )

Colonies = input('How many colonies did you count? ')

CFU = (Colonies/Dilution_Factor)

CFU_perMl = CFU/Drop_Volume

Cell_Count = Final_Sample*CFU_perMl

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 17:03:52 2017

@author: michael
"""

from __future__ import division
from time import sleep
#Ask all questions
Sample_num = input('And how many samples will you be doing total? ')
DNA_max = input('How many microliters will your largest DNA sample be? ')
d_FP = input('How much primer concentration?\nChoose from 0.2-1.0: ')
d_Concentration_Primers = input('What are the default concentrations of your Primers? ')
#Define the default values for a standard 50 microliter PCR
d_total = 50.0
d_Taq = 0.25
d_Buffer = 5.0
d_Dntp = 4.0
d_FP = (d_total*d_FP)/d_Concentration_Primers
d_BP = d_FP
#Append the list of reactants to a list
Mix = [d_Taq,d_Buffer,d_Dntp,d_FP,d_BP]

# The new total, is going to be the original 50 microliter total
# minus the largest amount of DNA sample you have
new_total = d_total - DNA_max
#In order to find out the amount of water you would put in
# you first need to calculate the total of all the reactants
mix_with_no_water = sum(Mix)
# The amount of remaining water to add, will be the new total
# minus the total of the reactants (mix_with_no_water)
d_Water = new_total - mix_with_no_water
# You now add the value of water to your list
Mix.append(d_Water)
# The Master Mix is going to be every value in that list
# of reactants multiplied by the amount of samples your running
Master_Mix = map(lambda x: x*Sample_num,Mix)
# This provides you with all the info you need.
print 'For the Master Mix you are going to add\n',\
Master_Mix[0],'microliters of Taq\n',\
Master_Mix[1],'microliters of Buffer\n',\
Master_Mix[2],'microliters of dntp\'s\n',\
Master_Mix[3],'microliters of Forward Primer\n',\
Master_Mix[4],'microliters of Backwards Primer\n',\
Master_Mix[5],'microliters of Water'

sleep(2)

print 'And each sample is going to get',sum(Master_Mix)/Sample_num,'microliter of the Master Mix'
sleep(2)
print 'Remember to add the remaining microliters of all your other samples using water.'




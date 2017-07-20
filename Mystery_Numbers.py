# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 19:48:47 2017

@author: michael
"""

from time import sleep
from random import randint
from random import choice

print 'Greetings\nWelcome to Numception'
#main list of numbers
MainList = range(1,13)
#player empty list
Player1 = []
Player2 = []

print 'This decides who goes first'
sleep(1)
quater = raw_input('Heads or tails?: ')

flip = randint(1,2)
if flip == 1:
    result = 'heads'
else:
    result = 'tails'
    
if quater[3] in result:
    print 'Nice you get to choose first Player 1!'
else:
    print 'It was ' + result + '. You go second now.'

sleep(2.5)
print 'You\'ve each been given a random 6 numbers from this list'
sleep(2)
print MainList
sleep(1)
print 'Your goal is to utilize four questions\
 to try and figure out what numbers you have,\
 and in what order'
sleep(4)
print 'Player one goes first'

for i in range(6):
    Player1.append(MainList.pop(MainList.index(choice(MainList))))
    Player2.append(MainList.pop(MainList.index(choice(MainList))))

Players = [Player1,Player2]


"""a1,b1 = input('Player 1: What two numbers would you like to know the sum of?: ')
print 'The sum of those numbers is' + (Player1[a1] + Player1[b1])"""

for i in Players:
    a1,b1 = input('Player{}. What would two numbers would you like to know the sum of?: '.format(Players.index(i)+1))
    x = i[a1-1] + i[b1-1]
    print 'The sum of those numbers is',x

for i in Players:
    a1,b1 = input('Player{}. What would two numbers would you like to know the difference of?: '.format(Players.index(i)+1))
    x = i[a1-1] - i[b1-1]
    print 'The difference of those numbers is',x

for i in Players:
    a1,b1 = input('Player{}. What would two numbers would you like to know the product of?: '.format(Players.index(i)+1))
    x = i[a1-1] * i[b1-1]
    print 'The product of those numbers is',x
    
for i in Players:
    a1,b1 = input('Player{}. What would two numbers would you like to know the quotient of?: '.format(Players.index(i)+1))
    a,b = i[a1-1],i[b1-1]
    x = float(a)/float(b)
    print 'The quotient of those numbers is',x
    
    
print 'Okay time to tell me what you think your number list is'
sleep(2)

Player1Ans = [int(i) for i in input('Player1: What are your numbers?: ')]    
Player2Ans = [int(i) for i in input('Player2: What are your numbers?: ')]

Player1Cor = 0
Player2Cor = 0

for i in range(len(Player1)):
    if Player1[i] == Player1Ans[i]:
        Player1Cor += 1
        
for i in range(len(Player2)):
    if Player2[i] == Player2Ans[i]:
        Player2Cor += 1

if Player1Cor == Player2Cor:
    print 'And the winner...',
    sleep(1)
    print 'Oh! It\'s a tie game with a score of %i each!!' % Player1Cor
else:
    Ver = [Player1Cor,Player2Cor]
    Winner = max(Ver)
    if max(Ver) == Ver[0]:
        Champ = 'Player1!'
    else:
        Champ = 'Player2!'
            
    print 'And the winner...',
    sleep(1)
    print 'With a total of %i right!!' % Winner,
    sleep(2)
    print 'Is.......'
    sleep(1)
    print Champ


"""print 'Choose numbers. One by one from this list'   
for i in range(6):
    print MainList
    p1 = input('Player 1: ')
    Player1.append(MainList.pop(MainList.index(p1)))
    print MainList
    p2 = input('Player 2: ')
    Player2.append(MainList.pop(MainList.index(p2)))"""
    
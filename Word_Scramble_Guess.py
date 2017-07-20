# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 14:11:06 2017

@author: michael
"""
import datetime
import os
import sys
from random import shuffle
from random import choice
os.chdir('/usr/share/dict')
File = open('words','r')
Cross = File.read().splitlines()
for i in range(1000):
    x = choice(Cross)
    if len(x) == 7 and x.find("'") == -1 and x.lower() == x:
        word = x
        break
    else:
        continue

    
Final = []
for i in word:
    for j in word:
        for k in word:
            for n in word:
                for l in word:
                    for q in word:
                        for r in word:
                            poss = [i,j,k,n,l,q,r]
                            poss1 = [i,j,k,n,l,q]
                            poss2 = [i,j,k,n,l]
                            poss3 = [i,j,k,n]
                            poss4 = [i,j,k]
                            Final.extend([poss,poss1,poss2,poss3,poss4])

Final = map(lambda i:''.join(i),Final)
Final = set(Final)

Cross = set(Cross)

CorWord = list(Cross.intersection(Final))

for x in range(5):
    for i in range(7):
        for j in CorWord:
            if j.count(word[i]) > word.count(word[i]):
                CorWord.remove(j)

os.chdir('/home/michael/Desktop/Python')
if len(CorWord) > 30 or len(CorWord) < 10:
    execfile('Fail.py')



Guesses = []
Correct = []


time = True
Stop = datetime.datetime.now().minute + 4
Points = 0

while time is True:
    Start = datetime.datetime.now().minute
    word2 = list(word)
    shuffle(word2)
    Letters = ''.join(word2)
    print ('\n')
    print 'Letters: '+ Letters
    print 'Words left- Three:',len(filter(lambda x: len(x) == 3,CorWord)) - len(filter(lambda x: len(x) == 3,Correct))\
    ,'Four:',len(filter(lambda x: len(x) == 4,CorWord)) - len(filter(lambda x: len(x) == 4,Correct))\
    ,'Five:',len(filter(lambda x: len(x) == 5,CorWord)) - len(filter(lambda x: len(x) == 5,Correct))\
    ,'Six:',len(filter(lambda x: len(x) == 6,CorWord)) - len(filter(lambda x: len(x) == 6,Correct))\
    ,'Seven:',len(filter(lambda x: len(x) == 7,CorWord)) - len(filter(lambda x: len(x) == 7,Correct))
    Guess = raw_input('Guess: ')
    if Guess in Guesses or Guess in Correct:
        print ('\n')
        print 'You\'ve already guessed that!'
    elif Guess in CorWord:
        print ('\n')
        if len(Guess) == 3:
            Points += 10
        elif len(Guess) == 4:
            Points += 15
        elif len(Guess) == 5:
            Points += 25
        elif len(Guess) == 6:
            Points += 50
        elif len(Guess) == 7:
            Points += 100
        print 'Got it!',
        print 'Points:',Points
        Correct.append(Guess)
    elif Guess not in CorWord:
        print ('\n')
        print 'Nope!'
        Guesses.append(Guess)
    if len(Correct) == len(CorWord):
        #print 'You win! With a grand total of',Points,'points!!'
        time = False
    if Start >= Stop:
        time = False
else:
    if len(CorWord) != len(Correct):
        print 'TIMES UP!',
        print '\tYour score:',Points
        print 'Here\'s the words you missed:'
        for i in CorWord:
            if i not in Correct:
                print i,
        sys.exit()
    else:
        print 'You win! With a grand total of',Points,'points!!'
        sys.exit()
            
    #sys.exit()
    
        
        
    


            
        


        
    

                            
                                
                           
                           



        

                            
                            
                            
    
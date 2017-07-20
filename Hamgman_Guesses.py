# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 16:20:39 2017

@author: michael
"""

from random import *
from time import sleep

print 'Let\'s play hangman'
sleep(1)
#Generate the User Word
UsrWord = raw_input('Input a word, I promise I won\'t peek: ')
DisWord = UsrWord
ShowWord = ['_']*len(UsrWord)
N = input('And do me a favor, how vowels are there? ')
print 'Okay perfect, let us begin'

#Make lists of letters, in order of most likely
Vowels = ['a','e','i','o','u']
HighlyLikely = ['s','r','t','n','c','l']
MediumLikely = ['b','d','f','g','h','k','m','p']
NotLikely = ['z','x','v','q','w','j','y']

#Keep a list of previously guessed letters and vowels, and the hangman body parts
Guesses = []
VowelRight = []
hangman = []
WordGuess = '_'*len(UsrWord)
hangmanbody = ['Wooden Beam','Noose','Head','Eyes','Nose','Mouth','Ears',\
'Torso','Left Arm','Right Arm','Left Leg','Right Leg']
#hangmanbody = range(28) 

#Set the number of turns
turns = 0

#Randomly choose to pick from whichever list
while turns < 12:
    if UsrWord.count('$') == len(UsrWord):
        print 'The word is',''.join(ShowWord)
        print 'HAHA I win!!'
        break
    else:
        chance = random()
        if chance > 0.2 and len(VowelRight) < N:
            guess = choice(Vowels)
            print 'I\'m guessing the letter',guess
            sleep(1)
            LetterCount = UsrWord.count(guess)
            if LetterCount > 0:
                UsrWord = UsrWord.replace(guess,'$',LetterCount)
                Vowels.remove(guess)
                VowelRight.append(guess)
                index = []
                for letter in range(LetterCount):
                    index.append(DisWord.find(guess))
                    DisWord = DisWord.replace(guess,'$',1)
                    for num in index:
                        ShowWord[num] = guess
                        
                print 'I knew it!'
                sleep(.5)
                print 'My hangman has',hangman
                sleep(.4)
                print 'And so far I have',''.join(ShowWord)
                
            else:
                Guesses.append(guess)
                Vowels.remove(guess)
                hangman.append(hangmanbody[turns])
                turns += 1
                print 'Damn, okay'
                sleep(.5)
                print 'My hangman has',hangman
                sleep(.4)
                print 'And so far I have',''.join(ShowWord)
        
        elif chance > 0 and chance < 0.45 and len(HighlyLikely) > 0:
            guess = choice(HighlyLikely)
            print 'I\'m guessing the letter',guess
            sleep(1)
            LetterCount = UsrWord.count(guess)
            if LetterCount > 0:
                UsrWord = UsrWord.replace(guess,'$',LetterCount)
                HighlyLikely.remove(guess)
                index = []
                for letter in range(LetterCount):
                    index.append(DisWord.find(guess))
                    DisWord = DisWord.replace(guess,'$',1)
                    for num in index:
                        ShowWord[num] = guess
                        
                print 'I got it!'
                sleep(.5)
                print 'My hangman has',hangman
                sleep(.4)
                print 'And so far I have',''.join(ShowWord)
            
            else:
                Guesses.append(guess)
                HighlyLikely.remove(guess)
                hangman.append(hangmanbody[turns])
                turns += 1
                print 'Damn, okay'
                sleep(.5)
                print 'My hangman has',hangman
                sleep(.4)
                print 'And so far I have',''.join(ShowWord)
                
        elif chance > .45 and chance < 0.85 and len(MediumLikely) > 0:
            guess = choice(MediumLikely)
            print 'I\'m guessing the letter',guess
            sleep(1)
            LetterCount = UsrWord.count(guess)
            if LetterCount > 0:
                UsrWord = UsrWord.replace(guess,'$',LetterCount)
                MediumLikely.remove(guess)
                index = []
                for letter in range(LetterCount):
                    index.append(DisWord.find(guess))
                    DisWord = DisWord.replace(guess,'$',1)
                    for num in index:
                        ShowWord[num] = guess
                        
                print 'I got it!'
                sleep(.5)
                print 'My hangman has',hangman
                sleep(.4)
                print 'And so far I have',''.join(ShowWord)
            
            else:
                Guesses.append(guess)
                MediumLikely.remove(guess)
                hangman.append(hangmanbody[turns])
                turns += 1
                print 'Damn, okay'
                sleep(.5)
                print 'My hangman has',hangman
                sleep(.4)
                print 'And so far I have',''.join(ShowWord)
                
        elif chance > .85 and chance < 1 and len(NotLikely) > 0:
            guess = choice(NotLikely)
            print 'I\'m guessing the letter',guess
            sleep(1)
            LetterCount = UsrWord.count(guess)
            if LetterCount > 0:
                UsrWord = UsrWord.replace(guess,'$',LetterCount)
                NotLikely.remove(guess)
                index = []
                for letter in range(LetterCount):
                    index.append(DisWord.find(guess))
                    DisWord = DisWord.replace(guess,'$',1)
                    for num in index:
                        ShowWord[num] = guess
                        
                print 'I got it!'
                sleep(.5)
                print 'My hangman has',hangman
                sleep(.4)
                print 'And so far I have',''.join(ShowWord)
            
            else:
                Guesses.append(guess)
                NotLikely.remove(guess)
                hangman.append(hangmanbody[turns])
                turns += 1
                print 'Damn, okay'
                sleep(.5)
                print 'My hangman has',hangman
                sleep(.4)
                print 'And so far I have',''.join(ShowWord)

else:
    print 'I lose...'
    
    
    
    
        
    


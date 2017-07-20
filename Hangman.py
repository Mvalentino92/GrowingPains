# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 09:10:03 2017

@author: michael
"""
#Making a hangman game
#First I'm importing the file of words, and making it into a list

from random import *
file = open('/home/michael/Downloads/Words_List.txt','r')
Word_List = file.read()
Word_List = Word_List.split('\n')

#randomly selecting a word from the Word_List
word = choice(Word_List)

#Setting a list equal to the empty unguessed letters
List = []
word = word.lower()
wordback = word
for i in word:
    List.append('_ ')
word_guess = ''.join(List) #The length of word_guess is double of the length
print word_guess,len(word_guess)/2                     #of the actual word
#Asking the user for input
#guess = raw_input('What\'s your guess? ')

#How to get the index values of all the occurances of a letter
"""num = word.count('e')
index = []
for i in range(num):
    index.append(word.find('e'))
    word=word.replace('e','$',1)
    
#Change all the index values of the letter in the word_guess
word_guess_list = list(word_guess)
for i in index:
    word_guess_list[i*2] = 'e'
    word_guess = ''.join(word_guess_list)"""
guesses= []
turns = 0
hangman = []
hangmanbody = ['Wooden Beam','Noose','Head','Body','Right Arm','Left Arm','Right Leg','Left Leg']
while turns <= 7:
    if turns == 7 or word == len(word)*word[0]:
        print 'Just the Left Leg left!'
        solve = raw_input('So what do you think it is? ')
        if solve == wordback:
            print 'You win!'
            break
        else:
            print 'Sorry you lose!'
            print 'The word was', wordback
            break
    else:
        guess = raw_input('So what\'s your guess? ')
        guesses.append(guess)
        for letter in guess:
            num = word.count(letter)
            index = []
            if num > 0:
                for number in range(num):
                    index.append(word.find(letter))
                    word = word.replace(letter,'$',1)
                    word_guess_list = list(word_guess)
                    for numdex in index:
                        word_guess_list[numdex*2] = letter
                        word_guess = ''.join(word_guess_list)
            else:
                hangman.append(hangmanbody[turns])    
                turns += 1
        print word_guess
        print 'Your hangman has...',hangman
        print 'Your previous guesses are', guesses
        print 'You have',7 - len(hangman),'wrong guesses left' 


    
    
"""for letter in guess:
    num = word.count(letter)
    index = []
    if num > 0:
        for number in range(num):
            index.append(word.find(letter))
            word = word.replace(letter,'$',1)
        word_guess_list = list(word_guess)
        for numdex in index:
            word_guess_list[numdex*2] = letter
            word_guess = ''.join(word_guess_list)"""

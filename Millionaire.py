# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 18:36:39 2017

@author: michael
"""
from Tkinter import *
import os
os.chdir('/home/michael/Sounds')
from time import sleep
import pygame
import tkMessageBox as tkm
class Myclass:
    def submit(self,event):
        key = [4,2,4,1,4,2,1,3,2,1,3,4,1]
        for i in key:
            yield i
    def __init__(self,master):
        self.frame = Frame(master,bg='white')
        self.frame.grid(row=0,columnspan=4)
        self.Question = Label(self.frame,text='What are the three Primary Colors?'\
        ,bg = 'white')
        self.Question.grid(row=0,sticky = W)
        #Make all of the question label
        self.AnsA = Label(master,text='Yellow,Blue,Green',bg='white')
        self.AnsA.grid(row=1,column = 1,sticky = W)
        self.AnsB = Label(master,text='Yellow,Green,Red',bg='white')
        self.AnsB.grid(row=1,column  =3,sticky = W)
        self.AnsC = Label(master,text='Blue,White,Red',bg='white')
        self.AnsC.grid(row=2,column =1,sticky = W)
        self.AnsD = Label(master,text = 'Red,Yellow,Blue',bg='white')
        self.AnsD.grid(row=2,column =3,sticky = W)
        #set all the variables
        self.var = IntVar(master,1)
        self.var = IntVar(master,2)
        self.var = IntVar(master,3)
        self.var = IntVar(master,4)
        #Make all the checkbuttons
        self.A = Checkbutton(master,text='A:',variable = self.var,onvalue = 1,\
        bg = 'white')
        self.B = Checkbutton(master,text='B:',variable = self.var,onvalue = 2,\
        bg ='white')
        self.C = Checkbutton(master,text='C:',variable = self.var,onvalue = 3,\
        bg ='white')
        self.D = Checkbutton(master,text='D:',variable = self.var,onvalue = 4,\
        bg='white')
        self.A.grid(row=1,column= 0)
        self.B.grid(row=1,column =2)
        self.C.grid(row=2,column =0)
        self.D.grid(row=2,column =2)
        self.Final = Button(master,text='Is that your\n final answer?',bg='ivory2')
        self.Final.grid(row=3,column = 1)
        self.Final.bind('<Button-1>',self.final)
        self.total = 0
        self.key = [4,2,4,1,4,2,1,3,2,1,3,4,1]
        self.change = self.submit(self.key)
        
        
    def final(self,event):
        Questions = ['Complete this famous nursery rhyme: Ring around\n the\
 rosie, pocket full of \'blank\'?','The average human temperature is \'blank\'?',\
 'What state is home to the Great Lakes?','On what scale are earthquakes\
 measured by?','Earth is the \'blank\' planet away from the sun','What\
 famous cartoon cat is\n known for loving lasagna?','Genghis Khan was the leader of\
 the \'blank\' empire?','In the sport of NASCAR, the team of people who\n are\
 responsible for servicing the teams cars at\n checkpoints are known as what?'\
 ,'The Organization known as PETA stands for \'blank\'?','Which of the following\
 animals is NOT killed for harvesting it\'s ivory?','Which former US president\
 is featured on the dime?','For one million dollars...\n What is the name of the\
 programming language known as \'Python\' a reference to?']
 
        Aanswers = ['Tulips','96.8','Michigan','Nueremburg Scale','Fourth',\
        'Garfield','Chinese','Racer Repairers','People for the Ethical Treatment\
 of Animals','Narwhal','Abraham Lincoln','The show Montey Python']
        Banswers = ['Posies','97.4','Idaho','Hoss 9','Third','Felix','Mesopotamian'\
        ,'Pit Crew','Prosperity of Everlasting Tolerance in America','Elephant'\
        ,'Ulysses S. Grant','The size of the Python Animal']
        Canswers = ['Cosies','100','Utah','Mievitz Scale','First','Alfonso','Mongol'\
        ,'Service Squad','People for Economies Triumph in America','Gazelle'\
        ,'Theodore Roosevelt','The nickname of it\'s creator']
        Danswers = ['Lint','98.6','Pennsylvania','Richter Scale','Fifth',\
        'Whiskers','Korean','Clean-Up Crew','Peace in Every Targeted Area','Hippopotamus'\
        ,'Franklin Delano Roosevelt','An old printing company spelled \'PieThon\'']
        titleroot = ['Question 2: For 1,000 Dollars','Question 3: For 2,500 Dollars'\
        ,'Question 4: For 5,000 Dollars','Question 5: For 10,000 Dollars',\
        'Question 6: For 25,000 Dollars','Question 7: For 50,000','Question 8:\
 For 100,000 Dollars','Question 9: For 150,000 Dollars','Question 10: For 300,000 Dollars',\
 'Question 11: For 500,000 Dollars','Question 12: For 750,000 Dollars',\
 'Question 13: For 1,000,000 Dollars']
        sub = self.change
        ans = next(sub)
        if self.total == 12 and ans == self.var.get():
            pygame.init()
            pygame.mixer.music.load('DrumRoll.wav')
            pygame.mixer.music.play()
            sleep(4.85)
            pygame.mixer.music.load('winner.wav')
            pygame.mixer.music.play()
            tkm.showinfo('Congratulations!!.','YOU ARE\n A MILLIONAIRE!!')
            root.destroy()
        elif ans == self.var.get():
            pygame.init()
            pygame.mixer.music.load('Millionare.wav')
            pygame.mixer.music.play()
            sleep(5.65)
            pygame.mixer.music.load('correct.wav')
            pygame.mixer.music.play()
            tkm.showinfo('You are..','CORRECT!!')
            self.Question['text'] = Questions[self.total]
            self.AnsA['text'] = Aanswers[self.total]
            self.AnsB['text'] = Banswers[self.total]
            self.AnsC['text'] = Canswers[self.total]
            self.AnsD['text'] = Danswers[self.total]
            root.title(titleroot[self.total])
            self.total += 1
        else:
            pygame.init()
            pygame.mixer.music.load('Millionare.wav')
            pygame.mixer.music.play()
            sleep(5.65)
            pygame.mixer.music.load('dundun.wav')
            pygame.mixer.music.play()
            tkm.showinfo('I\'m sorry', 'You lose!\nTry again next time!')
            root.destroy()
            
            
root = Tk()
root.title('Question 1: For 500 Dollars')
root.configure(bg='white')
#root.geometry('400x200')
myclass = Myclass(root)
root.mainloop()
        
        
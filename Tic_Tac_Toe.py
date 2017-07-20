# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 10:44:48 14017

@author: michael
"""
from Tkinter import *
import tkMessageBox as tkm
import tkFont as tkf
from random import choice
from time import sleep
from numpy import *
class TicTacToe:
    
    
    def __init__(self,master):
        #Make all the Blank Buttons, which will function as the grid boxes
        self.OneB = Button(master,text='    ',font=('w',140))
        #self.OneB.config(height = 10,width=140)
        self.OneB.grid(row=0,column=0)
        #We need to bind the left and right click to two seperate funtions
        self.OneB.bind('<Button-1>',self.X1)
        self.OneB.bind('<Button-3>',self.O1)
        
        self.TwoB = Button(master,text='    ',font=('w',140))
        #self.TwoB.config(height = 10,width=140)
        self.TwoB.grid(row=0,column=1)
        #We need to bind the left and right click to two seperate funtions
        self.TwoB.bind('<Button-1>',self.X2)
        self.TwoB.bind('<Button-3>',self.O2)
         
        self.ThreeB = Button(master,text='    ',font=('w',140))
        #self.ThreeB.config(height = 10, width = 140)
        self.ThreeB.grid(row = 0,column =2)
        #We need to bind the left and right click to two seperate funtions
        self.ThreeB.bind('<Button-1>',self.X3)
        self.ThreeB.bind('<Button-3>',self.O3)
        
        
        self.FourB = Button(master,text='    ',font=('w',140))
        #self.FourB.config(height = 10,width=140)
        self.FourB.grid(row=1,column=0)
        #We need to bind the left and right click to two seperate funtions
        self.FourB.bind('<Button-1>',self.X4)
        self.FourB.bind('<Button-3>',self.O4)
        
        
        self.FiveB = Button(master,text='    ',font=('w',140))
       # self.FiveB.config(height = 10,width=140)
        self.FiveB.grid(row=1,column=1)
        #We need to bind the left and right click to two seperate funtions
        self.FiveB.bind('<Button-1>',self.X5)
        self.FiveB.bind('<Button-3>',self.O5)
        
        
        self.SixB = Button(master,text='    ',font=('w',140))
        #self.SixB.config(height = 10,width=140)
        self.SixB.grid(row=1,column=2)
        #We need to bind the left and right click to two seperate funtions
        self.SixB.bind('<Button-1>',self.X6)
        self.SixB.bind('<Button-3>',self.O6)
        
        
        self.SevenB = Button(master,text='    ',font=('w',140))
        #self.SevenB.config(height = 10,width=140)
        self.SevenB.grid(row=2,column=0)
        #We need to bind the left and right click to two seperate funtions
        self.SevenB.bind('<Button-1>',self.X7)
        self.SevenB.bind('<Button-3>',self.O7)
        
        
        self.EightB = Button(master,text='    ',font=('w',140))
        #self.EightB.config(height = 10,width=140)
        self.EightB.grid(row=2,column=1)
        #We need to bind the left and right click to two seperate funtions
        self.EightB.bind('<Button-1>',self.X8)
        self.EightB.bind('<Button-3>',self.O8)
        
        
        self.NineB = Button(master,text='    ',font=('w',140))
        #self.NineB.config(height = 10,width=140)
        self.NineB.grid(row=2,column=2)
        #We need to bind the left and right click to two seperate funtions
        self.NineB.bind('<Button-1>',self.X9)
        self.NineB.bind('<Button-3>',self.O9)
        
        #Create the matrix of zero's which will correspond to the board
        
        self.board = zeros([3,3])
        self.color = ['blue','red','brown','green','pink','violet','yellow','cyan','sienna1'\
        ,'SeaGreen1']
        #Create the functions for each button, right and left click
    def colorchange(self):
        self.OneB['bg'] = choice(self.color)
        self.TwoB['bg'] = choice(self.color)
        self.ThreeB['bg'] = choice(self.color)
        self.FourB['bg'] = choice(self.color)
        self.FiveB['bg'] = choice(self.color)
        self.SixB['bg'] = choice(self.color)
        self.SevenB['bg'] = choice(self.color)
        self.EightB['bg'] = choice(self.color)
        self.NineB['bg'] = choice(self.color)
        
        
        
    def X1(self,event):
        self.board[0,0] = 1
        self.OneB['text'] = ' x '
        if sum(self.board[0,:]) == 3 or sum(self.board[1,:]) == 3\
        or sum(self.board[2,:]) == 3 or sum(self.board[:,0]) == 3\
        or sum(self.board[:,1]) == 3 or sum(self.board[:,2]) == 3\
        or self.board[0,0] + self.board[1,1] + self.board [2,2] == 3\
        or self.board[0,2] + self.board[1,1] + self.board[2,0] == 3:
            self.OneB.after(250,self.colorchange)
            self.OneB.after(500,self.colorchange)
            self.OneB.after(750,self.colorchange)
            self.OneB.after(1000,self.colorchange)
            self.OneB.after(1250,self.colorchange)
            self.OneB.after(1500,self.colorchange)
            self.OneB.after(1750,self.colorchange)
            self.OneB.after(2000,self.colorchange)            
            self.OneB.after(2250,self.colorchange)    
            self.OneB.after(2500,self.colorchange)    
            self.OneB.after(2750,self.colorchange)
            self.OneB.after(3000,self.colorchange)
            self.OneB.after(3250,self.colorchange)
            self.OneB.after(3500,self.colorchange)
            self.OneB.after(3750,self.colorchange)
            self.OneB.after(4000,self.colorchange)
            tkm.showinfo('Congratz!','You win!!!')
    
    def O1(self,event):
        self.board[0,0] = 5
        self.OneB['text'] = ' o '
        if sum(self.board[0,:]) == 15 or sum(self.board[1,:]) == 15\
        or sum(self.board[2,:]) == 15 or sum(self.board[:,0]) == 15\
        or sum(self.board[:,1]) == 15 or sum(self.board[:,2]) == 15\
        or self.board[0,0] + self.board[1,1] + self.board [2,2] == 15\
        or self.board[0,2] + self.board[1,1] + self.board[2,0] == 15:
            self.OneB.after(250,self.colorchange)
            self.OneB.after(500,self.colorchange)
            self.OneB.after(750,self.colorchange)
            self.OneB.after(1000,self.colorchange)
            self.OneB.after(1250,self.colorchange)
            self.OneB.after(1500,self.colorchange)
            self.OneB.after(1750,self.colorchange)
            self.OneB.after(2000,self.colorchange)            
            self.OneB.after(2250,self.colorchange)    
            self.OneB.after(2500,self.colorchange)    
            self.OneB.after(2750,self.colorchange)
            self.OneB.after(3000,self.colorchange)
            self.OneB.after(3250,self.colorchange)
            self.OneB.after(3500,self.colorchange)
            self.OneB.after(3750,self.colorchange)
            self.OneB.after(4000,self.colorchange)
            tkm.showinfo('Congratz!','You win!!!')
            
    def X2(self,event):
        self.board[0,1] = 1
        self.TwoB['text'] = ' x '
        if sum(self.board[0,:]) == 3 or sum(self.board[1,:]) == 3\
        or sum(self.board[2,:]) == 3 or sum(self.board[:,0]) == 3\
        or sum(self.board[:,1]) == 3 or sum(self.board[:,2]) == 3\
        or self.board[0,0] + self.board[1,1] + self.board [2,2] == 3\
        or self.board[0,2] + self.board[1,1] + self.board[2,0] == 3:
            self.OneB.after(250,self.colorchange)
            self.OneB.after(500,self.colorchange)
            self.OneB.after(750,self.colorchange)
            self.OneB.after(1000,self.colorchange)
            self.OneB.after(1250,self.colorchange)
            self.OneB.after(1500,self.colorchange)
            self.OneB.after(1750,self.colorchange)
            self.OneB.after(2000,self.colorchange)            
            self.OneB.after(2250,self.colorchange)    
            self.OneB.after(2500,self.colorchange)    
            self.OneB.after(2750,self.colorchange)
            self.OneB.after(3000,self.colorchange)
            self.OneB.after(3250,self.colorchange)
            self.OneB.after(3500,self.colorchange)
            self.OneB.after(3750,self.colorchange)
            self.OneB.after(4000,self.colorchange)
            tkm.showinfo('Congratz!','You win!!!')
            
    def O2(self,event):
        self.board[0,1] = 5
        self.TwoB['text'] = ' o '
        if sum(self.board[0,:]) == 15 or sum(self.board[1,:]) == 15\
        or sum(self.board[2,:]) == 15 or sum(self.board[:,0]) == 15\
        or sum(self.board[:,1]) == 15 or sum(self.board[:,2]) == 15\
        or self.board[0,0] + self.board[1,1] + self.board [2,2] == 15\
        or self.board[0,2] + self.board[1,1] + self.board[2,0] == 15:
            self.OneB.after(250,self.colorchange)
            self.OneB.after(500,self.colorchange)
            self.OneB.after(750,self.colorchange)
            self.OneB.after(1000,self.colorchange)
            self.OneB.after(1250,self.colorchange)
            self.OneB.after(1500,self.colorchange)
            self.OneB.after(1750,self.colorchange)
            self.OneB.after(2000,self.colorchange)            
            self.OneB.after(2250,self.colorchange)    
            self.OneB.after(2500,self.colorchange)    
            self.OneB.after(2750,self.colorchange)
            self.OneB.after(3000,self.colorchange)
            self.OneB.after(3250,self.colorchange)
            self.OneB.after(3500,self.colorchange)
            self.OneB.after(3750,self.colorchange)
            self.OneB.after(4000,self.colorchange)
            tkm.showinfo('Congratz!','You win!!!')
            
    def X3(self,event):
        self.board[0,2] = 1
        self.ThreeB['text'] = ' x '
        if sum(self.board[0,:]) == 3 or sum(self.board[1,:]) == 3\
        or sum(self.board[2,:]) == 3 or sum(self.board[:,0]) == 3\
        or sum(self.board[:,1]) == 3 or sum(self.board[:,2]) == 3\
        or self.board[0,0] + self.board[1,1] + self.board [2,2] == 3\
        or self.board[0,2] + self.board[1,1] + self.board[2,0] == 3:
            self.OneB.after(250,self.colorchange)
            self.OneB.after(500,self.colorchange)
            self.OneB.after(750,self.colorchange)
            self.OneB.after(1000,self.colorchange)
            self.OneB.after(1250,self.colorchange)
            self.OneB.after(1500,self.colorchange)
            self.OneB.after(1750,self.colorchange)
            self.OneB.after(2000,self.colorchange)            
            self.OneB.after(2250,self.colorchange)    
            self.OneB.after(2500,self.colorchange)    
            self.OneB.after(2750,self.colorchange)
            self.OneB.after(3000,self.colorchange)
            self.OneB.after(3250,self.colorchange)
            self.OneB.after(3500,self.colorchange)
            self.OneB.after(3750,self.colorchange)
            self.OneB.after(4000,self.colorchange)
            tkm.showinfo('Congratz!','You win!!!')
            
    def O3(self,event):
        self.board[0,2] = 5
        self.ThreeB['text'] = ' o '
        if sum(self.board[0,:]) == 15 or sum(self.board[1,:]) == 15\
        or sum(self.board[2,:]) == 15 or sum(self.board[:,0]) == 15\
        or sum(self.board[:,1]) == 15 or sum(self.board[:,2]) == 15\
        or self.board[0,0] + self.board[1,1] + self.board [2,2] == 15\
        or self.board[0,2] + self.board[1,1] + self.board[2,0] == 15:
            self.OneB.after(250,self.colorchange)
            self.OneB.after(500,self.colorchange)
            self.OneB.after(750,self.colorchange)
            self.OneB.after(1000,self.colorchange)
            self.OneB.after(1250,self.colorchange)
            self.OneB.after(1500,self.colorchange)
            self.OneB.after(1750,self.colorchange)
            self.OneB.after(2000,self.colorchange)            
            self.OneB.after(2250,self.colorchange)    
            self.OneB.after(2500,self.colorchange)    
            self.OneB.after(2750,self.colorchange)
            self.OneB.after(3000,self.colorchange)
            self.OneB.after(3250,self.colorchange)
            self.OneB.after(3500,self.colorchange)
            self.OneB.after(3750,self.colorchange)
            self.OneB.after(4000,self.colorchange)
            tkm.showinfo('Congratz!','You win!!!')
            
    def X4(self,event):
        self.board[1,0] = 1
        self.FourB['text'] = ' x '
        if sum(self.board[0,:]) == 3 or sum(self.board[1,:]) == 3\
        or sum(self.board[2,:]) == 3 or sum(self.board[:,0]) == 3\
        or sum(self.board[:,1]) == 3 or sum(self.board[:,2]) == 3\
        or self.board[0,0] + self.board[1,1] + self.board [2,2] == 3\
        or self.board[0,2] + self.board[1,1] + self.board[2,0] == 3:
            self.OneB.after(250,self.colorchange)
            self.OneB.after(500,self.colorchange)
            self.OneB.after(750,self.colorchange)
            self.OneB.after(1000,self.colorchange)
            self.OneB.after(1250,self.colorchange)
            self.OneB.after(1500,self.colorchange)
            self.OneB.after(1750,self.colorchange)
            self.OneB.after(2000,self.colorchange)            
            self.OneB.after(2250,self.colorchange)    
            self.OneB.after(2500,self.colorchange)    
            self.OneB.after(2750,self.colorchange)
            self.OneB.after(3000,self.colorchange)
            self.OneB.after(3250,self.colorchange)
            self.OneB.after(3500,self.colorchange)
            self.OneB.after(3750,self.colorchange)
            self.OneB.after(4000,self.colorchange)
            tkm.showinfo('Congratz!','You win!!!')
            
    def O4(self,event):
        self.board[1,0] = 5
        self.FourB['text'] = ' o '
        if sum(self.board[0,:]) == 15 or sum(self.board[1,:]) == 15\
        or sum(self.board[2,:]) == 15 or sum(self.board[:,0]) == 15\
        or sum(self.board[:,1]) == 15 or sum(self.board[:,2]) == 15\
        or self.board[0,0] + self.board[1,1] + self.board [2,2] == 15\
        or self.board[0,2] + self.board[1,1] + self.board[2,0] == 15:
            self.OneB.after(250,self.colorchange)
            self.OneB.after(500,self.colorchange)
            self.OneB.after(750,self.colorchange)
            self.OneB.after(1000,self.colorchange)
            self.OneB.after(1250,self.colorchange)
            self.OneB.after(1500,self.colorchange)
            self.OneB.after(1750,self.colorchange)
            self.OneB.after(2000,self.colorchange)            
            self.OneB.after(2250,self.colorchange)    
            self.OneB.after(2500,self.colorchange)    
            self.OneB.after(2750,self.colorchange)
            self.OneB.after(3000,self.colorchange)
            self.OneB.after(3250,self.colorchange)
            self.OneB.after(3500,self.colorchange)
            self.OneB.after(3750,self.colorchange)
            self.OneB.after(4000,self.colorchange)
            tkm.showinfo('Congratz!','You win!!!')
            
    def X5(self,event):
        self.board[1,1] = 1
        self.FiveB['text'] = ' x '
        if sum(self.board[0,:]) == 3 or sum(self.board[1,:]) == 3\
        or sum(self.board[2,:]) == 3 or sum(self.board[:,0]) == 3\
        or sum(self.board[:,1]) == 3 or sum(self.board[:,2]) == 3\
        or self.board[0,0] + self.board[1,1] + self.board [2,2] == 3\
        or self.board[0,2] + self.board[1,1] + self.board[2,0] == 3:
            self.OneB.after(250,self.colorchange)
            self.OneB.after(500,self.colorchange)
            self.OneB.after(750,self.colorchange)
            self.OneB.after(1000,self.colorchange)
            self.OneB.after(1250,self.colorchange)
            self.OneB.after(1500,self.colorchange)
            self.OneB.after(1750,self.colorchange)
            self.OneB.after(2000,self.colorchange)            
            self.OneB.after(2250,self.colorchange)    
            self.OneB.after(2500,self.colorchange)    
            self.OneB.after(2750,self.colorchange)
            self.OneB.after(3000,self.colorchange)
            self.OneB.after(3250,self.colorchange)
            self.OneB.after(3500,self.colorchange)
            self.OneB.after(3750,self.colorchange)
            self.OneB.after(4000,self.colorchange)
            tkm.showinfo('Congratz!','You win!!!')
            
    def O5(self,event):
        self.board[1,1] = 5
        self.FiveB['text'] = ' o '
        if sum(self.board[0,:]) == 15 or sum(self.board[1,:]) == 15\
        or sum(self.board[2,:]) == 15 or sum(self.board[:,0]) == 15\
        or sum(self.board[:,1]) == 15 or sum(self.board[:,2]) == 15\
        or self.board[0,0] + self.board[1,1] + self.board [2,2] == 15\
        or self.board[0,2] + self.board[1,1] + self.board[2,0] == 15:
            self.OneB.after(250,self.colorchange)
            self.OneB.after(500,self.colorchange)
            self.OneB.after(750,self.colorchange)
            self.OneB.after(1000,self.colorchange)
            self.OneB.after(1250,self.colorchange)
            self.OneB.after(1500,self.colorchange)
            self.OneB.after(1750,self.colorchange)
            self.OneB.after(2000,self.colorchange)            
            self.OneB.after(2250,self.colorchange)    
            self.OneB.after(2500,self.colorchange)    
            self.OneB.after(2750,self.colorchange)
            self.OneB.after(3000,self.colorchange)
            self.OneB.after(3250,self.colorchange)
            self.OneB.after(3500,self.colorchange)
            self.OneB.after(3750,self.colorchange)
            self.OneB.after(4000,self.colorchange)
            tkm.showinfo('Congratz!','You win!!!')
            
    def X6(self,event):
        self.board[1,2] = 1
        self.SixB['text'] = ' x '
        if sum(self.board[0,:]) == 3 or sum(self.board[1,:]) == 3\
        or sum(self.board[2,:]) == 3 or sum(self.board[:,0]) == 3\
        or sum(self.board[:,1]) == 3 or sum(self.board[:,2]) == 3\
        or self.board[0,0] + self.board[1,1] + self.board [2,2] == 3\
        or self.board[0,2] + self.board[1,1] + self.board[2,0] == 3:
            self.OneB.after(250,self.colorchange)
            self.OneB.after(500,self.colorchange)
            self.OneB.after(750,self.colorchange)
            self.OneB.after(1000,self.colorchange)
            self.OneB.after(1250,self.colorchange)
            self.OneB.after(1500,self.colorchange)
            self.OneB.after(1750,self.colorchange)
            self.OneB.after(2000,self.colorchange)            
            self.OneB.after(2250,self.colorchange)    
            self.OneB.after(2500,self.colorchange)    
            self.OneB.after(2750,self.colorchange)
            self.OneB.after(3000,self.colorchange)
            self.OneB.after(3250,self.colorchange)
            self.OneB.after(3500,self.colorchange)
            self.OneB.after(3750,self.colorchange)
            self.OneB.after(4000,self.colorchange)
            tkm.showinfo('Congratz!','You win!!!')
            
    def O6(self,event):
        self.board[1,2] = 5
        self.SixB['text'] = ' o '
        if sum(self.board[0,:]) == 15 or sum(self.board[1,:]) == 15\
        or sum(self.board[2,:]) == 15 or sum(self.board[:,0]) == 15\
        or sum(self.board[:,1]) == 15 or sum(self.board[:,2]) == 15\
        or self.board[0,0] + self.board[1,1] + self.board [2,2] == 15\
        or self.board[0,2] + self.board[1,1] + self.board[2,0] == 15:
            self.OneB.after(250,self.colorchange)
            self.OneB.after(500,self.colorchange)
            self.OneB.after(750,self.colorchange)
            self.OneB.after(1000,self.colorchange)
            self.OneB.after(1250,self.colorchange)
            self.OneB.after(1500,self.colorchange)
            self.OneB.after(1750,self.colorchange)
            self.OneB.after(2000,self.colorchange)            
            self.OneB.after(2250,self.colorchange)    
            self.OneB.after(2500,self.colorchange)    
            self.OneB.after(2750,self.colorchange)
            self.OneB.after(3000,self.colorchange)
            self.OneB.after(3250,self.colorchange)
            self.OneB.after(3500,self.colorchange)
            self.OneB.after(3750,self.colorchange)
            self.OneB.after(4000,self.colorchange)
            tkm.showinfo('Congratz!','You win!!!')
            
    def X7(self,event):
        self.board[2,0] = 1
        self.SevenB['text'] = ' x '
        if sum(self.board[0,:]) == 3 or sum(self.board[1,:]) == 3\
        or sum(self.board[2,:]) == 3 or sum(self.board[:,0]) == 3\
        or sum(self.board[:,1]) == 3 or sum(self.board[:,2]) == 3\
        or self.board[0,0] + self.board[1,1] + self.board [2,2] == 3\
        or self.board[0,2] + self.board[1,1] + self.board[2,0] == 3:
            self.OneB.after(250,self.colorchange)
            self.OneB.after(500,self.colorchange)
            self.OneB.after(750,self.colorchange)
            self.OneB.after(1000,self.colorchange)
            self.OneB.after(1250,self.colorchange)
            self.OneB.after(1500,self.colorchange)
            self.OneB.after(1750,self.colorchange)
            self.OneB.after(2000,self.colorchange)            
            self.OneB.after(2250,self.colorchange)    
            self.OneB.after(2500,self.colorchange)    
            self.OneB.after(2750,self.colorchange)
            self.OneB.after(3000,self.colorchange)
            self.OneB.after(3250,self.colorchange)
            self.OneB.after(3500,self.colorchange)
            self.OneB.after(3750,self.colorchange)
            self.OneB.after(4000,self.colorchange)
            tkm.showinfo('Congratz!','You win!!!')
            
    def O7(self,event):
        self.board[2,0] = 5
        self.SevenB['text'] = ' o '
        if sum(self.board[0,:]) == 15 or sum(self.board[1,:]) == 15\
        or sum(self.board[2,:]) == 15 or sum(self.board[:,0]) == 15\
        or sum(self.board[:,1]) == 15 or sum(self.board[:,2]) == 15\
        or self.board[0,0] + self.board[1,1] + self.board [2,2] == 15\
        or self.board[0,2] + self.board[1,1] + self.board[2,0] == 15:
            self.OneB.after(250,self.colorchange)
            self.OneB.after(500,self.colorchange)
            self.OneB.after(750,self.colorchange)
            self.OneB.after(1000,self.colorchange)
            self.OneB.after(1250,self.colorchange)
            self.OneB.after(1500,self.colorchange)
            self.OneB.after(1750,self.colorchange)
            self.OneB.after(2000,self.colorchange)            
            self.OneB.after(2250,self.colorchange)    
            self.OneB.after(2500,self.colorchange)    
            self.OneB.after(2750,self.colorchange)
            self.OneB.after(3000,self.colorchange)
            self.OneB.after(3250,self.colorchange)
            self.OneB.after(3500,self.colorchange)
            self.OneB.after(3750,self.colorchange)
            self.OneB.after(4000,self.colorchange)
            tkm.showinfo('Congratz!','You win!!!')
            
    def X8(self,event):
        self.board[2,1] = 1
        self.EightB['text'] = ' x '
        if sum(self.board[0,:]) == 3 or sum(self.board[1,:]) == 3\
        or sum(self.board[2,:]) == 3 or sum(self.board[:,0]) == 3\
        or sum(self.board[:,1]) == 3 or sum(self.board[:,2]) == 3\
        or self.board[0,0] + self.board[1,1] + self.board [2,2] == 3\
        or self.board[0,2] + self.board[1,1] + self.board[2,0] == 3:
            self.OneB.after(250,self.colorchange)
            self.OneB.after(500,self.colorchange)
            self.OneB.after(750,self.colorchange)
            self.OneB.after(1000,self.colorchange)
            self.OneB.after(1250,self.colorchange)
            self.OneB.after(1500,self.colorchange)
            self.OneB.after(1750,self.colorchange)
            self.OneB.after(2000,self.colorchange)            
            self.OneB.after(2250,self.colorchange)    
            self.OneB.after(2500,self.colorchange)    
            self.OneB.after(2750,self.colorchange)
            self.OneB.after(3000,self.colorchange)
            self.OneB.after(3250,self.colorchange)
            self.OneB.after(3500,self.colorchange)
            self.OneB.after(3750,self.colorchange)
            self.OneB.after(4000,self.colorchange)
            tkm.showinfo('Congratz!','You win!!!')
            
            
    def O8(self,event):
        self.board[2,1] = 5
        self.EightB['text'] = ' o '
        if sum(self.board[0,:]) == 15 or sum(self.board[1,:]) == 15\
        or sum(self.board[2,:]) == 15 or sum(self.board[:,0]) == 15\
        or sum(self.board[:,1]) == 15 or sum(self.board[:,2]) == 15\
        or self.board[0,0] + self.board[1,1] + self.board [2,2] == 15\
        or self.board[0,2] + self.board[1,1] + self.board[2,0] == 15:
            self.OneB.after(250,self.colorchange)
            self.OneB.after(500,self.colorchange)
            self.OneB.after(750,self.colorchange)
            self.OneB.after(1000,self.colorchange)
            self.OneB.after(1250,self.colorchange)
            self.OneB.after(1500,self.colorchange)
            self.OneB.after(1750,self.colorchange)
            self.OneB.after(2000,self.colorchange)            
            self.OneB.after(2250,self.colorchange)    
            self.OneB.after(2500,self.colorchange)    
            self.OneB.after(2750,self.colorchange)
            self.OneB.after(3000,self.colorchange)
            self.OneB.after(3250,self.colorchange)
            self.OneB.after(3500,self.colorchange)
            self.OneB.after(3750,self.colorchange)
            self.OneB.after(4000,self.colorchange)
            tkm.showinfo('Congratz!','You win!!!')
            
    def X9(self,event):
        self.board[2,2] = 1
        self.NineB['text'] = ' x '
        if sum(self.board[0,:]) == 3 or sum(self.board[1,:]) == 3\
        or sum(self.board[2,:]) == 3 or sum(self.board[:,0]) == 3\
        or sum(self.board[:,1]) == 3 or sum(self.board[:,2]) == 3\
        or self.board[0,0] + self.board[1,1] + self.board [2,2] == 3\
        or self.board[0,2] + self.board[1,1] + self.board[2,0] == 3:
            self.OneB.after(250,self.colorchange)
            self.OneB.after(500,self.colorchange)
            self.OneB.after(750,self.colorchange)
            self.OneB.after(1000,self.colorchange)
            self.OneB.after(1250,self.colorchange)
            self.OneB.after(1500,self.colorchange)
            self.OneB.after(1750,self.colorchange)
            self.OneB.after(2000,self.colorchange)            
            self.OneB.after(2250,self.colorchange)    
            self.OneB.after(2500,self.colorchange)    
            self.OneB.after(2750,self.colorchange)
            self.OneB.after(3000,self.colorchange)
            self.OneB.after(3250,self.colorchange)
            self.OneB.after(3500,self.colorchange)
            self.OneB.after(3750,self.colorchange)
            self.OneB.after(4000,self.colorchange)
            tkm.showinfo('Congratz!','You win!!!')
            
    def O9(self,event):
        self.board[2,2] = 5
        self.NineB['text'] = ' o '
        if sum(self.board[0,:]) == 15 or sum(self.board[1,:]) == 15\
        or sum(self.board[2,:]) == 15 or sum(self.board[:,0]) == 15\
        or sum(self.board[:,1]) == 15 or sum(self.board[:,2]) == 15\
        or self.board[0,0] + self.board[1,1] + self.board [2,2] == 15\
        or self.board[0,2] + self.board[1,1] + self.board[2,0] == 15:
            self.OneB.after(250,self.colorchange)
            self.OneB.after(500,self.colorchange)
            self.OneB.after(750,self.colorchange)
            self.OneB.after(1000,self.colorchange)
            self.OneB.after(1250,self.colorchange)
            self.OneB.after(1500,self.colorchange)
            self.OneB.after(1750,self.colorchange)
            self.OneB.after(2000,self.colorchange)            
            self.OneB.after(2250,self.colorchange)    
            self.OneB.after(2500,self.colorchange)    
            self.OneB.after(2750,self.colorchange)
            self.OneB.after(3000,self.colorchange)
            self.OneB.after(3250,self.colorchange)
            self.OneB.after(3500,self.colorchange)
            self.OneB.after(3750,self.colorchange)
            self.OneB.after(4000,self.colorchange)
            tkm.showinfo('Congratz!','You win!!!')
            
            
        
        
        
        
      
      
      
      
      
      
      
root = Tk()
root.title('Tic Tac Toe!!')
tictactoe = TicTacToe(root)
root.mainloop()         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

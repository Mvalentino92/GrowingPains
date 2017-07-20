# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 17:17:32 2017

@author: michael
"""
from __future__ import division
from Tkinter import *
Level1 = Tk()

class Arithmatic:
    
    def __init__(self,level1):
        self.Frame1 = Frame(level1)
        self.Frame1.grid(row=0)
        self.Frame2 = Frame(level1)
        self.Frame2.grid(row=1)
        self.Frame3 = Frame(level1)
        self.Frame3.grid(row=2)
        self.Frame4 = Frame(level1)
        self.Frame4.grid(row=3)
        #Design the Labels
        self.Oldnum = Label(self.Frame1,font=('w',16))
        self.Oldnum.grid(row=0,column=0)
        self.Arrow = Label(self.Frame1,text='------>',font=('w',16))
        self.Arrow.grid(row=0,column=1)
        self.Newnum = Label(self.Frame1,font=('w',16))
        self.Newnum.grid(row=0,column=2)
        
        #Do the buttons for the numbers
        self.N1 = Button(self.Frame2,font=('w',13),bg='white')
        self.N1.grid(row=0,column=0)
        self.N2 = Button(self.Frame2,font=('w',13),bg='white')
        self.N2.grid(row=0,column=1)
        self.N3 = Button(self.Frame2,font=('w',13),bg='white')
        self.N3.grid(row=0,column=2)
        self.N4 = Button(self.Frame2,font=('w',13),bg='white')
        self.N4.grid(row=0,column=3)
        self.N5 = Button(self.Frame2,font=('w',13),bg='white')
        self.N5.grid(row=0,column=4)
        
        #Do the buttons for the signs
        self.S1 = Button(self.Frame3,font=('w',13),bg='white')
        self.S1.grid(row=0,column=0)
        self.S2 = Button(self.Frame3,font=('w',13),bg='white')
        self.S2.grid(row=0,column=1)
        self.S3 = Button(self.Frame3,font=('w',13),bg='white')
        self.S3.grid(row=0,column=2)
        self.S4 = Button(self.Frame3,font=('w',13),bg='white')
        self.S4.grid(row=0,column=3)
        self.S5 = Button(self.Frame3,font=('w',13),bg='white')
        self.S5.grid(row=0,column=4)
        
        #Create the start over button, and submit button
        self.Clear = Button(self.Frame4,text='Clear!!',font=('w',12),bg='white')
        self.Clear.grid(row=0,column=3)
        self.Advance = Button(self.Frame4,text='Advance',font=('w',12),bg='white')
        self.Advance.grid(row=0,column=4)
        
        #Append all the buttons for the refresh!
        self.Buttons = [self.N1,self.N2,self.N3,self.N4,\
        self.N5,self.S1,self.S2,self.S3,self.S4,self.S5]
        
        #Do all the bindings for the functions
        self.N1.bind('<Button-1>',self.n1)
        self.N2.bind('<Button-1>',self.n2)
        self.N3.bind('<Button-1>',self.n3)
        self.N4.bind('<Button-1>',self.n4)
        self.N5.bind('<Button-1>',self.n5)
        self.S1.bind('<Button-1>',self.s1)
        self.S2.bind('<Button-1>',self.s2)
        self.S3.bind('<Button-1>',self.s3)
        self.S4.bind('<Button-1>',self.s4)
        self.S5.bind('<Button-1>',self.s5)
        self.Clear.bind('<Button-1>',self.clearit)
        self.Advance.bind('<Button-1>',self.GoodJob)

        
        #Create all the texts!!
        self.Oldnum['text'] = 23
        self.Newnum['text'] = 25
        self.N1['text'] = 4
        self.N2['text'] = 6
        self.N3['text'] = 2
        self.N4['text'] = 13
        self.N5['text'] = 7
        self.S1['text'] = '-'
        self.S2['text'] = '*'
        self.S3['text'] = '+'
        self.S4['text'] = '-'
        self.S5['text'] = '/'
        
        #Define working number and calculation!
        self.workingnumber = self.Oldnum['text']
        self.refreshnum = self.workingnumber
        self.calc = Text(level1)
        
    #Function time!! The Number buttons first
    def n1(self,event):
        self.calc.insert(END,self.N1['text'])
        self.ans = self.calc.get(1.0,END)
        self.Oldnum['text'] = eval(self.ans)
        self.workingnumber = eval(self.ans)
        self.calc.delete(1.0,END)
        self.N1.config(state=DISABLED,bg='black')
    
    def n2(self,event):
        self.calc.insert(END,self.N2['text'])
        self.ans = self.calc.get(1.0,END)
        self.Oldnum['text'] = eval(self.ans)
        self.workingnumber = eval(self.ans)
        self.calc.delete(1.0,END)
        self.N2.config(state=DISABLED,bg='black')
    
    def n3(self,event):
        self.calc.insert(END,self.N3['text'])
        self.ans = self.calc.get(1.0,END)
        self.Oldnum['text'] = eval(self.ans)
        self.workingnumber = eval(self.ans)
        self.calc.delete(1.0,END)
        self.N3.config(state=DISABLED,bg='black')

    def n4(self,event):
        self.calc.insert(END,self.N4['text'])
        self.ans = self.calc.get(1.0,END)
        self.Oldnum['text'] = eval(self.ans)
        self.workingnumber = eval(self.ans)
        self.calc.delete(1.0,END)
        self.N4.config(state=DISABLED,bg='black')

    def n5(self,event):
        self.calc.insert(END,self.N5['text'])
        self.ans = self.calc.get(1.0,END)
        self.Oldnum['text'] = eval(self.ans)
        self.workingnumber = eval(self.ans)
        self.calc.delete(1.0,END)
        self.N5.config(state=DISABLED,bg='black')    
        
    #The sign buttons now
    def s1(self,event):
        self.calc.insert(END,self.workingnumber)
        self.calc.insert(END,self.S1['text'])
        self.S1.config(state=DISABLED,bg='black')
    
    def s2(self,event):
        self.calc.insert(END,self.workingnumber)
        self.calc.insert(END,self.S2['text'])
        self.S2.config(state=DISABLED,bg='black')
        
    def s3(self,event):
        self.calc.insert(END,self.workingnumber)
        self.calc.insert(END,self.S3['text'])
        self.S3.config(state=DISABLED,bg='black')
        
    def s4(self,event):
        self.calc.insert(END,self.workingnumber)
        self.calc.insert(END,self.S4['text'])
        self.S4.config(state=DISABLED,bg='black')
        
    def s5(self,event):
        self.calc.insert(END,self.workingnumber)
        self.calc.insert(END,self.S5['text'])
        self.S5.config(state=DISABLED,bg='black')
        
    #Make the clear function
    def clearit(self,event):
        self.calc.delete(1.0,END)
        self.workingnumber = self.refreshnum
        self.Oldnum['text'] = self.workingnumber
        for i in self.Buttons:
            i.config(state=NORMAL,bg='white')
    
    #Define next
    def GoodJob(self,event):
        if self.Oldnum['text'] == self.Newnum['text']:
            execfile('Level2.py')
            
            

            
            
        
        
        
        
        
arithmatic = Arithmatic(Level1)
Level1.title('Arith Me Not')
Level1.config(bg='goldenrod1')
Level1.mainloop()        
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 17:52:27 2017

@author: michael
"""

"""import sympy as sy
x = sy.Symbol('x')

C1 = input('Concentration your diluting?: ')
C2 = input('Concentration you want?: ')
V2 = input('Volume that you want?: ')

V1 = sy.solve(C1*x - C2*V2,x)


print 'Put',V1[0],'of the concentrate, and',(V2-V1[0]),'of water'"""

import sympy as sy
from Tkinter import *
root = Tk()

class C1V1:
    
    def calc(self,event):
        self.C1v = int(self.C1.get())
        self.C2v = int(self.C2.get())
        self.V2v = int(self.V2.get())
        self.V1v = sy.solve(self.C1v*self.x - self.C2v*self.V2v)
        self.Solution = Label(master,text=('Put',self.V1v[0],'of the concentrate,\
 and',(self.V2v - self.V1v[0],'of water')))
        self.Solution.grid(row=3,columnspan=2)
    
    def __init__(self,master):
        self.C1 = Entry(master,width=10)
        self.C1.grid(row=0,column=1)
        self.C1t = Label(master,text='Enter concentration you have')
        self.C1t.grid(row=0,column=0,sticky = W)
        self.C2 = Entry(master,width=10)
        self.C2.grid(row=1,column=1)
        self.C2t = Label(master,text='Enter the concentration you want')
        self.C2t.grid(row=1,column=0,sticky=W)
        self.V2 = Entry(master,width=10)
        self.V2.grid(row=2,column=1)
        self.V2t = Label(master,text='How much volume do you want?')
        self.V2t.grid(row=2,column=0,sticky=W)
        #The button
        self.Calculate = Button(master,text='Calculate',bg='white',fg='black')
        self.Calculate.grid(row=3,columnspan=2)
        self.Calculate.bind('<Return>',self.calc)
        self.x = sy.Symbol('x')
        self.Solution = Label(master,text='hey')
        
    def calc(self,event):
        self.C1v = float(self.C1.get())
        self.C2v = float(self.C2.get())
        self.V2v = float(self.V2.get())
        self.V1v = sy.solve(self.C1v*self.x - self.C2v*self.V2v)
        self.Solution['text'] =('Put',self.V1v[0],'of the concentrate,\
 and',(self.V2v - self.V1v[0],'of water'))
        self.Solution.grid(row=4,columnspan=2)
        

        
        
        
        
        
        
        
        
c1 = C1V1(root)
root.mainloop()


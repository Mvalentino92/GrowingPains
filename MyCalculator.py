#!/usr/bin/env python
from __future__ import division
from Tkinter import *


class CalcClass:
    
    def __init__(self,master):
        #First we make the display
        self.frame1 = Frame(master)
        self.frame1.pack(side=TOP)
        #Then we make the frame that will house the buttons
        self.frame2 = Frame(master)
        self.frame2.pack(side=TOP)
        self.frame2.config(bg = 'cyan')
        
        #Now we make all the  buttons, starting with rows
        #First row
        self.bdivide = Button(self.frame2,text='/\nswitch',bg='white',height=5,width=6)
        self.bdivide.grid(row=3,column=3)
        self.bdivide.bind('<Button-1>',self.divide)
        self.bdivide.bind('<Button-3>',self.switch)  
        self.bdivide.bind('<Return>',self.switch)
        
        self.b1 = Button(self.frame2,text='1',bg='white',height=5,width=6)
        self.b1.grid(row=0,column=0)
        self.b1.bind('<Button-1>',self.one)
        
        self.b2 = Button(self.frame2,text='2',bg='white',height=5,width=6)
        self.b2.grid(row=0,column=1)
        self.b2.bind('<Button-1>',self.two)
        
        self.b3 = Button(self.frame2,text='3',bg='white',height=5,width=6)
        self.b3.grid(row=0,column=2)
        self.b3.bind('<Button-1>',self.three)
        
        self.bplus = Button(self.frame2,text='+',bg='white',height=5,width=6)
        self.bplus.grid(row=0,column=3)
        self.bplus.bind('<Button>',self.add)
        
        
        #Second row
        self.b4 = Button(self.frame2,text='4',bg='white',height=5,width=6)
        self.b4.grid(row=1,column=0)
        self.b4.bind('<Button-1>',self.four)
        
        self.b5 = Button(self.frame2,text='5',bg='white',height=5,width=6)
        self.b5.grid(row=1,column=1)
        self.b5.bind('<Button-1>',self.five)
        
        self.b6 = Button(self.frame2,text='6',bg='white',height=5,width=6)
        self.b6.grid(row=1,column=2)
        self.b6.bind('<Button-1>',self.six)
        
        self.bminus = Button(self.frame2,text='-',bg='white',height=5,width=6)
        self.bminus.grid(row=1,column=3)
        self.bminus.bind('<Button-1>',self.minus)
        
        #Third row
        self.b7 = Button(self.frame2,text='7',bg='white',height=5,width=6)
        self.b7.grid(row=2,column=0)
        self.b7.bind('<Button-1>',self.seven)
        
        self.b8 = Button(self.frame2,text='8',bg='white',height=5,width=6)
        self.b8.grid(row=2,column=1)
        self.b8.bind('<Button-1>',self.eight)
        
        self.b9 = Button(self.frame2,text='9',bg='white',height=5,width=6)
        self.b9.grid(row=2,column=2)
        self.b9.bind('<Button-1>',self.nine)
        
        self.bmulti = Button(self.frame2,text='*',bg='white',height=5,width=6)
        self.bmulti.grid(row=2,column=3)
        self.bmulti.bind('<Button-1>',self.multi)
        
        #Fourth Row
        
        self.bperiod = Button(self.frame2,text='.',bg='white',height=5,width=6)
        self.bperiod.grid(row=3,column=0)
        self.bperiod.bind('<Button-1>',self.period)
        
        self.b0 = Button(self.frame2,text='0',bg='white',height=5,width=6)
        self.b0.grid(row=3,column=1)
        self.b0.bind('<Button-1>',self.zero)
        
        #Fifth Row
        self.pleft = Button(self.frame2,text='(',bg='white',height=5,width=6)
        self.pleft.grid(row=4,column=0)
        self.pleft.bind('<Button-1>',self.paraleft)
        
        self.pright = Button(self.frame2,text=')',bg='white',height=5,width=6)
        self.pright.grid(row=4,column=1)
        self.pright.bind('<Button-1>',self.pararight)
        
        self.clear = Button(self.frame2,text='clear',bg='white',height=5,width=6)
        self.clear.grid(row=4,column=3)
        self.clear.bind('<Button-1>',self.clearspace)
        self.clear.bind('<Return>',self.clearspace)
        
        self.ans = Button(self.frame2,text='Ans',bg='white',height=5,width=6)
        self.ans.grid(row=4,column=2)
        self.ans.bind('<Button-1>',self.answer)
        self.ans.bind('<Return>',self.answer)
        
        self.beq = Button(self.frame2,text='=',bg='white',height=5,width=6)
        self.beq.grid(row=3,column=2)
        self.beq.bind('<Button-1>',self.eq)
        self.beq.bind('<Return>',self.eq)
        
        
        #Make the display using label
        
        self.screen = Text(self.frame1,bg='floral white',width=30,height=5,font=('w',11))
        self.screen.pack(side=TOP)
        
        
        
        
        #Make the functions for each button
    def one(self,event):
        self.screen.insert(END,1)
    
    def two(self,event):
        self.screen.insert(END,2)
    
    
    def three(self,event):
        self.screen.insert(END,3)
    
    
    def four(self,event):
        self.screen.insert(END,4)
    
    
    def five(self,event):
        self.screen.insert(END,5)
    
    
    def six(self,event):
        self.screen.insert(END,6)
    
    
    def seven(self,event):
        self.screen.insert(END,7)
    
    
    def eight(self,event):
        self.screen.insert(END,8)
    
    
    def nine(self,event):
        self.screen.insert(END,9)
    
    
    def zero(self,event):
        self.screen.insert(END,0)
    

    def add(self,event):
        self.screen.insert(END,'+')
    
    
    def minus(self,event):
        self.screen.insert(END,'-')
    
    
    def multi(self,event):
        self.screen.insert(END,'*')
    
    
    def divide(self,event):
        self.screen.insert(END,'/')
    
    
    def paraleft(self,event):
        self.screen.insert(END,'(')
    
    def period(self,event):
        self.screen.insert(END,'.')
    
    def pararight(self,event):
        self.screen.insert(END,')')
        
    def sin(self,event):
        self.screen.insert(END,'sin')
    
    def cos(self,event):
        self.screen.insert(END,'cos')
        
    def tan(self,event):
        self.screen.insert(END,'tan')
        
    def e(self,event):
        self.screen.insert(END,'exp')
    
    def log(self,event):
        self.screen.insert(END,'log')
    
    def pi(self,event):
        self.screen.insert(END,'pi')
    
    def power(self,event):
        self.screen.insert(END,'**')
    
    def sqrt(self,event):
        self.screen.insert(END,'sqrt')
    
    def evod(self,event):
        self.screen.insert(END,'%')
        
        #The equal and clear function
    
    def eq(self,event):
        self.compute = (self.screen.get(1.0,END))
        self.answer = float((eval(self.compute)))
        self.screen.insert(END,'\n' + str((self.answer)))
        self.beq.focus()
        
        
        
    
    
    
    def clearspace(self,event):
        self.screen.delete(1.0,END)
        
    def answer(self,event):
        self.screen.delete(1.0,END)
        self.screen.insert(END,self.answer)
        
    def switch(self,event):
        self.b0['text'] = 'switch'
        self.b0.bind('<Button-1>',self.otherswitch)
        #Change all the other buttons
        self.b1['text'] = 'sin'
        self.b1.bind('<Button-1>',self.sin)
        
        self.b2['text'] = 'cos'
        self.b2.bind('<Button-1>',self.cos)
        
        self.b3['text'] = 'tan'
        self.b3.bind('<Button-1>',self.tan)
        
        self.b4['text'] = 'ln'
        self.b4.bind('<Button-1>',self.log)
        
        self.b5['text'] = 'pi'
        self.b5.bind('<Button-1>',self.pi)
        
        self.b6['text'] = 'e'
        self.b6.bind('<Button-1>',self.e)
        
        self.b7['text'] = '^'
        self.b7.bind('<Button-1>',self.power)
        
        self.b8['text'] = 'sqrt'
        self.b8.bind('<Button-1>',self.sqrt)
        
        self.b9['text'] = '%'
        self.b9.bind('<Button-1>',self.evod)
        
    
        
        
       
        
    def otherswitch(self,event):
        self.b0['text'] = '0'
        #redo everything
        self.b1['text'] = '1'
        self.b1.bind('<Button-1>',self.one)
        
        self.b2['text'] = '2'
        self.b2.bind('<Button-1>',self.two)
        
        self.b3['text'] = '3'
        self.b3.bind('<Button-1>',self.three)
        
        self.b4['text'] = '4'
        self.b4.bind('<Button-1>',self.four)
        
        self.b5['text'] = '5'
        self.b5.bind('<Button-1>',self.five)
        
        self.b6['text'] = '6'
        self.b6.bind('<Button-1>',self.six)
        
        self.b7['text'] = '7'
        self.b7.bind('<Button-1>',self.seven)
        
        self.b8['text'] = '8'
        self.b8.bind('<Button-1>',self.eight)
        
        self.b9['text'] = '9'
        self.b9.bind('<Button-1>',self.nine)

        
        
    
    
   
        
 
        
root = Tk()
root.title('Mikes Calculator')
root.config(bg='purple')
myclass = CalcClass(root)
root.mainloop()
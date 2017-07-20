# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 18:15:59 2017

@author: michael
"""

from Tkinter import *
from numpy import *

class MyClass:
    
    def __init__(self,master):
        self.frametop = Frame(master)
        self.frametop.pack(side=TOP)
        self.frame1 = Frame(master)
        self.frame1.pack(side=LEFT)
        self.frame2 = Frame(master)
        self.frame2.pack(side=LEFT)
        self.frame3 = Frame(master)
        self.frame3.pack(side=LEFT)
        self.frame4 = Frame(master)
        self.frame4.pack(side=LEFT)
        self.frame5 = Frame(master)
        self.frame5.pack(side=LEFT)
        self.frame6 = Frame(master)
        self.frame6.pack(side=LEFT)
        self.frame7 = Frame(master)
        self.frame7.pack(side=LEFT)
        #Buttons
        self.col1 = Button(self.frametop,text='Drop Here',font=('w',int(14)))
        self.col1.pack(side=LEFT)
        self.col1.bind('<Button-1>',self.column1)
        self.col1.bind('<Button-3>',self.column1b)
        self.col2 = Button(self.frametop,text='Drop Here',font=('w',int(14)))
        self.col2.pack(side=LEFT)
        self.col2.bind('<Button-1>',self.column2)
        self.col2.bind('<Button-3>',self.column2b)
        self.col3 = Button(self.frametop,text='Drop Here',font=('w',int(14)))
        self.col3.pack(side=LEFT)
        self.col3.bind('<Button-1>',self.column3)
        self.col3.bind('<Button-3>',self.column3b)
        self.col4 = Button(self.frametop,text='Drop Here',font=('w',int(14)))
        self.col4.pack(side=LEFT)
        self.col4.bind('<Button-1>',self.column4)
        self.col4.bind('<Button-3>',self.column4b)
        self.col5 = Button(self.frametop,text='Drop Here',font=('w',int(14)))
        self.col5.pack(side=LEFT)
        self.col5.bind('<Button-1>',self.column5)
        self.col5.bind('<Button-3>',self.column5b)
        self.col6 = Button(self.frametop,text='Drop Here',font=('w',int(14)))
        self.col6.pack(side=LEFT)
        self.col6.bind('<Button-1>',self.column6)
        self.col6.bind('<Button-3>',self.column6b)
        self.col7 = Button(self.frametop,text='Drop Here',font=('w',int(14)))
        self.col7.pack(side=LEFT)
        self.col7.bind('<Button-1>',self.column7)
        self.col7.bind('<Button-3>',self.column7b)
        #Canvas's
        self.can1 = Canvas(self.frame1,height = 600, width = 140)
        self.can1.pack()
        self.can2 = Canvas(self.frame2,height = 600, width = 140)
        self.can2.pack()
        self.can3 = Canvas(self.frame3,height = 600, width = 140)
        self.can3.pack()
        self.can4 = Canvas(self.frame4,height = 600, width = 140)
        self.can4.pack()
        self.can5 = Canvas(self.frame5,height = 600, width = 140)
        self.can5.pack()
        self.can6 = Canvas(self.frame6,height = 600, width = 140)
        self.can6.pack()
        self.can7 = Canvas(self.frame7,height = 600, width = 140)
        self.can7.pack()
        #Circles in canvases
        self.can1_circ0 = self.can1.create_oval(20,600,120,500,width=3.5)
        self.can1_circ1 = self.can1.create_oval(20,500,120,400,width=3.5)
        self.can1_circ2 = self.can1.create_oval(20,400,120,300,width=3.5)
        self.can1_circ3 = self.can1.create_oval(20,300,120,200,width=3.5)
        self.can1_circ4 = self.can1.create_oval(20,200,120,100,width=3.5)
        self.can1_circ5 = self.can1.create_oval(20,100,120,0,width=3.5)
        
        self.can2_circ0 = self.can2.create_oval(20,600,120,500,width=3.5)
        self.can2_circ1 = self.can2.create_oval(20,500,120,400,width=3.5)
        self.can2_circ2 = self.can2.create_oval(20,400,120,300,width=3.5)
        self.can2_circ3= self.can2.create_oval(20,300,120,200,width=3.5)
        self.can2_circ4 = self.can2.create_oval(20,200,120,100,width=3.5)
        self.can2_circ5 = self.can2.create_oval(20,100,120,0,width=3.5)
        
        self.can3_circ0 = self.can3.create_oval(20,600,120,500,width=3.5)
        self.can3_circ1 = self.can3.create_oval(20,500,120,400,width=3.5)
        self.can3_circ2 = self.can3.create_oval(20,400,120,300,width=3.5)
        self.can3_circ3 = self.can3.create_oval(20,300,120,200,width=3.5)
        self.can3_circ4 = self.can3.create_oval(20,200,120,100,width=3.5)
        self.can3_circ5 = self.can3.create_oval(20,100,120,0,width=3.5)
        
        self.can4_circ0 = self.can4.create_oval(20,600,120,500,width=3.5)
        self.can4_circ1 = self.can4.create_oval(20,500,120,400,width=3.5)
        self.can4_circ2 = self.can4.create_oval(20,400,120,300,width=3.5)
        self.can4_circ3 = self.can4.create_oval(20,300,120,200,width=3.5)
        self.can4_circ4 = self.can4.create_oval(20,200,120,100,width=3.5)
        self.can4_circ5 = self.can4.create_oval(20,100,120,0,width=3.5)
        
        self.can5_circ0 = self.can5.create_oval(20,600,120,500,width=3.5)
        self.can5_circ1 = self.can5.create_oval(20,500,120,400,width=3.5)
        self.can5_circ2 = self.can5.create_oval(20,400,120,300,width=3.5)
        self.can5_circ3 = self.can5.create_oval(20,300,120,200,width=3.5)
        self.can5_circ4 = self.can5.create_oval(20,200,120,100,width=3.5)
        self.can5_circ5 = self.can5.create_oval(20,100,120,0,width=3.5)
        
        self.can6_circ0 = self.can6.create_oval(20,600,120,500,width=3.5)
        self.can6_circ1 = self.can6.create_oval(20,500,120,400,width=3.5)
        self.can6_circ2 = self.can6.create_oval(20,400,120,300,width=3.5)
        self.can6_circ3 = self.can6.create_oval(20,300,120,200,width=3.5)
        self.can6_circ4 = self.can6.create_oval(20,200,120,100,width=3.5)
        self.can6_circ5 = self.can6.create_oval(20,100,120,0,width=3.5)
        
        self.can7_circ0 = self.can7.create_oval(20,600,120,500,width=3.5)
        self.can7_circ1 = self.can7.create_oval(20,500,120,400,width=3.5)
        self.can7_circ2 = self.can7.create_oval(20,400,120,300,width=3.5)
        self.can7_circ3 = self.can7.create_oval(20,300,120,200,width=3.5)
        self.can7_circ4 = self.can7.create_oval(20,200,120,100,width=3.5)
        self.can7_circ5 = self.can7.create_oval(20,100,120,0,width=3.5)
        self.board = zeros((7,7))
        self.board[-1,:] = 2
        
    def column1(self,event):
        self.circles = [self.can1_circ0,self.can1_circ1,self.can1_circ2,\
        self.can1_circ3,self.can1_circ4,self.can1_circ5]
        size1 = [100,200,300,400,500,600]
        size2 =[0,100,200,300,400,500]
        x1 = self.board[:,0].nonzero() 
        self.board[(x1[0][0]-1),0] = 1
        for i in self.board[:,0].tolist():
            if i == 1:
                self.circles[self.board[:,0].tolist().index(i)] = self.can1.create_oval(20,size1[self.board[:,0].tolist().index(i)],120,size2[self.board[:,0].tolist().index(i)],fill='red')
                
    def column1b(self,event):
        self.circles = [self.can1_circ0,self.can1_circ1,self.can1_circ2,\
        self.can1_circ3,self.can1_circ4,self.can1_circ5]
        size1 = [100,200,300,400,500,600]
        size2 =[0,100,200,300,400,500]
        x1 = self.board[:,0].nonzero() 
        self.board[(x1[0][0]-1),0] = 1
        for i in self.board[:,0].tolist():
            if i == 1:
                self.circles[self.board[:,0].tolist().index(i)] = self.can1.create_oval(20,size1[self.board[:,0].tolist().index(i)],120,size2[self.board[:,0].tolist().index(i)],fill='blue')
                           
    def column2(self,event):
        self.circles = [self.can2_circ0,self.can2_circ1,self.can2_circ2,\
        self.can2_circ3,self.can2_circ4,self.can2_circ5]
        size1 = [100,200,300,400,500,600]
        size2 =[0,100,200,300,400,500]
        x1 = self.board[:,1].nonzero() 
        self.board[(x1[0][0]-1),1] = 1
        for i in self.board[:,1].tolist():
            if i == 1:
                self.circles[self.board[:,1].tolist().index(i)] = self.can2.create_oval(20,size1[self.board[:,1].tolist().index(i)],120,size2[self.board[:,1].tolist().index(i)],fill='red')
                
    def column2b(self,event):
        self.circles = [self.can2_circ0,self.can2_circ1,self.can2_circ2,\
        self.can2_circ3,self.can2_circ4,self.can2_circ5]
        size1 = [100,200,300,400,500,600]
        size2 =[0,100,200,300,400,500]
        x1 = self.board[:,1].nonzero() 
        self.board[(x1[0][0]-1),1] = 1
        for i in self.board[:,1].tolist():
            if i == 1:
                self.circles[self.board[:,1].tolist().index(i)] = self.can2.create_oval(20,size1[self.board[:,1].tolist().index(i)],120,size2[self.board[:,1].tolist().index(i)],fill='blue')
                   
            
    def column3(self,event):
        self.circles = [self.can3_circ0,self.can3_circ1,self.can3_circ2,\
        self.can3_circ3,self.can3_circ4,self.can3_circ5]
        size1 = [100,200,300,400,500,600]
        size2 =[0,100,200,300,400,500]
        x1 = self.board[:,2].nonzero() 
        self.board[(x1[0][0]-1),2] = 1
        for i in self.board[:,2].tolist():
            if i == 1:
                self.circles[self.board[:,2].tolist().index(i)] = self.can3.create_oval(20,size1[self.board[:,2].tolist().index(i)],120,size2[self.board[:,2].tolist().index(i)],fill='red')

    def column3b(self,event):
        self.circles = [self.can3_circ0,self.can3_circ1,self.can3_circ2,\
        self.can3_circ3,self.can3_circ4,self.can3_circ5]
        size1 = [100,200,300,400,500,600]
        size2 =[0,100,200,300,400,500]
        x1 = self.board[:,2].nonzero() 
        self.board[(x1[0][0]-1),2] = 1
        for i in self.board[:,2].tolist():
            if i == 1:
                self.circles[self.board[:,2].tolist().index(i)] = self.can3.create_oval(20,size1[self.board[:,2].tolist().index(i)],120,size2[self.board[:,2].tolist().index(i)],fill='blue')
          
     
    def column4(self,event):
        self.circles = [self.can4_circ0,self.can4_circ1,self.can4_circ2,\
        self.can4_circ3,self.can4_circ4,self.can4_circ5]
        size1 = [100,200,300,400,500,600]
        size2 =[0,100,200,300,400,500]
        x1 = self.board[:,3].nonzero() 
        self.board[(x1[0][0]-1),3] = 1
        for i in self.board[:,3].tolist():
            if i == 1:
                self.circles[self.board[:,3].tolist().index(i)] = self.can4.create_oval(20,size1[self.board[:,3].tolist().index(i)],120,size2[self.board[:,3].tolist().index(i)],fill='red')
      
    def column4b(self,event):
        self.circles = [self.can4_circ0,self.can4_circ1,self.can4_circ2,\
        self.can4_circ3,self.can4_circ4,self.can4_circ5]
        size1 = [100,200,300,400,500,600]
        size2 =[0,100,200,300,400,500]
        x1 = self.board[:,3].nonzero() 
        self.board[(x1[0][0]-1),3] = 1
        for i in self.board[:,3].tolist():
            if i == 1:
                self.circles[self.board[:,3].tolist().index(i)] = self.can4.create_oval(20,size1[self.board[:,3].tolist().index(i)],120,size2[self.board[:,3].tolist().index(i)],fill='blue')
                
          
    def column5(self,event):
        self.circles = [self.can5_circ0,self.can5_circ1,self.can5_circ2,\
        self.can5_circ3,self.can5_circ4,self.can5_circ5]
        size1 = [100,200,300,400,500,600]
        size2 =[0,100,200,300,400,500]
        x1 = self.board[:,4].nonzero() 
        self.board[(x1[0][0]-1),4] = 1
        for i in self.board[:,4].tolist():
            if i == 1:
                self.circles[self.board[:,4].tolist().index(i)] = self.can5.create_oval(20,size1[self.board[:,4].tolist().index(i)],120,size2[self.board[:,4].tolist().index(i)],fill='red')
     
    def column5b(self,event):
        self.circles = [self.can5_circ0,self.can5_circ1,self.can5_circ2,\
        self.can5_circ3,self.can5_circ4,self.can5_circ5]
        size1 = [100,200,300,400,500,600]
        size2 =[0,100,200,300,400,500]
        x1 = self.board[:,4].nonzero() 
        self.board[(x1[0][0]-1),4] = 1
        for i in self.board[:,4].tolist():
            if i == 1:
                self.circles[self.board[:,4].tolist().index(i)] = self.can5.create_oval(20,size1[self.board[:,4].tolist().index(i)],120,size2[self.board[:,4].tolist().index(i)],fill='blue')
          
     
    def column6(self,event):
        self.circles = [self.can6_circ0,self.can6_circ1,self.can6_circ2,\
        self.can6_circ3,self.can6_circ4,self.can6_circ5]
        size1 = [100,200,300,400,500,600]
        size2 =[0,100,200,300,400,500]
        x1 = self.board[:,5].nonzero() 
        self.board[(x1[0][0]-1),5] = 1
        for i in self.board[:,5].tolist():
            if i == 1:
                self.circles[self.board[:,5].tolist().index(i)] = self.can6.create_oval(20,size1[self.board[:,5].tolist().index(i)],120,size2[self.board[:,5].tolist().index(i)],fill='red')
          
    def column6b(self,event):
        self.circles = [self.can6_circ0,self.can6_circ1,self.can6_circ2,\
        self.can6_circ3,self.can6_circ4,self.can6_circ5]
        size1 = [100,200,300,400,500,600]
        size2 =[0,100,200,300,400,500]
        x1 = self.board[:,5].nonzero() 
        self.board[(x1[0][0]-1),5] = 1
        for i in self.board[:,5].tolist():
            if i == 1:
                self.circles[self.board[:,5].tolist().index(i)] = self.can6.create_oval(20,size1[self.board[:,5].tolist().index(i)],120,size2[self.board[:,5].tolist().index(i)],fill='blue')
                                        
                                                             
    def column7(self,event):
        self.circles = [self.can7_circ0,self.can7_circ1,self.can7_circ2,\
        self.can7_circ3,self.can7_circ4,self.can7_circ5]
        size1 = [100,200,300,400,500,600]
        size2 =[0,100,200,300,400,500]
        x1 = self.board[:,6].nonzero() 
        self.board[(x1[0][0]-1),6] = 1
        for i in self.board[:,6].tolist():
            if i == 1:
                self.circles[self.board[:,6].tolist().index(i)] = self.can7.create_oval(20,size1[self.board[:,6].tolist().index(i)],120,size2[self.board[:,6].tolist().index(i)],fill='red')
                                                  
    def column7b(self,event):
        self.circles = [self.can7_circ0,self.can7_circ1,self.can7_circ2,\
        self.can7_circ3,self.can7_circ4,self.can7_circ5]
        size1 = [100,200,300,400,500,600]
        size2 =[0,100,200,300,400,500]
        x1 = self.board[:,6].nonzero() 
        self.board[(x1[0][0]-1),6] = 1
        for i in self.board[:,6].tolist():
            if i == 1:
                self.circles[self.board[:,6].tolist().index(i)] = self.can7.create_oval(20,size1[self.board[:,6].tolist().index(i)],120,size2[self.board[:,6].tolist().index(i)],fill='blue')
                                                  
         
root = Tk()
root.title('Connect Four')
root.config(bg='white')
myclass = MyClass(root)
root.mainloop()        
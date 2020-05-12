# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 13:01:51 2020

@author: kingc


Change file directories to match where you put the images for the game 
prime climb gb.tiff
green pawn
blue pawn
"""

from tkinter import *
from PIL import Image, ImageTk
import numpy as np

class Application(Frame):
    def createboard(self):
        img_name = "prime climb gb.tiff"
        
        load = Image.open('C:\\Users\\kingc\\.spyder-py3\\images\\'+img_name) #Put images at this extension
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.grid(row=0,column=0,rowspan=655,columnspan=655)

    def createPanel(self):
        self.dieroll = Button(self)
        self.dieroll["text"] = "      Roll      "
        self.dieroll["command"] = self.rolldice
        self.dieroll.grid(row=1, column=660, rowspan = 25, columnspan=10)
        
        self.addbut = Button(self, text="    +    ", command=lambda: self.entermoves('op',0))
        self.subbut = Button(self, text="    -    ", command=lambda: self.entermoves('op',1))
        self.mulbut = Button(self, text="    x    ", command=lambda: self.entermoves('op',2)) 
        self.divbut = Button(self, text="    /    ", command=lambda: self.entermoves('op',3))

        self.addbut.grid(row=25, column=660, rowspan = 25, columnspan=5)
        self.subbut.grid(row=25, column=665, rowspan = 25, columnspan=5)
        self.mulbut.grid(row=50, column=660, rowspan = 25, columnspan=5)
        self.divbut.grid(row=50, column=665, rowspan = 25, columnspan=5)
        
        self.enter = Button(self, text="Enter", command=lambda: self.calcmove())
        self.clear = Button(self, text="Clear", command=lambda: {self.clearmove(1,1),self.writemoves(0,0,0)})
        
        self.enter.grid(row=75, column=660, rowspan = 25, columnspan=5)
        self.clear.grid(row=75, column=665, rowspan = 25, columnspan=5)
        
        self.textbox = Text(self, width=12, height=33)
        self.textbox.grid(row=100, column=660, sticky=NW, rowspan=600, columnspan=10)
        
    def pawn(self):
        for color in ['blue', 'green']:
            img_name = "%s pawn.tiff" %color
        
            load1 = Image.open('C:\\Users\\kingc\\.spyder-py3\\images\\'+img_name)
            render1 = ImageTk.PhotoImage(load1)
            if color == "blue":
                self.p1 = Label(self, image=render1,bg='black')
                self.p1.image = render1
                pawnpos = self.pos1
                xloc = self.loc[0,int(pawnpos)]
                yloc = self.loc[1,int(pawnpos)]
                self.p1.grid(row=yloc,column=xloc, rowspan=30, columnspan=20)
            if color == "green":
                self.p2 = Label(self, image=render1, bg='black')
                self.p2.image = render1
                pawnpos = self.pos2
                xloc = self.loc[0,int(pawnpos)]
                yloc = self.loc[1,int(pawnpos)]
                self.p2.grid(row=yloc,column=xloc, rowspan=30, columnspan=20)
        
    def movepawn(self):
            self.p1.destroy()
            self.p2.destroy()
            self.pawn()
        
    def writemoves(self,endturn,pos2,win):
        play = self.turn
        if play == 'P1':
            play = 'P1 turn    '
            pos1 = str(int(self.pos1))
        if play == 'P2':
            play = '    P2 turn'
            pos1 = str(int(self.pos2))
        n1 = str(self.num1)
        n2 = str(self.num2)
        o1 = self.op1
        o2 = self.op2
        if endturn==0:
            self.textbox.delete("1.0","2.end")
            self.textbox.insert("1.0",pos1+o1+n1+o2+n2+'=')
            self.textbox.insert("1.0",play+"\n")

        if endturn==1:
            
            self.textbox.delete("1.0","2.end")
            self.textbox.insert("1.0",pos1+o1+n1+o2+n2+'='+str(int(pos2)))
            self.textbox.insert("1.0",play+"\n")
            self.textbox.insert("1.0","\n\n\n")
            
    def rolldice(self):
        self.nsides = 10
        nside = self.nsides
        self.die = np.random.randint(1,nside+1,2)  
        die = self.die
        self.dieroll.destroy()
        
        self.die1 = Button(self, text="    "+str(die[0])+"    ", command=lambda: self.entermoves('num',0))
        self.die2 = Button(self, text="    "+str(die[1])+"    ", command=lambda: self.entermoves('num',1))
        
        self.die1.grid(row=1, column=660, rowspan = 25, columnspan=5)
        self.die2.grid(row=1, column=665, rowspan = 25, columnspan=5)

    def entermoves(self,tp,place):
        if tp == 'op':
            inputs = ['+','-','*','/']
            if self.op1 == ' ':
                self.op1 = inputs[place]
                self.writemoves(0,0,0)
            else:
                if self.op2 == ' ':
                    self.op2 = inputs[place]
                    self.writemoves(0,0,0)
                else:
                    self.clearmove(0,1)
                    self.writemoves(0,0,0)
        else:
            s = np.sum(self.diceused)
            die = self.diceused[place]
            if s == 0:
                self.num1 = self.die[place]
                self.writemoves(0,0,0)
                self.diceused[place] = 1
            else:
                if s == 1 and die == 0:
                    self.num2 = self.die[place]
                    self.writemoves(0,0,0)
                    self.diceused[place] = 1
                else:
                    self.clearmove(1,0)
                    self.writemoves(0,0,0)

    def resetdice(self):
        self.die1.destroy()
        self.die2.destroy()
        
        self.dieroll = Button(self)
        self.dieroll["text"] = "      Roll      "
        self.dieroll["command"] = self.rolldice
        self.dieroll.grid(row=1, column=660, rowspan = 25, columnspan=10)

    def clearmove(self,die,op):
        if die == 1:
            self.num1 = ' '
            self.num2 = ' '
            self.diceused = np.array([0,0])            
        if op == 1:
            self.op1 = ' '
            self.op2 = ' '
    
    def compmoves(self):
        end_ = 101
        moves_  = np.zeros((end_+1,end_+1))
        operations = ["+", "-", "*", "/"]
        
        die1 = self.die[0]
        self.num1 = die1
        die2 = self.die[1]
        self.num2 = die2
        start = self.pos2
        
        for i in operations:
            for j in operations:
                f1 = str(start) + i + str(die1)
                pos1 = eval(f1)
                if pos1 == end_:
                    moves_[start,end_] = 1

                f2 = str(pos1) + j + str(die2)
                pos2 = eval(f2)
                if pos2 % 1 == 0 and pos1% 1 == 0 and -1 < pos1 < end_+1 and -1 < pos2 < end_+1:
                    moves_[int(pos1),int(pos2)] = 1

     
                f3 = str(start) + i + str(die2)
                pos3 = eval(f3)
                if pos3 == end_:
                    moves_[start,end_] = 1

                f4 = str(pos3) + j + str(die1)
                pos4 = eval(f4)
                if pos4 % 1 == 0 and pos3% 1 == 0 and -1 < pos3 < end_+1 and -1 < pos4 < end_+1:
                    moves_[int(pos3),int(pos4)] = 1
        self.moves_ = moves_
        
    def computer(self):
        self.rolldice()
        self.compmoves()
        moves_ = self.moves_
        pos1 = self.pos1
        
        #find best move
        moves = np.sum(moves_, axis=0)
        best1 = np.array([101,96,94,95,97,98,93,92,99,100,91,90,89,88,87,86,85,84,83,82,81,80,10,11,12,14,16,18,79,20,23,24,22,25,13,15,9,19,78,17,21,50,30,77,45,33,48,28,32,29,27,46,31,40,49,26,42,44,76,8,47,43,5,75,41,7,4,6,3,39,2,54,38,36,60,37,52,74,55,72,35,51,53,56,34,1,73,57,70,0,58,64,66,59,63,65,71,62,69,68,61,67])
        for i in best1:
            if moves[i] !=0:
                pos2 = i
                self.writemoves(1,pos2,0)
                self.pos2 = pos2
                break
            
        #check for 'sorry'
        if moves_[pos1, pos2] == 1:
             self.pos1 = 0
             
        self.movepawn()
        self.turn = 'P1'
        self.clearmove(1,1)
        self.writemoves(0,0,0)
        self.resetdice()
    
    def calcmove(self):
        num1 = self.num1
        num2 = self.num2
        op1 = self.op1
        op2 = self.op2
        
        #human moves       
        if num1 == ' ' or num2 == ' ' or op1 == ' ' or op2 == ' ':
            pass
        else:
            #set up original positions for p1 and p2
            pos1 = self.pos1
            pos2 = self.pos2
            #evaluate new pos
            newpos1 = eval(str(pos1)+op1+str(num1))
            newpos2 = eval(str(newpos1)+op2+str(num2))
            #check for valid moves
            if newpos1%1 != 0 or 0>newpos1 or newpos1>101 or newpos2%1 != 0 or 0>newpos2 or newpos2>101:
                self.clearmove(1,1)
                self.writemoves(0,0,0)
            else:
                #check for win
                if newpos1 == 101 or newpos2 == 101:
                    self.writemoves(1,newpos2,1)
                    self.pos1 = 101
                    self.winner = 'P1'
                    self.movepawn()
                #check if bumped and set for next turn
                else:
                    self.writemoves(1,newpos2,0)
                    self.pos1 = newpos2
                    if newpos2 == pos2:
                        self.pos2 = 0
                    self.movepawn()
                    self.turn = 'P2'
                    self.clearmove(1,1)
                    self.writemoves(0,0,0)
                    self.resetdice()
                    self.computer()      #computer moves
            
            
                
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.loc = np.array([[327,262,214,170,126,91,62,37,21,14,18,39,54,85,122,164,209,259,310,360,410,457,498,535,562,584,594,596,587,567,541,505,463,407,366,316,266,217,174,136,106,87,77,79,92,115,149,189,235,285,334,386,431,471,504,526,536,531,516,489,452,407,358,308,258,212,176,149,136,138,156,188,230,276,329,376,420,453,473,474,458,426,382,331,282,239,206,196,210,241,285,338,384,412,414,386,338,290,259,269,314,330],[605,590,575,550,520,485,445,400,353,301,250,202,156,115,80,51,31,18,15,18,30,50,78,114,155,203,252,303,352,400,442,478,507,528,539,540,533,517,491,457,416,370,319,270,219,173,137,105,85,74,72,84,103,135,173,218,268,319,368,409,443,468,480,482,469,447,412,369,321,270,223,183,152,136,131,142,166,204,251,302,349,389,414,424,416,393,353,304,254,216,193,193,211,255,303,345,365,358,317,270,248,304]])
        self.turn = 'P1'
        self.createboard()
        self.createPanel()
        self.clearmove(1,1)
        self.pos1 = 0
        self.pos2 = 0
        self.pawn()
        self.writemoves(0,0,0)
        
        

    
    
root = Tk()
root.geometry("800x700")
app = Application(master=root)
root.wm_title("Prime Climb")
app.mainloop()

"""
from tkinter import *
from PIL import Image, ImageTk
import numpy as np

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        img_name = "prime climb gb.tiff"
        
        load = Image.open('C:\\Users\\kingc\\.spyder-py3\\images\\'+img_name)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        return

class panel(Button):
    def __init__(self, master=None):

    def        

class Pawn(Label):
    def __initi(self, window, master=None, lab,, position):
        Label.__init__(self, window, master)
        self.master = master
        self.place()
    def moveto(newpos):
        self.position = newpos
        
root = Tk()
control = Tk()
app = Window(root)
panel = panel(control)
root.wm_title("Prime Climb")
root.geometry("656x656")

panel.mainloop()




       
        self.die = [0,0]
        
        self.turn = 0
        
        self.pawn1 = 
        
        self.pawn2 = 
        
    def diedisp(self,dieroll)   
        self.die = Button(Frame, text=dieroll, fg="red", bg="blue", command=applydie())
        self.die.pack(side=RIGHT)
    
    def rolldice(self):
        self.die = np.random.randint(1,11,2)

    def movpawn1(self,dieroll):
        
    def movpawn2(self,dieroll):
        
    def applydie(self):
        
        
        
"""


"""
from scipy import constants as c
import tkinter as tk
import math as m
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = Image.open('prime climb gameboard.png')
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.place(x=0, y=0)

top = tk.Tk()
app = Window(top)
top.wm_title('primeclimb')
top.geometry('200x120')
top.mainloop()


window = tk.Tk()

def click():
    label1 = tk.Label(window, text="look i clicked a button!")
    label1.pack()
    
button = tk.Button(window, text="click me!", command=click)
button.pack()

window.mainloop()


back = "#265"
ft = "#791"
font1 = "helvetica"

frame = tk.Frame(master=window, bg = back, width=500, height=500)
frame.pack()

def pedal(posx,posy,shape):
    label1 = tk.Label(master=frame, text=shape, font=(font1, 8), bg = back, fg = ft) 
    label1.place(x=250+posx, y=250-posy)
    return label1

def grow(Irr):
    c = 0
    posx = 0
    posy = 0
    pedal(posx,posy,"<3")
    dt = 2*m.pi*Irr
    while posx**2 + posy**2 <= 62500:
        c = c+1
        t = c*dt
        posx = c*m.cos(t)
        posy = c*m.sin(t)
        pedal(posx,posy,"<3")
  
      

grow(c.golden)

window.mainloop()
"""



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 22:50:51 2019

@author: elzhar
"""

import tkinter as tk
from tkinter import messagebox
import socket as sk
import threading as th

s=sk.socket(sk.AF_INET,sk.SOCK_STREAM)
s.setsockopt(sk.SOL_SOCKET,sk.SO_REUSEADDR, 1)
host='127.0.0.1'
port=7001
s.connect((host,port))

window = tk.Tk()
window.title('Client')
window.geometry('450x160')
lb1=tk.Label(window,text='You : X',font=('Helvetica','15'))
lb1.grid(row=0,column=0)
lb2=tk.Label(window,text='Server : O',font=('Helvetica','15'))
lb2.grid(row=1,column=0)
lb3=tk.Label(window,text="it's server Turn",font=('Helvetica','15'))
lb3.grid(row=5,column=0,padx=(10,0))

turn=0
def clicked1():
    global turn
    if btn1['text']=='':
        if turn==1:
            turn=0
            btn1['text']='X'
            lb3['text']=("it's server Turn")
            s.send(str(1).encode('utf-8'))
            check()

def clicked2():
    global turn
    if btn2['text']=='':
        if turn==1:
            turn=0
            btn2['text']='X'
            lb3['text']=("it's server Turn")
            s.send(str(2).encode('utf-8'))
            check()
        
def clicked3():
    global turn
    if btn3['text']=='':
        if turn==1:
            turn=0
            btn3['text']='X'
            lb3['text']=("it's server Turn")
            s.send(str(3).encode('utf-8'))
            check()
        
def clicked4():
    global turn
    if btn4['text']=='':
        if turn==1:
            turn=0
            btn4['text']='X'
            lb3['text']=("it's server Turn")
            s.send(str(4).encode('utf-8'))
            check()
        
def clicked5():
    global turn
    if btn5['text']=='':
        if turn==1:
            turn=0
            btn5['text']='X'
            lb3['text']=("it's server Turn")
            s.send(str(5).encode('utf-8'))
            check()
        
def clicked6():
    global turn
    if btn6['text']=='':
        if turn==1:
            turn=0
            btn6['text']='X'
            lb3['text']=("it's server Turn")
            s.send(str(6).encode('utf-8'))
            check()
        
def clicked7():
    global turn
    if btn7['text']=='':
        if turn==1:
            turn=0
            btn7['text']='X'
            lb3['text']=("it's server Turn")
            s.send(str(7).encode('utf-8'))
            check()
        
def clicked8():
    global turn
    if btn8['text']=='':
        if turn==1:
            turn=0
            btn8['text']='X'
            lb3['text']=("it's server Turn")
            s.send(str(8).encode('utf-8'))
            check()
        
def clicked9():
    global turn
    if btn9['text']=='':
        if turn==1:
            turn=0
            btn9['text']='X'
            lb3['text']=("it's server Turn")
            s.send(str(9).encode('utf-8'))
            check()

btn1=tk.Button(window,text='',width=3,height=1,command=clicked1)
btn1.grid(row=2,column=1)
btn2=tk.Button(window,text='',width=3,height=1,command=clicked2)
btn2.grid(row=2,column=2)
btn3=tk.Button(window,text='',width=3,height=1,command=clicked3)
btn3.grid(row=2,column=3)
btn4=tk.Button(window,text='',width=3,height=1,command=clicked4)
btn4.grid(row=3,column=1)
btn5=tk.Button(window,text='',width=3,height=1,command=clicked5)
btn5.grid(row=3,column=2)
btn6=tk.Button(window,text='',width=3,height=1,command=clicked6)
btn6.grid(row=3,column=3)
btn7=tk.Button(window,text='',width=3,height=1,command=clicked7)
btn7.grid(row=4,column=1)
btn8=tk.Button(window,text='',width=3,height=1,command=clicked8)
btn8.grid(row=4,column=2)
btn9=tk.Button(window,text='',width=3,height=1,command=clicked9)
btn9.grid(row=4,column=3)        

flag=1
def check():
    global flag
    flag+=1
    b1=btn1['text']
    b2=btn2['text']
    b3=btn3['text']
    b4=btn4['text']
    b5=btn5['text']
    b6=btn6['text']
    b7=btn7['text']
    b8=btn8['text']
    b9=btn9['text']
    if flag<10:
        if(b1==b2 and b2==b3 and b1=='X'):
            win()
        if(b4==b5 and b5==b6 and b4=='X'):
            win()
        if(b7==b8 and b8==b9 and b7=='X'):
            win()
        if(b1==b4 and b4==b7 and b1=='X'):
            win()
        if(b2==b5 and b5==b8 and b2=='X'):
            win()
        if(b3==b6 and b6==b9 and b3=='X'):
            win()
        if(b1==b5 and b5==b9 and b1=='X'):
            win()
        if(b3==b5 and b5==b7 and b3=='X'):
            win()
    else:
        s.send(str(12).encode('utf-8'))
        messagebox.showinfo(message='Game Over No Winner')
        flag=1
        global turn
        turn=1
        btn1['text']=''
        btn2['text']=''
        btn3['text']=''
        btn4['text']=''
        btn5['text']=''
        btn6['text']=''
        btn7['text']=''
        btn8['text']=''
        btn9['text']=''
        
def win():
    s.send(str(11).encode('utf-8'))
    messagebox.showinfo(message='congratulations you are the winner')
    global flag
    flag=1
    global turn
    turn=1
    btn1['text']=''
    btn2['text']=''
    btn3['text']=''
    btn4['text']=''
    btn5['text']=''
    btn6['text']=''
    btn7['text']=''
    btn8['text']=''
    btn9['text']=''


def recv_func():
    while True:
         x=int(s.recv(2048).decode('utf-8'))
         global turn
         turn=1
         global flag
         flag+=1
         if x==1:
             btn1['text']='O'
             lb3['text']=("it's your turn")
         if x==2:
             btn2['text']='O'
             lb3['text']=("it's your turn")
         if x==3:
             btn3['text']='O'
             lb3['text']=("it's your turn")
         if x==4:
             btn4['text']='O'
             lb3['text']=("it's your turn")
         if x==5:
             btn5['text']='O'
             lb3['text']=("it's your turn")
         if x==6:
             btn6['text']='O'
             lb3['text']=("it's your turn")
         if x==7:
             btn7['text']='O'
             lb3['text']=("it's your turn")
         if x==8:
             btn8['text']='O'
             lb3['text']=("it's your turn")
         if x==9:
             btn9['text']='O'
             lb3['text']=("it's your turn")
         if x==11:
             messagebox.showinfo(message='Hard luck, Server is the winner')
             flag=1
             turn=1
             btn1['text']=''
             btn2['text']=''
             btn3['text']=''
             btn4['text']=''
             btn5['text']=''
             btn6['text']=''
             btn7['text']=''
             btn8['text']=''
             btn9['text']=''
         if x==12:
             messagebox.showinfo(message='Game Over No Winner')
             flag=1
             turn=1
             btn1['text']=''
             btn2['text']=''
             btn3['text']=''
             btn4['text']=''
             btn5['text']=''
             btn6['text']=''
             btn7['text']=''
             btn8['text']=''
             btn9['text']=''

rcv_thrd=th.Thread(target=recv_func)
rcv_thrd.start()
    
window.mainloop()
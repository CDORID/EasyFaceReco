# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 11:42:42 2019

@author: Romain
"""

import cv2
import os
import pandas as pd
from tkinter import * 


## function to create an input message as popup
def popup(message):
    root = Tk()
    
    root.title('Welcome !') 
    root.geometry('700x100+150+150')
    
    heading = Label(root, text = message, font=("arial", 14,'bold'), fg = "black").pack()
    
    name = StringVar()
    name.set('')
    entree = Entry(root, textvariable = name, justify = 'center', relief = 'flat', bg = 'lightgrey')
    entree.pack()
    root.lift()
    root.after(1, lambda: root.focus_force())
    entree.after(1,lambda:entree.focus_force())
    root.bind("<Return>", lambda x:root.destroy())    
    root.mainloop()
    
    new_name = name.get()
    
    return new_name

def popup_no_input(message):
    root = Tk()
    
    root.title('Welcome !') 
    root.geometry('700x100+150+150')
    
    heading = Label(root, text = message, font=("arial", 14,'bold'), fg = "black").pack()
    enter = Label(root, text = '\n Appuyer sur ENTREE pour continuer', font=("arial", 10,'bold'), fg = "grey").pack()
    root.lift()
    root.after(1, lambda: root.focus_force())
    root.bind("<Return>", lambda x:root.destroy())    
    root.mainloop()

## put the time you want the popup to stay (no idea of the measure unit, like 3/5 seconds)
def timed_popup(message,duration=5):
    root = Tk()
    
    root.title('Welcome ') 
    root.geometry('700x100+150+150')  
    heading = Label(root, text = message, font=("arial", 14,'bold'), fg = "black").pack()
    root.lift()
    root.after(1, lambda: root.focus_force())
    root.bind("<Return>", lambda x:root.destroy())
    duration = duration*1667 #lets try to put it in seconds 
    root.after(duration, lambda: root.destroy())
    root.mainloop()



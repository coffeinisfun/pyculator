import tkinter as tk
from tkinter import *
from tkinter import ttk

import math

expression = ""

def press(x):
    global expression
    expression = expression+str(x)

    equation.set(expression)

def equals():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)

        expression = ""
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set(expression)

def undo():
    global expression
    expression = expression[0:len(expression)-1]
    equation.set(expression)

if __name__ == '__main__':
# create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("Simple Calculator")

    # set the configuration of GUI window
    gui.geometry("300x180")

    equation = StringVar()

    expression_field = Entry(gui, textvariable=equation)

    expression_field.grid(columnspan=4, ipadx=70)


    for i in range(1,10):
        button = Button(gui, text = str(i), command= lambda i=i :press(i), height=1, width=3)

        button.grid(column = (i-1)%3, row = math.floor((i-1)/3) + 1)

    button0 = Button(gui, text = str(0), command= lambda :press(0), height=1, width=3)
    button0.grid(column = 1, row = 4)

    buttonPoint = Button(gui, text = ".", command= lambda :press("."), height=1, width=3)
    buttonPoint.grid(column = 2 , row = 4)

    buttonPlus = Button(gui, text = "+", command= lambda :press("+"), height=1, width=3)
    buttonPlus.grid(column = 3 , row = 1)

    buttonMinus = Button(gui, text = "-", command= lambda :press("-"), height=1, width=3)
    buttonMinus.grid(column = 3 , row = 2)

    buttonMult = Button(gui, text = "*", command= lambda :press("*"), height=1, width=3)
    buttonMult.grid(column = 3 , row = 3)

    buttonDiv = Button(gui, text = "/", command= lambda :press("/"), height=1, width=3)
    buttonDiv.grid(column = 3 , row = 4)

    buttonEqu = Button(gui, text = "=", command= lambda :equals())
    buttonEqu.grid(column = 0 , row = 5, columnspan = 2, ipadx = 50)

    buttonPlus = Button(gui, text = "BACK", command= lambda :undo(), height=1, width=3)
    buttonPlus.grid(column = 2 , row = 5)

    buttonPlus = Button(gui, text = "CLEAR", command= lambda :clear(), height=1, width=3)
    buttonPlus.grid(column = 3, row = 5)

     # start the GUI
    gui.mainloop()

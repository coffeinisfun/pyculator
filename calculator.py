import tkinter as tk
from tkinter import *
from tkinter import ttk

import math

expression = ""

def press(x):
    global expression
    expression = expression+str(x)

    equation.set(expression)



if __name__ == '__main__':
# create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("Simple Calculator")

    # set the configuration of GUI window
    gui.geometry("270x150")

    equation = StringVar()

    expression_field = Entry(gui, textvariable=equation)

    expression_field.grid(columnspan=4, ipadx=70)


    for i in range(1,10):
        button = Button(gui, text = str(i), command= lambda i=i :press(i))

        button.grid(column = (i-1)%3, row = math.floor((i-1)/3) + 1)

    button0 = Button(gui, text = str(0), command= lambda :press(0))

    button0.grid(column = 1, row = 4)

     # start the GUI
    gui.mainloop()

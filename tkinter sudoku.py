from tkinter import *
import tkinter
from tkinter import ttk
import numpy_test

window = tkinter.Tk()
def henk(bla):

    print(bla)


frm = tkinter.ttk.Frame(master=window, padding=20)
frm.grid(row=11, column=9, ipady=10, ipadx=10)
display = numpy_test.display()
for i in range(9):
    # if i == 3:
    #     continue
    for j in range(9):
        ttk.Button(master=frm, text=str(display[i][j]),
                   command=lambda position=i*9+j+1: henk(position)).grid(column=j, row=i, ipady=25, ipadx=0)
window.mainloop()
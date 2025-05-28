from tkinter import *
import tkinter
from tkinter import ttk
import numpy_test

posHolder = [[0, 0]]
window = tkinter.Tk()
def coords(position):
    posHolder[0] = position
    #buttonHolder[bla[0]][bla[1]].config(text="0")
    print(posHolder)
def numberPlacer(number):
    fieldButtonHolder[posHolder[0][0]][posHolder[0][1]].config(text=str(number+1))


frm = tkinter.ttk.Frame(master=window, padding=20)
frm.grid(row=11, column=9, ipady=10, ipadx=10) <---------- maak meer
display = numpy_test.display()
fieldButtonHolder = []
numberButtonHolder = []
for i in range(9):
    # if i == 3:
    #     continue
    fieldButtonHolder.append([])
    for j in range(9):
        x = 0
        y = 0
        btn = ttk.Button(master=frm, text=str(display[i][j]), width=2,
                         command=lambda position=[i, j]: coords(position))
        if i%2 == 0:
            y = 20
        if j%3 == 0:
            x = 20
        btn.grid(column=j, row=i, ipady=0, ipadx=0)
        fieldButtonHolder[i].append(btn)
separator = ttk.Separator(frm, orient="horizontal")
separator.place(relx=0, rely=0.5, relwidth=1, relheight=1)
for i in range(9):
    btn = ttk.Button(master=frm, text=str(i+1), width=2,
                     command=lambda number=i: numberPlacer(number))
    btn.grid(column=i, row=11, ipady=0, ipadx=0, pady=0)
    numberButtonHolder.append(btn)

window.mainloop()


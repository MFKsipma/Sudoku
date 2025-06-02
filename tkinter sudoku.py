from tkinter import *
import tkinter
from tkinter import ttk
import numpy_test

posHolder = [[0, 0]]

def coords(position):
    posHolder[0] = position
    #buttonHolder[bla[0]][bla[1]].config(text="0")
    print(posHolder)
def numberPlacer(number):
    fieldButtonHolder[posHolder[0][0]][posHolder[0][1]].config(text=str(number+1))

window = tkinter.Tk()
frm = tkinter.ttk.Frame(master=window, padding=20)
frm.grid(row=1, column=1, ipady=0, ipadx=0)
frm2 = tkinter.ttk.Frame(master=window, padding=20)
frm2.grid(row=2, column=1, ipady=0, ipadx=0)
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
#separator = ttk.Separator(frm, orient="horizontal")
#separator.place(relx=0, rely=0.5, relwidth=1, relheight=1)
for i in range(9):
    btn = ttk.Button(master=frm2, text=str(i+1), width=2,
                     command=lambda number=i: numberPlacer(number))
    btn.grid(column=i, row=11, ipady=0, ipadx=0, pady=0)
    numberButtonHolder.append(btn)


frm3 = tkinter.ttk.Frame(master=window, padding=20)
frm3.grid(row=3, column=1, ipady=0, ipadx=0)
henk1 = ttk.Button(master=frm3, text=str(1), width=2, command=print("henk"))
henk1.grid(column=1, row=1, ipady=0, ipadx=0, pady=0)
henk2 = ttk.Button(master=frm3, text=str(1), width=2, command=print("henk"))
henk2.grid(column=3, row=1, ipady=0, ipadx=0, pady=0)
ttk.Label(frm3, width=2).grid(column=2, row=0)
window.mainloop()


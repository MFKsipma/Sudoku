from tkinter import *
import tkinter
from tkinter import ttk
import numpy_test

posHolder = [[0, 0]]

display = numpy_test.display()

def coords(position):
    posHolder[0] = position
    #buttonHolder[bla[0]][bla[1]].config(text="0")
    print(posHolder)
    print(display)
def numberPlacer(number):
    fieldButtonHolder[posHolder[0][0]][posHolder[0][1]].config(text=number if number != 0 else " ")
    display[posHolder[0][0], posHolder[0][1]] = number
    print("hoi")
    print(number)

window = tkinter.Tk()
frm = tkinter.ttk.Frame(master=window, padding=20)
frm.grid(row=1, column=1, ipady=0, ipadx=0)
frm2 = tkinter.ttk.Frame(master=window, padding=20)
frm2.grid(row=2, column=1, ipady=0, ipadx=0)

fieldButtonHolder = []
numberButtonHolder = []
for i in range(9):
    # if i == 3:
    #     continue
    fieldButtonHolder.append([])
    for j in range(9):
        #change a 0 into a " "
        buttonString = display[i][j]
        if buttonString == 0:
            buttonString = " "

        btn = ttk.Button(master=frm, text=str(buttonString), width=2,
                         command=lambda position=[i, j]: coords(position))

        btn.grid(column=j + j//3, row=i + i//3, ipady=0, ipadx=0)
        fieldButtonHolder[i].append(btn)

ttk.Label(frm, width=1).grid(column=3, row=0)
ttk.Label(frm, width=1).grid(column=7, row=0)
ttk.Label(frm, width=1).grid(column=0, row=3)
ttk.Label(frm, width=1).grid(column=0, row=7)

for i in range(10):
    btn = ttk.Button(master=frm2, text=str(i), width=2,
                     command=lambda number=i: numberPlacer(number))
    btn.grid(column=i, row=11, ipady=0, ipadx=0, pady=0)
    numberButtonHolder.append(btn)

#btn = ttk.Button(master=frm2, text=str(i+1), width=2, command=lambda number=i: numberPlacer(number))

# frm3 = tkinter.ttk.Frame(master=window, padding=20)
# frm3.grid(row=3, column=1, ipady=0, ipadx=0)
# henk1 = ttk.Button(master=frm3, text=str(1), width=2, command=print("henk"))
# henk1.grid(column=1, row=1, ipady=0, ipadx=0, pady=0)
# henk2 = ttk.Button(master=frm3, text=str(1), width=2, command=print("henk"))
# henk2.grid(column=3, row=1, ipady=0, ipadx=0, pady=0)
# ttk.Label(frm3, width=1).grid(column=2, row=0)
window.mainloop()


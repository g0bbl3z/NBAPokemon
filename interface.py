from tkinter import *

def nothing():
    return

master = Tk()
Label(master, text="Weight (KG)").grid(row=0)
Label(master, text="Height (m)").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Calculate', command=nothing).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )

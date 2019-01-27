import tkinter as tk
from Pokemon import getPokemonAdjusted, getPokemon

def getPokemans():
    weight = float(e1.get())/2.205
    height = float(e2.get())/39.37

    if choice.get() == 2:
        getPokemon(weight, height)
    elif choice.get() == 1:
        getPokemonAdjusted(weight,height)
    return

master = tk.Tk()

choice = tk.IntVar()
tk.Label(master,
        text="""Choose a Mode:""",
        justify = tk.LEFT,
        padx = 20).grid(row=0)

tk.Radiobutton(master,
              text="Relative Comparison",
              padx = 20,
              variable=choice,
              value=1).grid(row=4)
tk.Radiobutton(master,
              text="Direct Comparison",
              padx = 20,
              variable=choice,
              value=2).grid(row=3)


tk.Label(master, text="Weight (lb)").grid(row=1)
tk.Label(master, text="Height (in)").grid(row=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)

tk.Button(master, text='Quit', command=master.quit).grid(row=4, column=1, sticky=tk.W, pady=4)
tk.Button(master, text='Calculate', command=getPokemans).grid(row=3, column=1, sticky=tk.W, pady=4)

tk.mainloop()

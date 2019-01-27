import tkinter as tk
from PokemonChoose import getPokemonAdjusted, getPokemon

approvedPokemon = []
dynamic_sprites = []

def getPokemans():

    if (e3.get() == ""):
        weight = float(e1.get())/2.205
        height = float(e2.get())/39.37

        if choice.get() == 2:
            approvedPokemon = getPokemon(weight, height)
        elif choice.get() == 1:
            approvedPokemon = getPokemonAdjusted(weight,height)
    elif (e3.get() != ""):
        #Do all the stuff regarding the nba stats, call the zeke method and allself.
        print()

    i = 0
    while i < len(approvedPokemon):
        tk.Label(master, text = approvedPokemon[i]).grid(row=7+i,column=0)
        sprite = tk.PhotoImage(file=("sprites/"+approvedPokemon[i]+".png"))
        dynamic_sprites.append(sprite)
        tk.Label(master, image=dynamic_sprites[i]).grid(row=7+i,column=1)
        i+=1

    # tk.Label(master, text=approvedPokemon).grid(row = 5)

    return

master = tk.Tk()

choice = tk.IntVar()
tk.Label(master,
        text="""Enter your weight and height or Enter the name of an NBA Player!""",
        justify = tk.LEFT,
        padx = 20).grid(row=0)

tk.Radiobutton(master,
              text="Relative Comparison",
              padx = 20,
              variable=choice,
              value=1).grid(row=5)
tk.Radiobutton(master,
              text="Direct Comparison",
              padx = 20,
              variable=choice,
              value=2).grid(row=4)

logo = tk.PhotoImage(file="pokeball_sprite.png")
logo = logo.subsample(8)

logo2 = tk.PhotoImage(file="nba_sprite.png")
logo2 = logo2.subsample(8)

logoImg = tk.Label(master, image=logo).grid(row=1, column=2)
logoImg2 = tk.Label(master, image=logo2).grid(row=3, column=2)

tk.Label(master, text="Weight (lb)").grid(row=1)
tk.Label(master, text="Height (in)").grid(row=2)
tk.Label(master, text="Name of NBA Player:").grid(row=3)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)

tk.Button(master, text='Quit', command=master.quit).grid(row=5, column=1, sticky=tk.W, pady=4)
tk.Button(master, text='Calculate', command=getPokemans).grid(row=4, column=1, sticky=tk.W, pady=4)

tk.mainloop()

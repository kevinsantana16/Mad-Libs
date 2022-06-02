from tkinter import * 
from tkinter import ttk
import main



root = Tk()
root.title("Mad labis")

tela2= ttk.Frame(root)
tela = ttk.Frame(root, padding="3 3 12 12")
tela.grid(column=0, row=0, sticky=(N, W, E, S))
tela2.grid(column=0, row=7, sticky=(N, W, E, S))
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)



sub = StringVar()
name_entry = Entry(tela, textvariable=sub).grid(column=2, row=4, sticky=(W, E))
name = Label(tela, text="name").grid(column=1, row=4, sticky=W)


anim = StringVar()
animal_entry= Entry(tela, textvariable=anim).grid(column=2, row=5, sticky=(W, E))
animal = Label(tela, text="animal").grid(column=1,row=5, sticky=W)

col = StringVar()
col_entry = Entry(tela, textvariable=col).grid(column=2, row=6, sticky=(W, E))
cor = Label(tela, text="cor").grid(column=1, row=6, sticky=W)

opcao = StringVar()

name_his = Label(tela, text="escolha uma opção").grid(column=1, row=1, sticky=W)

one = ttk.Radiobutton(tela, text="♧", variable=opcao, value="primeiro").grid(column=2, row=1, sticky=W)

two = ttk.Radiobutton(tela, text="♡", variable=opcao, value="segundo").grid(column=2, row=2, sticky=W)

three = ttk.Radiobutton(tela, text="◇", variable=opcao, value="terceiro").grid(column=2, row=3, sticky=W)

m = historia(opcao, name, anim, col)
ok = Button(tela, text="iniciar", command=m).grid(column=1, row=7, sticky=W)

tee = Label(tela2, ).grid(column=1, row=8, sticky=W)



root.mainloop()
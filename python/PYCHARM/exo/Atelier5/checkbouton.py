from tkinter import *
def maj():
	if v.get() == 1: # la case est cochée
		label.configure(text="JOUR")
	elif v.get() == 0: # la case est décochée
		label.configure(text="NUIT")
top = Tk()
v = IntVar()
label = Label(top, text = " ");
bouton= Checkbutton(top, text="Allume",
variable = v, command = maj)
bouton.select() # deselect() pour décocher la case
label.pack(); bouton.pack()
top.mainloop()
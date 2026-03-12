from tkinter import *
def bouton():
    msg = "choix: " + str(v.get())
    l1.configure(text=msg)
root = Tk()
v = IntVar()
r1 = Radiobutton( root, text="Bouton 1",
    variable=v, value=1, command=bouton)
r2 = Radiobutton( root, text="Bouton 2",
    variable=v, value=2, command=bouton)
l1 = Label(root)
r1.pack(); r2.pack(); l1.pack()
root.mainloop()
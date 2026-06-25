from tkinter import *
from tkinter.messagebox import *
def msgbox():
	reponse = askquestion("titre","Voulez-vous quitter?")
	if reponse == "yes":
		showinfo("titre"," Au revoir ! ")
		root.destroy()
root = Tk()
widget = Button(root, text="ByeBye", command=msgbox)
widget.pack()
root.mainloop()
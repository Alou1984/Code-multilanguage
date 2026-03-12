from tkinter import *
def valide():
    try:
        i = l1.curselection()[0]; var = l1.get(i)
        label.configure( text = var )
    except: pass
top = Tk()
l1 = Listbox(top, width = 15, height = 5 );
ferme = ["Chat","Chien","Cochon","Poule","Mouton","Cheval"]
for animal in ferme:
    l1.insert(END, animal)
label = Label(top, text = " ");
bouton = Button(top, text = " OK ", command = valide)
l1.pack(); label.pack(); bouton.pack()
top.mainloop()
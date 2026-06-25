from tkinter import *
def valide():
    try:
        i = lstbox.curselection()[0]
        var = lstbox.get(i)
        label.configure( text = var )
    except: pass
top = Tk()
fr = Frame(top)
scrol = Scrollbar(fr, orient="vertical")
lstbox = Listbox(fr, width = 15, height = 5, yscrollcommand=scrol.set )
ferme = ["Chat","Chien","Cochon","Poule","Mouton","Cheval"]
for animal in ferme:
    lstbox.insert(END, animal)
scrol.config(command=lstbox.yview)
label = Label(top, text = " ");
bouton = Button(top, text = " OK ", command = valide)
fr.pack()
lstbox.pack(side=LEFT)
label.pack()
bouton.pack()
scrol.pack(side=RIGHT, fill=Y)
top.mainloop()
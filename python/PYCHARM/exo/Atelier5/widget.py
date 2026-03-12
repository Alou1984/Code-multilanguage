import tkinter
root = tkinter.Tk()
lab1 = tkinter.Label(root, text="Salut",
font=('Times','30','bold'))
lab2 = tkinter.Label(root, text="Coucou", bg="yellow")
lab3 = tkinter.Label(root, text="Bye",
heigh=10, width=20, relief="sunken" )
print("couleur du fond:", lab2.cget('bg'))
lab2.configure(fg='red')
lab1.pack(); lab2.pack(); lab3.pack()
root.mainloop()
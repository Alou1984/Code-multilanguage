rom tkinter import *
root = Tk()
fra1 = Frame(root)
lab1 = Label(root, text="UN ",relief="ridge")
lab2 = Label(root, text="DEUX ",relief="ridge")
lab3 = Label(root, text="TROIS ",relief="ridge")
lab4 = Label(root, text="QUATRE",relief="ridge")
fra1.pack()
lab1.pack(side='top', anchor='n')
lab4.pack(side='bottom', anchor='s',
    padx=20, pady=20, expand=1, fill='both')
lab2.pack(side='left' )
lab3.pack(side='right' )
root.mainloop()
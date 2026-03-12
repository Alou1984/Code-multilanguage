from tkinter import *
root = Tk()
root.geometry("170x200+30+40")
lab1 = Label(root, text="100x50+10+10", relief="ridge")
lab2 = Label(root, text="120x80+10+100", relief="ridge")
lab1.place(width=100,height=50,x=10,y=10)
lab2.place(width=120,height=80,x=10,y=100)
root.mainloop()
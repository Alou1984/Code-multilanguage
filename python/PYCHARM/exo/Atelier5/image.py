from tkinter import *
win = Tk();
img = PhotoImage(file="python.png") # Gif ou PNG
can = Canvas(win)
can.pack(fill=BOTH)
can.config(width=img.width(), height=img.height())
can.create_image(2,2, image=img, anchor=NW)
win.mainloop()
from tkinter import *
canvas = Canvas(width=650, height=300, bg='yellow')
canvas.pack()
canvas.create_line(100, 100, 200, 200)
canvas.create_oval(30, 30, 100, 200, width=1, fill='blue')
canvas.create_arc(200, 200, 300, 300, width=5, fill='red')
canvas.create_rectangle( 200, 200, 300, 300,
width=10, fill='green')
photo = PhotoImage(file="monty.gif")canvas.create_image(
250, 0, image=photo, anchor=NW)
widget = Label(canvas, text='salut', fg='white', bg='black')
widget.pack()
canvas.create_window(100, 100, window=widget)
canvas.create_text(100, 280, text='coucou')
mainloop()
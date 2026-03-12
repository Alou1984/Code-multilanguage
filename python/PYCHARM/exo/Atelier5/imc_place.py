from tkinter import *

def message(IMC):
    if IMC < 16.5:
        msg = "Vous êtes en état de dénutrition"
    elif IMC >= 16.5 and IMC < 18.5:
        msg = "Vous êtes maigre"
    elif IMC >= 18.5 and IMC < 25:
        msg = "Votre poids est normal"
    elif IMC >= 25 and IMC < 30:
        msg = "Vous êtes en surpoids"
    elif IMC >= 30 and IMC < 35:
        msg = "Vous êtes en état d'obésité modérée"
    elif IMC >= 35 and IMC < 40:
        msg = "Vous êtes en état d'obésité sévère"
    elif IMC >= 40:
        msg = "Vous êtes en état d'obésité morbide"
    else:
        msg = " "
    return msg
    
def calcul():
    ch1 = widSaisiePoids.get()
    ch2 = widSaisieTaille.get()
    if ch1.isdigit() and ch2.isdigit():
        P = int(ch1) ; T = int(ch2)
        IMC = P / ((T/100) ** 2)
        result = "%5.2f" % (IMC)
        widAfficheIMC.configure(text=result)
        widAfficheMSG.configure(text=message(IMC) )
root = Tk()
root.resizable(False,False)
root.geometry("600x500+100+100")

laPolice= ('Times','20','roman')
widPromptPoids = Label(root, text="Poids (en kg) ? ",
    font=laPolice)
widSaisiePoids = Entry(root, width=20, font=laPolice)
widPromptTaille = Label(root, text="Taille (en cm) ? ",
    font=laPolice)
widSaisieTaille = Entry(root, width=20, font=laPolice)
widCalcul = Button(root, text="IMC", command=calcul,
font=laPolice)
widAfficheIMC = Label(root, text=" ", font=laPolice)
widAfficheMSG = Label(root, text=" ", font=laPolice)
widPromptPoids.place(width=200,height=50,x=20,y=20)
widSaisiePoids.place(width=150,height=50,x=300,y=20)
widPromptTaille.place(width=200,height=50,x=20,y=100)
widSaisieTaille.place(width=150,height=50,x=300,y=100)
widCalcul.place(width=100,height=50,x=20,y=200)
widAfficheIMC.place(width=200,height=50,x=200,y=200)
widAfficheMSG.place(width=400,height=50,x=20,y=300)
root.mainloop()
from tkinter import *
from game import Game
# perssonaliser la fenetre

window = Tk()
window.title("backrooms")
window.minsize(850, 720)
window.config(background='#C8AD7F')
# ajouter une frame
frame = Frame(window, bg='#C8AD7F')
# ajouter un premier texte
label_title = Label(frame,text="bienvenue aux backrooms",font=("Courrier", 40),bg='#C8AD7F',fg='white')
label_title.pack()

# ajouter un bouton
Start = Button(frame, text="commencer", font=("Courrier", 25), bg='white', fg='#C8AD7F')
Start.pack(pady=25,fill=X)
# afficher la fenetre
frame.pack(expand= YES)

window.mainloop()



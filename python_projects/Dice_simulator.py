import random
from tkinter import*
#first ui for project
root = Tk()
root.title("Dice simulator Kajal")
root.geometry("500x300")
face = Label(root,font=("arial",60))
def s():
    number=['\u2680','\u2681','\u2681','\u2682','\u2683','\u2684']
    face.config(text=f'{random.choice(number)}')
    face.pack()

b1 = Button(root, text=" Please roll", command=s)
b1.place(x=250, y=150)

root.mainloop()

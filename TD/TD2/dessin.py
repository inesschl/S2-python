import tkinter as tk
import random
import numpy as np

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400


def creer_cercle():
    '''fonction qui cree un cercle'''
    x = random.randint(50, w - 50)
    y = random.randint(50, h - 50)
    canvas.create_oval(x - 50, y + 50, x + 50, y - 50, fill=color)


def creer_carre():
    x = random.randint(50, w - 50)
    y = random.randint(50, h - 50)
    canvas.create_rectangle(x - 50, y + 50, x + 50, y - 50, fill=color)


def creer_croix():
    x = random.randint(50, w - 50)
    y = random.randint(50, h - 50)
    canvas.create_line(x - 50, y, x + 50, y, fill=color, width=15)
    canvas.create_line(x, y - 50, x, y + 50, fill=color, width=15)


def choix_couleur():
    global color
    color = input("Quel couleur voulez vous?")


def les_objets():
    global objet
    objet.append


def undo():



color = "blue"
objet = np.empty()
root = tk.Tk()
w = 300
h = 300

root.title("mon dessin")
canvas = tk.Canvas(root, width=w, height=h, bg=color)
boutton_couleur = tk.Button(root, text="Choisir une couleur", command=choix_couleur)
boutton_cercle = tk.Button(root, text="cercle", command=creer_cercle)
boutton_carre = tk.Button(root, text="carre", command=creer_carre)
button_croix = tk.Button(root, text="croix", command=creer_croix)
button_undo = tk.Button(root, text="undo", command=undo)

canvas.grid(row=1, rowspan=3, column=1)
boutton_couleur.grid(row=0, column=1)
boutton_cercle.grid(row=1, column=0)
boutton_carre.grid(row=2, column=0)
button_croix.grid(row=3, column=0)
button_undo.grid(row=0, column=2)

root.mainloop()

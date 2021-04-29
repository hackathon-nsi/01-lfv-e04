from tkinter import *
from adam_fonc import *
from Projet_Hackathon_Pyxelator import *
from PIL import Image, ImageEnhance

def adam_2():
    import urllib.request
    im = Image.open("Elon_Musk.jpg")
    print(im.size)
    print(adam())

def arian_2():
    im = Image.open("Tiger_Woods.jpg")
    en = ImageEnhance.Color(im)
    im = en.enhance(0.0)
    im_new = Image.open("Elon_Musk.jpg")
    im_new = im_new.convert("RGB")
    en = ImageEnhance.Contrast(im_new)
    im_new = en.enhance(0.7)
    datas = im_new.getdata()
    new_image_data = []
    for item in datas:
        if item[0] in list(range(190, 256)):
            new_image_data.append((232, 37, 37))
        else:
            new_image_data.append(item)
    im_new.putdata(new_image_data)
    print(im.format, im.size, im.mode)
    width, height = im.size
    print(arian())

fenetre = Tk() 	# objet fenetre à partir de la classe Tk() fenetre principale
fenetre.minsize(200,200)
# titre = Objet de classe Label, argument fenetre, fenetre = objet parent de l'objet titre
titre = Label(fenetre, text="Editeur d'image",fg='blue', bg="yellow")
alerte=Label(fenetre, text="")

bouton_option_1=Button(fenetre, text="quadrillage couleurs inversé",fg="white",bg="red",bd=2,command=adam_2)
bouton_option_2=Button(fenetre, text="quadrillage multicolor",fg="white",bg="red",bd=2,command=arian_2)
bouton_fermer=Button(fenetre, text="Quitter",command=fenetre.destroy)

# Interface graphique n'existe pas, représentation interne des objets
# Méthode .pack() définit les paramètres géométriques au gestionnaire de position
titre.pack()
alerte.pack()
bouton_option_1.pack(side=LEFT)
bouton_option_2.pack(side=RIGHT)
bouton_fermer.pack(side=BOTTOM)

# Représentation géométrique interne mais pas visible
# Methode mainloop tourne en boucle
# gestionnaire d'événement + affichage fenetre
fenetre.mainloop()
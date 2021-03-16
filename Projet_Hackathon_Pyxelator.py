from PIL import Image
#from IPython.display import display
import urllib.request
#from adam import *
#from aron import *

# ouvrir une image hébergée sur internet
#im = Image.open(urllib.request.urlopen('https://raw.githubusercontent.com/hackathon-nsi/h7n-nsi-01/main/images/washington.bmp'))
im2 = Image.open("Tiger_Woods.jpg")

# créer une nouvelle image vide
# le deuxième argument représente la taille de l'image et le troisième argument (optionnel) la couleur de remplissage au format RVB
#im_new = Image.new("RGB", (900,500), (26, 158, 214))
im_new = Image.open("Elon_Musk.jpg")

# informations sur l'image
print(im2.format, im2.size, im2.mode) # im2 et no im parce que im = l'image du web

# taille de l'image
width, height = im2.size

#n = int(input("Quelle taille de pixels voulez-vous? "))

# valeurs du pixel de coordonnées x, y (l'origine (0, 0) est en haut à gauche)
##pixel = im.getpixel((x, y))

#           0-100 = première ligne
def arian():
    for y in range(0,100):
        for x in range(0,100):
            pixel = im2.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    for y in range(0,100):
        for x in range(200,300):
            pixel = im2.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    for y in range(0,100):
        for x in range(400,500):
            pixel = im2.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    for y in range(0,100):
        for x in range(600,700):
            pixel = im2.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    for y in range(0,100):
        for x in range(800,900):
            pixel = im2.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    #          100-200 = deuxième ligne

    for y in range(100,200):
        for x in range(100,200):
            pixel = im2.getpixel((x , y))
            im_new.putpixel((x , y),pixel)

    for y in range(100,200):
        for x in range(700,800):
            pixel = im2.getpixel((x , y))
            im_new.putpixel((x , y),pixel)

    for y in range(100,200):
        for x in range(300,400):
            pixel = im2.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    for y in range(100,200):
        for x in range(500,600):
            pixel = im2.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    #          200-300 = troisième ligne

    for y in range(200, 300):
        for x in range(0, 100):
            pixel = im2.getpixel((x, y))
            im_new.putpixel((x, y), pixel)

    for y in range(200, 300):
        for x in range(200, 300):
            pixel = im2.getpixel((x, y))
            im_new.putpixel((x, y), pixel)

    for y in range(200, 300):
        for x in range(400, 500):
            pixel = im2.getpixel((x, y))
            im_new.putpixel((x, y), pixel)

    for y in range(200, 300):
        for x in range(600, 700):
            pixel = im2.getpixel((x, y))
            im_new.putpixel((x, y), pixel)

    for y in range(200, 300):
        for x in range(800, 900):
            pixel = im2.getpixel((x, y))
            im_new.putpixel((x, y), pixel)

    #          300-400 = quatrième ligne

    for y in range(300,400):
        for x in range(100,200):
            pixel = im2.getpixel((x , y))
            im_new.putpixel((x , y),pixel)

    for y in range(300,400):
        for x in range(300,400):
            pixel = im2.getpixel((x , y))
            im_new.putpixel((x , y),pixel)

    for y in range(300,400):
        for x in range(500,600):
            pixel = im2.getpixel((x , y))
            im_new.putpixel((x , y),pixel)

    for y in range(300,400):
        for x in range(700,800):
            pixel = im2.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    #          400-500 = cinquième ligne

    for y in range(400,500):
        for x in range(0,100):
            pixel = im2.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    for y in range(400,500):
        for x in range(200,300):
            pixel = im2.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    for y in range(400,500):
        for x in range(400,500):
            pixel = im2.getpixel((x , y))
            im_new.putpixel((x , y),pixel)

    for y in range(400,500):
        for x in range(600,700):
            pixel = im2.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    for y in range(400,500):
        for x in range(800,900):
            pixel = im2.getpixel((x, y))
            im_new.putpixel((x,y),pixel)


    ### valeurs des couleurs rouge, vert, bleu
    ##p_rouge = pixel[0]
    ##p_vert =  pixel[1]
    ##p_bleu =  pixel[2]

    # modification du pixel de coordonnées x, y


    # affichage de l'image
    ##display(im)
    im_new.show()

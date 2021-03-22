from PIL import Image
from IPython.display import display
import urllib.request

# ouvrir une image hébergée sur internet
im = Image.open(urllib.request.urlopen('https://raw.githubusercontent.com/hackathon-nsi/h7n-nsi-01/main/images/washington.bmp'))

# créer une nouvelle image vide
# le deuxième argument représente la taille de l'image et le troisième argument (optionnel) la couleur de remplissage au format RVB

# informations sur l'image
print(im.format, im.size, im.mode)

# taille de l'image
width, height = im.size

# valeurs du pixel de coordonnées x, y (l'origine (0, 0) est en haut à gauche)

for x in range(300 ):
     for y in range(400 ):
         pixel = im.getpixel((x, y,))


# valeurs des couleurs rouge, vert, bleu
         p_rouge = 255-int(pixel[0])
         p_vert =  255-int(pixel[1])
         p_bleu =  255-int(pixel[2])

# modification du pixel de coordonnées x, y
         p_rouge= 0
         im.putpixel((x,y),(p_rouge,p_vert,p_bleu))

# affichage de l'image
im.save("sortie.png")
im.show()
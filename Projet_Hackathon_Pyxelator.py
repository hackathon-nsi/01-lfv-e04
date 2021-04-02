from PIL import Image, ImageEnhance # le module ImageEnhance a pour classes: Color, Contrast, Brightness et Sharpness
#from adam import *
#from aron import *

# ouvre la première image
im = Image.open("Tiger_Woods.jpg")

# transforme l´image en noir et blanc
en = ImageEnhance.Color(im)
im = en.enhance(0.0)

# ouvre une deuxième image et change le contraste
im_new = Image.open("Elon_Musk.jpg")
im_new = im_new.convert("RGB")
en = ImageEnhance.Contrast(im_new)
im_new = en.enhance(0.7) # (0.0) = tout en gris et (1.0) = image sans effet

datas = im_new.getdata()

# change les couleurs de l´image
new_image_data = []
for item in datas:
    if item[0] in list(range(190, 256)):
        new_image_data.append((232, 37, 37)) # la couleur utilisé (rouge)
    else:
        new_image_data.append(item)

# la nouvelle image
im_new.putdata(new_image_data)

# informations sur l'image
print(im.format, im.size, im.mode)

# taille de l'image
width, height = im.size

#           0-100 = première ligne
def arian():
    for y in range(0,100):
        for x in range(0,100):
            pixel = im.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    for y in range(0,100):
        for x in range(200,300):
            pixel = im.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    for y in range(0,100):
        for x in range(400,500):
            pixel = im.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    for y in range(0,100):
        for x in range(600,700):
            pixel = im.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    for y in range(0,100):
        for x in range(800,900):
            pixel = im.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    #          100-200 = deuxième ligne

    for y in range(100,200):
        for x in range(100,200):
            pixel = im.getpixel((x , y))
            im_new.putpixel((x , y),pixel)

    for y in range(100,200):
        for x in range(700,800):
            pixel = im.getpixel((x , y))
            im_new.putpixel((x , y),pixel)

    for y in range(100,200):
        for x in range(300,400):
            pixel = im.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    for y in range(100,200):
        for x in range(500,600):
            pixel = im.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    #          200-300 = troisième ligne

    for y in range(200, 300):
        for x in range(0, 100):
            pixel = im.getpixel((x, y))
            im_new.putpixel((x, y), pixel)

    for y in range(200, 300):
        for x in range(200, 300):
            pixel = im.getpixel((x, y))
            im_new.putpixel((x, y), pixel)

    for y in range(200, 300):
        for x in range(400, 500):
            pixel = im.getpixel((x, y))
            im_new.putpixel((x, y), pixel)

    for y in range(200, 300):
        for x in range(600, 700):
            pixel = im.getpixel((x, y))
            im_new.putpixel((x, y), pixel)

    for y in range(200, 300):
        for x in range(800, 900):
            pixel = im.getpixel((x, y))
            im_new.putpixel((x, y), pixel)

    #          300-400 = quatrième ligne

    for y in range(300,400):
        for x in range(100,200):
            pixel = im.getpixel((x , y))
            im_new.putpixel((x , y),pixel)

    for y in range(300,400):
        for x in range(300,400):
            pixel = im.getpixel((x , y))
            im_new.putpixel((x , y),pixel)

    for y in range(300,400):
        for x in range(500,600):
            pixel = im.getpixel((x , y))
            im_new.putpixel((x , y),pixel)

    for y in range(300,400):
        for x in range(700,800):
            pixel = im.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    #          400-500 = cinquième ligne

    for y in range(400,500):
        for x in range(0,100):
            pixel = im.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    for y in range(400,500):
        for x in range(200,300):
            pixel = im.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    for y in range(400,500):
        for x in range(400,500):
            pixel = im.getpixel((x , y))
            im_new.putpixel((x , y),pixel)

    for y in range(400,500):
        for x in range(600,700):
            pixel = im.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    for y in range(400,500):
        for x in range(800,900):
            pixel = im.getpixel((x, y))
            im_new.putpixel((x,y),pixel)

    im_new.show()

print(arian())       # seulement pour mon logiciel qui exécute les fonctions de cette manière
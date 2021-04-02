from PIL import Image, ImageEnhance
#from adam import *
#from aron import *

# ouvrir une image hébergée sur internet
im2 = Image.open("Tiger_Woods.jpg")

# transforme l´image en noir et blanc
en = ImageEnhance.Color(im2)
im2 = en.enhance(0.0)

# créer une nouvelle image vide
im_new = Image.open("Elon_Musk.jpg")
im_new = im_new.convert("RGB")

datas = im_new.getdata()

# change les couleurs de l´image
new_image_data = []
for item in datas:
    if item[0] in list(range(190, 256)):
        new_image_data.append((232, 37, 37))
    else:
        new_image_data.append(item)

# la nouvelle image
im_new.putdata(new_image_data)

# informations sur l'image
print(im2.format, im2.size, im2.mode)

# taille de l'image
width, height = im2.size

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

    im_new.show()

print(arian())
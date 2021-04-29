from PIL import Image, ImageEnhance  # le module ImageEnhance a pour classes: Color, Contrast, Brightness et Sharpness

# from adam import *
# from aron import *

# ouvre la première image
im = Image.open("Tiger_Woods.jpg")

# transforme l´image en noir et blanc
en = ImageEnhance.Color(im)
im = en.enhance(0.0)

# ouvre une deuxième image et change le contraste
im_new = Image.open("Elon_Musk.jpg")
im_new = im_new.convert("RGB")
en = ImageEnhance.Contrast(im_new)
im_new = en.enhance(0.7)  # (0.0) = tout en gris et (1.0) = image sans effet

datas = im_new.getdata()

# change les couleurs de l´image
new_image_data = []
for item in datas:
    if item[0] in list(range(190, 256)):
        new_image_data.append((232, 37, 37))  # la couleur utilisé (rouge)
    else:
        new_image_data.append(item)

# la nouvelle image
im_new.putdata(new_image_data)

# informations sur l'image
print(im.format, im.size, im.mode)

# taille de l'image
width, height = im.size


def arian():
    for i in range(5):
        for c in range(3):  # lignes 1,3 et 5
            for x in range(0 + i * 200, 100 + i * 200):
                for y in range(0 + c * 200, 100 + c * 200):
                    pixel = im.getpixel((x, y))
                    im_new.putpixel((x, y), pixel)

    for i in range(4):
        for c in range(2):  # lignes 2 et 4
            for x in range(100 + i * 200, 200 + i * 200):
                for y in range(100 + c * 200, 200 + c * 200):
                    pixel = im.getpixel((x, y))
                    im_new.putpixel((x, y), pixel)
    im_new.show()


print(arian())

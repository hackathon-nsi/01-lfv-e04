#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Adam Atwa
#
# Created:     17/04/2021
# Copyright:   (c) Adam Atwa 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

choix=int(input("Quel modification voulez-vous?"))

if choix==1:
    from fonction_adam import*
    #programme d'adam viendra ici
elif choix==2:
    from PIL import Image, ImageEnhance

    # ouvre la première image

    im = Image.open("Tiger_Woods.jpg")

    # transforme l´image en noir et blanc

    en = ImageEnhance.Color(im)
    im = en.enhance(0.0)

    # ouvre une deuxième image et change le contraste

    im_new = Image.open("Elon_Musk.jpg")
    im_new = im_new.convert("RGB")
    en = ImageEnhance.Contrast(im_new)
    im_new = en.enhance(0.7)    # (0.0) = tout en gris et (1.0) = image sans effet
    datas = im_new.getdata()

    # change les couleurs de l´image

    new_image_data = []
    for item in datas:
    if item[0] in list(range(190, 256)):
    new_image_data.append((232, 37, 37)) #   la couleur utilisé (rouge)
    else:
    new_image_data.append(item)

elif choix==3:
    from fonction_arian import*
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

    arian()

elif choix==4:
    from fonction_arian import*

    from PIL import Image, ImageEnhance # le module ImageEnhance a pour classes: Color, Contrast, Brightness et Sharpness

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

arian()
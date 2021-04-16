from PIL import Image
from IPython.display import display
import urllib.request

# ouvrir une image hébergée sur internet
im_aron = Image.open(urllib.request.urlopen('https://i.pinimg.com/originals/3e/84/c6/3e84c651e14d70e34fa5c411cb40713b.jpg'))
im_aron.show()

#im_blank = Image.new ("RGB", (500,300), (0,0,0))

# taille de l'image
width, height = im.size
width = im.width
height = im.height

# informations sur l'image
print(im.format, im.size, im.mode)


#remplacement de parties de l'image avec des carrés blancs
for x in range(50,55):
    for y in range(50,55):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(100,105):
    for y in range(50,55):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(150,155):
    for y in range(50,55):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(200,205):
    for y in range(50,55):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(250,255):
    for y in range(50,55):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(300,305):
    for y in range(50,55):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(350,355):
    for y in range(50,55):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(400,405):
    for y in range(50,55):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(450,455):
    for y in range(50,55):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

#second row

for x in range(50,55):
    for y in range(100,105):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(100,105):
    for y in range(100,105):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(150,155):
    for y in range(100,105):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(200,205):
    for y in range(100,105):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(250,255):
    for y in range(100,105):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(300,305):
    for y in range(100,105):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(350,355):
    for y in range(100,105):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(400,405):
    for y in range(100,105):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(450,455):
    for y in range(100,105):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

#third row

for x in range(50,55):
    for y in range(150,155):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(100,105):
    for y in range(150,155):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(150,155):
    for y in range(150,155):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(200,205):
    for y in range(150,155):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(250,255):
    for y in range(150,155):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(300,305):
    for y in range(150,155):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(350,355):
    for y in range(150,155):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(400,405):
    for y in range(150,155):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(450,455):
    for y in range(150,155):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

#fourth row

for x in range(50,55):
    for y in range(200,205):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(100,105):
    for y in range(200,205):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(150,155):
    for y in range(200,205):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(200,205):
    for y in range(200,205):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(250,255):
    for y in range(200,205):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(300,305):
    for y in range(200,205):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(350,355):
    for y in range(200,205):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(400,405):
    for y in range(200,205):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(450,455):
    for y in range(200,205):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

#fifth row

for x in range(50,55):
    for y in range(250,255):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(100,105):
    for y in range(250,255):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(150,155):
    for y in range(250,255):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(200,205):
    for y in range(250,255):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(250,255):
    for y in range(250,255):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(300,305):
    for y in range(250,255):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(350,355):
    for y in range(250,255):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(400,405):
    for y in range(250,255):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))

for x in range(450,455):
    for y in range(250,255):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(0,0,0))





im_aron.save('aron_image.png')
im_aron.show()
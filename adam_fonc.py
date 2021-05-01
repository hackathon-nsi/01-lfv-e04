from PIL import Image
import urllib.request

im = Image.open("Elon_Musk.jpg")
print(im.size)

def adam():
    l = int(input("la longeur du rectangle en pixel?(C'est mieux de choisir un diviseur de 900)"))
    L = int(input("la largeur du rectangele?(C'est mieux de choisir un diviseur de 500)"))
    for i in range(int((900/2+l/2)/l)):
        for c in range(int((500/2+L/2)/L)):
            for x in range(0+i*l*2,l+i*l*2):
                for y in range(0+c*L*2,L+c*L*2):
                    pixel = im.getpixel((x,y))
                    p_rouge =255-int(pixel[0])
                    p_vert =255-int(pixel[1]) 
                    p_bleu =255-int(pixel[2])
                    im.putpixel((x,y),(p_rouge,p_vert,p_bleu))
    for i in range(int((900/2)/l)):
        for c in range(int((500/2)/L)):
            for x in range(l+i*l*2, l*2+i*l*2):
                for y in range(L+c*L*2,L*2+c*L*2):
                    pixel = im.getpixel((x,y))
                    p_rouge =255-int(pixel[0])
                    p_vert =255-int(pixel[1]) 
                    p_bleu =255-int(pixel[2])
                    im.putpixel((x,y),(p_rouge,p_vert,p_bleu))
    im.save("sortie.png")
    im.show()
print(adam())

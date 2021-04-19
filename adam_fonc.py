from PIL import Image
import urllib.request

im = Image.open("Elon_Musk.jpg")
print(im.size)

def adam():
    for i in range(5):
        for c in range(3):
            for x in range(0+i*200,100+i*200):
                for y in range(0+c*200,100+c*200):
                    pixel = im.getpixel((x,y))
                    p_rouge =255-int(pixel[0])
                    p_vert =255-int(pixel[1]) 
                    p_bleu =255-int(pixel[2])
                    im.putpixel((x,y),(p_rouge,p_vert,p_bleu))
    for i in range(4):
        for c in range(2):
            for x in range(100+i*200,200+i*200):
                for y in range(100+c*200,200+c*200):
                    pixel = im.getpixel((x,y))
                    p_rouge =255-int(pixel[0])
                    p_vert =255-int(pixel[1]) 
                    p_bleu =255-int(pixel[2])
                    im.putpixel((x,y),(p_rouge,p_vert,p_bleu))
    im.save("sortie.png")
    im.show()
print(adam())

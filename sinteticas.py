from PIL import Image
import os

INPUT_FOLDER = './images'
OUTPUT_FOLDER = './output'

#Função que retorna o caminho relativo da imagem
def in_path(filename):
    return os.path.join(INPUT_FOLDER, filename)


def triangulo(size):
    image = Image.new("RGB", (size,size), (255,255,255))

    for x in range(size):
        for y in range(size):
            if x < y:
                image.putpixel((x,y), (0,0,0))
    
    return image

def brandeira_franca():
    image = Image.new("RGB", (600,400), (255,255,255))

    for x in range(600):
        for y in range(400):
            if(x <= 200): #azul
                image.putpixel((x,y),(0,0,255))
            elif (x > 400): # vermelho
                image.putpixel((x,y), (255,0,0))
    return image


if __name__ == "__main__":
    # t = triangulo(700)
    # t.show()
    franca = brandeira_franca()
    franca.show()
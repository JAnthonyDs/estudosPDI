from PIL import Image
import os

INPUT_FOLDER = './images'
OUTPUT_FOLDER = './output'

#Função que retorna o caminho relativo da imagem
def in_path(filename):
    return os.path.join(INPUT_FOLDER, filename)

image = Image.open(in_path("pensador.jpeg"))
print(image.getpixel((400,300))) #Exibir o valor do pixel que está nessa linha e nessa coluna

image.show()
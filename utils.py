from PIL import Image
import numpy as np
import os 

INPUT_FOLDER = './images'
OUTPUT_FOLDER = './output'

#Função que retorna o caminho relativo da imagem
def in_file(filename):
    return os.path.join(INPUT_FOLDER, filename)

def out_file(filename):
    return os.path.join(OUTPUT_FOLDER, filename)

def show_vertical(img1, img2):
    im = Image.fromarray(np.vstack((np.array(img1), np.array(img2))))
    im.show()
    return im

def show_horizontal(img1,img2):
    im = Image.fromarray(np.hstack((np.array(img1), np.array(img2))))
    im.show()
    return im
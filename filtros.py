from PIL import Image, ImageFilter
import os

from utils import in_file, out_file

# DATA_DIR = os.path.join('filtros', 'data')

img = Image.open(in_file('people.jpg'))

filtred = img.filter(ImageFilter.BLUR) #borrar a imagem

filtred = img.filter(ImageFilter.CONTOUR) #contornos na imagem

filtred = img.filter(ImageFilter.EDGE_ENHANCE_MORE) #realce de arestas


filtred.show()
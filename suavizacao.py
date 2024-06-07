from PIL import Image, ImageFilter
from utils import show_horizontal, in_file

import numpy as np
from skimage import restoration

def suavizacao_gaussiana(img,r): #Utiliza média ponderada
    saida = img.filter(ImageFilter.BoxBlur(r))
    return saida

def suavizacao_mediana(img): # Utiliza filtro mediano
    saida = img.filter(ImageFilter.MedianFilter())
    return saida

def suavizacao_anisotropica(img, kappa):
    #Pare regiões diferentes da imagem usamos suavizações diferentes
    #suavização mais intesa onde não tem borda e menos intensa onde tem

    # img_array = np.array(img.convert('L'))  # Converter para escala de cinza e depois para array numpy
    img_array = np.array(img)
    anisotropic_img = restoration.denoise_tv_chambolle(img_array, weight=kappa)
    return Image.fromarray((anisotropic_img * 255).astype(np.uint8))


if __name__ == '__main__' :
    im = Image.open(in_file('lenaRuidoSaltEPepper.jpg'))
    
    gaussiana = suavizacao_gaussiana(im,2)

    mediana = suavizacao_mediana(im)

    anisotropica = suavizacao_anisotropica(im, kappa=0.1)

    show_horizontal(im,gaussiana)

from PIL import Image
from utils import in_file, out_file


def cinzaTransform(image):
    w, h = image.size

    img = Image.new("RGB", (w,h))

    for x in range(w):
        for y in range(h):
            pixel = image.getpixel((x,y))
            mediaPixel = int((0.3*pixel[0]) + (0.59*pixel[1]) + (0.11*pixel[2]))
            img.putpixel((x,y),(mediaPixel,mediaPixel,mediaPixel))
    return img

if __name__ == "__main__":
    img = Image.open(in_file("cidadeColorida.jpg"))
    cinza = cinzaTransform(img)
    # cinza.save(out_file("cinzaCidade3.jpg"))
    cinza.show()
    
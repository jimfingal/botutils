from PIL import Image
from StringIO import StringIO
import requests


path = "/Users/fingal/Code/Projects/Bots/tinyimagebot/"

small_width = 50
tiny_width = 20
very_tiny_width = 10
extremely_tiny_width = 1

def get_image_from_url(url):
    r = requests.get("https://pbs.twimg.com/media/B5HG0gWIgAAcyn2.png")
    img = Image.open(StringIO(r.content))
    return img

def resize_image(img, width):
    wpercent = (width / float(photo.size[0]))
    height = int((float(photo.size[1]) * float(wpercent)))
    img2 = img.resize((width, height), Image.NEAREST)
    return img2

def get_image_output(img):
    image_io = StringIO()
    img.save(image_io, format='JPEG')
    image_io.seek(0)  # seeks back to beginning of file for output
    return image_io

if __name__ == "__main__":

    r = requests.get("https://pbs.twimg.com/media/B5HG0gWIgAAcyn2.png")
    photo = Image.open(StringIO(r.content))
    print photo.format, photo.size, photo.mode

    width = small_width
    wpercent = (width / float(photo.size[0]))
    height = int((float(photo.size[1]) * float(wpercent)))

    im2 = photo.resize((width, height), Image.NEAREST)      # use nearest neighbour
    im3 = photo.resize((width, height), Image.BILINEAR)     # linear interpolation in a 2x2 environment
    im4 = photo.resize((width, height), Image.BICUBIC)      # cubic spline interpolation in a 4x4 environment
    im5 = photo.resize((width, height), Image.ANTIALIAS)    # best down-sizing filter
    ext = ".jpg"
    im2.save("NEAREST" + ext)
    im3.save("BILINEAR" + ext)
    im4.save("BICUBIC" + ext)
    im5.save("ANTIALIAS" + ext)

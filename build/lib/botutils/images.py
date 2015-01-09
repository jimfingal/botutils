from PIL import Image
from cStringIO import StringIO
import requests
import random

def get_image_from_url(url):
    r = requests.get(url)
    img = Image.open(StringIO(r.content))
    return img

def resize_image(img, width):
    wpercent = (width / float(img.size[0]))
    height = int((float(img.size[1]) * float(wpercent)))
    img2 = img.resize((width, height), Image.NEAREST)
    return img2

def save_and_get_image_path(img):
    rand = random.randint(1, 10000)
    img_path = "/tmp/tmpprocessed%s.png" % rand
    img.save(img_path, format='PNG')
    return img_path
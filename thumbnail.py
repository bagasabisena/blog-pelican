from PIL import Image
import glob, os

size = 256, 256

for infile in glob.glob("./content/images/gallery/cravn/*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(file + ".thumbnail.jpg", "JPEG")
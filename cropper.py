from PIL import Image

im = Image.open('Wall.png')

im2 = im.crop(im.getbbox())

im2.save("wall_cropped.png")

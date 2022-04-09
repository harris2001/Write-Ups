import base64
from PIL import Image
from pwn import *
import subprocess
from subprocess import check_output


def printing(image):
    image_64 = base64.b64encode(image)
    print(str(image_64)[2:-1])
    # print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
im1 = Image.open("../img1.png")
pixel1 = im1.load()
im2 = Image.open("../img2.png")
pixel2 = im2.load()
for i in range(im1.size[0]):
    for j in range(im1.size[1]):
        pix1 = (pixel1[i,j])
        pix2 = (pixel2[i,j])
        pixel2[i,j] += int(pix1/18)

im2.save('../img2-modified.png')

im1 = Image.open("../img1.png")
pixel1 = im1.load()
im2 = Image.open("../img2.png")
pixel2 = im2.load()
for i in range(im1.size[0]):
    for j in range(im1.size[1]):
        pix1 = (pixel1[i,j])
        pix2 = (pixel2[i,j])
        pixel1[i,j] = pixel2[i,j] + int(pix1/13)

im1.save('../img1-modified.png')

image1 = open("../img1-modified.png", 'rb').read()
image2 = open("../img2-modified.png", 'rb').read()

printing(image1)
printing(image2)


# r = remote("icu.chal.pwni.ng",1337)

# comm = str(r.recv())[2:-3].split(" ")[2]
# print(">>>>>"+comm)
# hashcash = check_output(["hashcash", "-qmb24", comm])
# out = hashcash
# print("Sending ")
# print(out)
#
# r.send(hashcash)
# out = r.recv()
# print(f"[Received]:{out}")
# print(f"[Sending]:{base64.b64encode(image1)}")
# r.send(base64.b64encode(image1))
# r.send(b'\n')
# out = r.recv()
# print(out)
# print(f"[Sending]:{base64.b64encode(image2)}")
# r.send(base64.b64encode(image2))
# r.send('\n')
# r.interactive()



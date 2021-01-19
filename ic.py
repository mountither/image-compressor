import sys
from PIL import Image
import io 
from os import path, listdir, chdir
from argparse import ArgumentParser

parser = ArgumentParser()


parser.add_argument('--dir', default=".", type=str)
parser.add_argument('--resize', default=False, type=bool)
parser.add_argument('--bh', default=500, type=int)
parser.add_argument('--ext', default=False, type=bool)

args=parser.parse_args()


def optimise_img():

    # abs_dir = path.dirname(path.abspath(__file__))

    if args.dir != ".":
        chdir(args.dir)

    files = listdir()

    imgs = [file for file in files if file.endswith(('png', 'jpg'))]

    baseheight = args.bh

    for img in imgs:

        filename, file_ext = path.splitext(img)

        opened_img = Image.open(img)

        if args.resize:
            print(opened_img.size)
            hpercent = (baseheight/float(opened_img.size[1]))
            wsize = int((float(opened_img.size[0])*float(hpercent)))
            img_r = opened_img.resize((wsize,baseheight), Image.ANTIALIAS)
            img_r.save('resized_' + img, quality=90)

        else:
            if file_ext == ".png":
                opened_img.convert('RGB').save('ic_' +filename + '.jpg', quality=95, optimize=True)
            else: 
                opened_img.save("ic_" + img, 'JPEG', quality=40, optimize=True)

        

optimise_img()


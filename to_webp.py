import subprocess
import sys
from PIL import Image
import io 
from os import path, listdir, chdir
from argparse import ArgumentParser

# subprocess.call('powershell.exe Get-Process', shell=True)


parser = ArgumentParser()


parser.add_argument('--dir', default=".", type=str)

args=parser.parse_args()

def convert_to_webp():

    if args.dir != ".":
            chdir(args.dir)

    files = listdir()

    imgs = [file for file in files if file.endswith(('png', 'jpg'))]

    for img in imgs:
        # print(img)

        filename, file_ext = path.splitext(img)

        subprocess.call('powershell.exe cwebp {} -o {}.webp'.format(img, filename), shell=True)

convert_to_webp()
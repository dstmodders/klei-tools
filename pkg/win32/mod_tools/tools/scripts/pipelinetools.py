import os
import string

import Image


def TrimImage(imagename):
    im = Image.open(imagename)
    width = im.size[0]
    height = im.size[1]

    top = height
    bottom = 0
    left = width
    right = 0

    x = 0
    y = 0
    for pix in im.getdata():
        if pix[3] != 0:
            if top > y:
                top = y
            if bottom < y:
                bottom = y
            if left > x:
                left = x
            if right < x:
                right = x

        x = x + 1
        if x == width:
            x = 0
            y = y + 1
    box = (left, top, right, bottom)
    cropped = im.crop(box)
    cropped.load()

    return (width, height), box, cropped


def GetBaseDirectory(_file, knowndir):
    fullpath = os.path.abspath(_file)
    basedir = fullpath
    idx = string.find(basedir, knowndir)
    if idx == -1:
        raise Exception("File " + basedir + " not rooted under " + knowndir)
    return basedir[:idx]


def VerifyDirectory(basedir, _dir):
    outdir = os.path.join(basedir, _dir)
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    return outdir

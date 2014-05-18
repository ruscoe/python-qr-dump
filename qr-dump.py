#! /usr/bin/env python

"""Parses QR codes found in image files and outputs results as CSV"""

from os import listdir
import argparse
import csv

import Image
import zbar

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--path", type=str, required=True, help="the path to the image files")
parser.add_argument("-o", "--output", type=str, help="the name of the file to write results to")

args = parser.parse_args()

results = []

scanner = zbar.ImageScanner();

files = listdir(args.path)
for filename in files:
    # Load image file.
    pil = Image.open(args.path + '/' + filename).convert('L')
    width, height = pil.size
    raw = pil.tostring()

    # Parse the image.
    image = zbar.Image(width, height, 'Y800', raw)

    # Scan the image for readable codes.
    scanner.scan(image)

    for symbol in image:
        if str(symbol.type) == 'QRCODE':
            imagedata = [filename, symbol.data]
            results.append(imagedata)

    del image

if args.output is None:
    # print the results.
    print results
else:
    # Write the results to a file.
    with open(args.output, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(results)


#!/bin/bash

# get the image from Postcode lottery
python getPCImage.py
# OCR the Image to get teh postcode
tesseract postcode.gif out
# run a fuzzy comparison and message if match is > 80
python matchCheck.py
#tidy up
rm *.txt
rm *.gif

# FPCL
## Overview
I signed up to thh Free Postcode Lottery a while ago and each day I need to click a link in the email to check the results.  
I understand that the lottery is funded by ads but though t it woulkd be interesting to see if I could automate teh checks.

This set of scripts perform the following:

* Controller.sh
  * Master controller for the scripts, I used shell as I could not get the pyTesseract library to work on CentOS
  * runs getPCImage.py to get the postcode image from the site
  * OCRs the Postcode image
  * runs matchCheck.py to check if they match and send a text
* getPCImage.py
  * Log into the FreepostcodeLottery site using your personal key
  * download the image that contains the winning postcode
* matchCheck.py
  * Perfomr a fuzzy comparison between the OCR output from timage and the desired postcode
  * of OCR is greater than 80 then send a text using twilio

I chose to this as a mixture of shell and Python based on the libraries I could find, and more importantly get working.  I am using Centos on AWS Lightsail.

## Prerequisite
I am assuming that Python and Pip are installed

### Tesseract
The main prerequisite was Tesseract Library, which did not seem to install easily on Centos, I therefore had to manuall install this.   I followed [this guide](https://www.linkedin.com/pulse/ocr-optical-character-recognition-set-up-tesseract-centos-kumar) witha few tweaks, so will replicate the steps below.

#### Install Dev Tools

sudo yum groupinstall "Development tools"
sudo yum -y install automake autoconf libtool zlib-devel libjpeg-devel giflib libtiff-devel libwebp libwebp-devel libicu-devel openjpeg-devel cairo-devel 

#### Install Leptonica

Wget http://www.leptonica.com/source/leptonica-1.74.1.tar.gz

 tar xzvf leptonica-1.74.1.tar.gz

cd leptonica-1.74.1

./configure

sudo make 
sudo make install
cd..

#### Install tesseract

Wget https://github.com/tesseract-ocr/tesseract/archive/3.05.00.tar.gz

tar xzvf 3.05.00.tar.gz

cd tesseract-3.05.00/

./autogen.sh
./configure
sudo make
sudo make install 
sudo ldconfig

#### Download Tesseract english trainer:

wget https://sourceforge.net/projects/tesseract-ocr-alt/files/tesseract-ocr-3.02.eng.tar.gz
tar xzvf tesseract-ocr-3.02.eng.tar.gz
sudo cp tesseract-ocr/tessdata/* /usr/local/share/tessdata
export TESSDATA_PREFIX=/usr/local/share/tessdata

### Install fuzzy checker
sudo pip install fuzzywuzzy
sudo pip install python-Levenshtein

### install Twilio
pip install Twilio

## Running The Scripts

I have simply set the script up to run at the time I normally receive the email using a cron job


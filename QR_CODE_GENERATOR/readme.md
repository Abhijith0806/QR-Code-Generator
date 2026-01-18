TITLE : QR CODE GENERATOR 
DESCRIPTION : Simple QR Code generator using Python.
            This project allows users to generate QR codes for any URL, with optional customization for size and borders.
WHAT IT DOES :
         - Reads the url from the user
         - Asks whether the user wants to modify QR code size
         - If 'yes' 
               Allows custom version, box size, and border
         - If 'no' 
               Uses default QR code settings
         - Reads the image name and format from the user
         - Generates and saves the QR code image.
LIBRARIES USED :
         [Python,qrcode,Pillow] 
HOW TO RUN :
         - Install dependencies 
         - run qr_code.py
OUTPUT :
     - Generates a QR code image file in one of the following formats:
        .png .jpg .jpeg
     - The image is saved in the same directory as the script.
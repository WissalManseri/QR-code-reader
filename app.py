#To create a QR code reader using Python, you can use the pyzbar library, which provides an interface to the ZBar barcode scanning library.
import cv2
from pyzbar.pyzbar import decode

# Load the image
image = cv2.imread('qrcode.png')

# Decode the QR code
decoded = decode(image)

# Print the decoded data
if decoded:
    print(decoded[0].data.decode())
else:
    print("No QR code detected.")

import qrcode

# URL to be encoded in the QR code
url = "https://www.yourwebsite.com/"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file
img_path = "./qr.png"
img.save(img_path)

img_path

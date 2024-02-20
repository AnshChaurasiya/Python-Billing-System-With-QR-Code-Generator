# main file: program.py

import read
import purchase
import write
import qrcode
from PIL import Image
import os



def generate_qr_code(user_details, file_name):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(user_details)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(file_name)

    # Open and display the image
    img.show()



again = "Y"
while again.upper() == "Y":
    a = read.read_file()
    b = purchase.purchase(a)
    write.over_write(a, b)

    # Calculate the total price based on the quantity and unit price of each item
    total_price = sum(int(a[i][1]) * b.get(a[i][0].upper(), 0) for i in range(len(a)))

    # Generate QR code for the current user's purchase details
    user_details = f"{b}\nTotal Price: {total_price}"  # Include total price in the user details
    qr_code_file_name = "user_purchase_qr_code.png"  # Replace with desired file name
    generate_qr_code(user_details, qr_code_file_name)

    again = input("\nDoes any new customer wait to buy a product? ")

print("\nThank you for shopping from our store!!")
print("Please check your invoice for your shopping details, \nWhich we created txt file format for you.")

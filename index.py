import cv2
import os
import pytesseract
import config

pytesseract.pytesseract.tesseract_cmd = config.TESSERACT_CMD_PATH

image_path = r"image.png"
image = cv2.imread(image_path)

if os.access(image_path, os.R_OK):
    image = cv2.imread(image_path)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresholded_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    custom_config = r'--oem 3 --psm 6'

    extracted_text = pytesseract.image_to_string(thresholded_image)

    print("[output]" , extracted_text)
    
else:
    print(f"[error] Cannot access file: {image_path}")

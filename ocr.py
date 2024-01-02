import pytesseract
import cv2

def detect(filename):
    img = cv2.imread(filename)
    text = pytesseract.image_to_string(img,lang='san')
    return text
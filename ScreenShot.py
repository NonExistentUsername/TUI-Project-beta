import cv2

def screenShotMake(img):
    image = img
    dst = cv2.GaussianBlur(image, (15, 15), cv2.BORDER_DEFAULT)
    return dst
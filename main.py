import cv2

image = cv2.imread('AVIRA.jpg') #to read the image

grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #to convert image into grey image i.e. B/W image
inverted_img = cv2.bitwise_not(grey_img)
blur_img = cv2.GaussianBlur(inverted_img, (21,21), 00)
inverted_blur_img = cv2.bitwise_not(blur_img)
sketch = cv2.divide(grey_img, inverted_blur_img, scale=256.0)

cv2.imwrite('sketch.png', sketch)
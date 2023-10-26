import cv2
import numpy as np
import utilis as utl

img_width, img_height = 500, 500 # img dimensions

img = cv2.imread("images/test_img.jpg")
img = cv2.resize(img, (img_width, img_height))
imgContours = img.copy()

# ----------------------Image Pre-Processing-------------------------------------

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # Covert img to grayscale
imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)  # Apply gaussian blur, parameter=>(grayscaled_img,kernel,sigma)

imgCanny = cv2.Canny(imgBlur,338,0)  # Canny edge detector to Detect edges, Parameters=>(Blurred Image, Thresh values)

contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imgContours, contours, -1, (0,255,0), 5)  # Parameters=>(imgContours, contours, <<how many | in my case all>>, <<color | in my case GREEN>>, <<Thickness>>)

imgBlank = np.zeros_like(img)
imageArray = ([img, imgBlur,imgGray, imgBlur, imgCanny, imgContours])

utl.display_images_scrollable(imageArray)


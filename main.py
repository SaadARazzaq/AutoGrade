import cv2
import numpy as np
import utilis as utl

img_width, img_height = 500, 500 # img dimensions

img = cv2.imread("images/test_img.jpg")
img = cv2.resize(img, (img_width, img_height))
imgContours = img.copy()
imgBiggestContours = img.copy()

# ----------------------Image Pre-Processing-------------------------------------

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # Covert img to grayscale
imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)  # Apply gaussian blur, parameter=>(grayscaled_img,kernel,sigma)

imgCanny = cv2.Canny(imgBlur,338,0)  # Canny edge detector to Detect edges, Parameters=>(Blurred Image, Thresh values)

# ----------------------Finding All Countours-------------------------------------
contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imgContours, contours, -1, (0,255,0), 5)  # Parameters=>(imgContours, contours, <<how many | in my case all>>, <<color | in my case GREEN>>, <<Thickness>>)

# ----------------------Find Rectangles-------------------------------------
rectCont = utl.rectContours(contours)
firstCont = utl.getCornerPoints(rectCont[0])
secondCont = utl.getCornerPoints(rectCont[1])
thirdCont = utl.getCornerPoints(rectCont[2])
fourthCont = utl.getCornerPoints(rectCont[3])


if firstCont.size != 0 and secondCont.size != 0 and thirdCont.size != 0 and fourthCont.size != 0:
    cv2.drawContours(imgBiggestContours, firstCont,-1,(0,255,0),10)  # Label: BOX#2
    cv2.drawContours(imgBiggestContours, secondCont,-1,(0,255,0),10)  # Label: BOX#3
    cv2.drawContours(imgBiggestContours, thirdCont,-1,(0,255,0),10)  # Label: BOX#1
    cv2.drawContours(imgBiggestContours, fourthCont,-1,(0,255,0),10)  # Label: BOX#4
   
    firstCont = utl.reorder(firstCont)
    secondCont = utl.reorder(secondCont)
    thirdCont = utl.reorder(thirdCont)
    fourthCont = utl.reorder(fourthCont)

    # ------------------For Bird Eye View---------------------------
    first_pt1 = np.float32(firstCont)
    first_pt2 = np.float32([[0,0], [200, 0], [0, img_height], [200, img_height]])
    first_matrix = cv2.getPerspectiveTransform(first_pt1, first_pt2)
    first_imgWarpColored = cv2.warpPerspective(img, first_matrix, (200, img_height))

    second_pt1 = np.float32(secondCont)
    second_pt2 = np.float32([[0,0], [200, 0], [0, img_height], [200, img_height]])
    second_matrix = cv2.getPerspectiveTransform(second_pt1, second_pt2)
    second_imgWarpColored = cv2.warpPerspective(img, second_matrix, (200, img_height))

    third_pt1 = np.float32(thirdCont)
    third_pt2 = np.float32([[0,0], [200, 0], [0, img_height], [200, img_height]])
    third_matrix = cv2.getPerspectiveTransform(third_pt1, third_pt2)
    third_imgWarpColored = cv2.warpPerspective(img, third_matrix, (200, img_height))

    fourth_pt1 = np.float32(fourthCont)
    fourth_pt2 = np.float32([[0,0], [200, 0], [0, img_height], [200, img_height]])
    fourth_matrix = cv2.getPerspectiveTransform(fourth_pt1, fourth_pt2)
    fourth_imgWarpColored = cv2.warpPerspective(img, fourth_matrix, (200, img_height))

    # ------------------APPLY THRESHOLD---------------------------
    first_imgWarpGray = cv2.cvtColor(first_imgWarpColored, cv2.COLOR_BGR2GRAY)
    first_imgThresh = cv2.threshold(first_imgWarpGray,140,255,cv2.THRESH_BINARY_INV)[1]
    
    second_imgWarpGray = cv2.cvtColor(second_imgWarpColored, cv2.COLOR_BGR2GRAY)
    second_imgThresh = cv2.threshold(second_imgWarpGray,140,255,cv2.THRESH_BINARY_INV)[1]

    third_imgWarpGray = cv2.cvtColor(third_imgWarpColored, cv2.COLOR_BGR2GRAY)
    third_imgThresh = cv2.threshold(third_imgWarpGray,140,255,cv2.THRESH_BINARY_INV)[1]
    
    fourth_imgWarpGray = cv2.cvtColor(fourth_imgWarpColored, cv2.COLOR_BGR2GRAY)
    fourth_imgThresh = cv2.threshold(fourth_imgWarpGray,140,255,cv2.THRESH_BINARY_INV)[1]

imgBlank = np.zeros_like(img)
imageArray = ([img, imgGray, imgBlur, imgCanny, imgContours, imgBiggestContours, first_imgWarpColored, first_imgThresh, second_imgWarpColored, second_imgThresh, third_imgWarpColored, third_imgThresh, fourth_imgWarpColored, fourth_imgThresh])

utl.display_images_scrollable(imageArray)


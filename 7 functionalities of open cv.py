import cv2 as cv

img = cv.imread(r"C:\Users\moiez\OneDrive\Desktop\computer vision\Resources\Photos\park.jpg")
cv.imshow("cats 2",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow("blur",blur)

canny = cv.Canny(blur,125,175)
cv.imshow("canny",canny)

dilated = cv.dilate(canny,None,iterations=3)
cv.imshow("dilated",dilated)

resize = cv.resize(dilated,(0,0),fx=3,fy=1)
cv.imshow("resize",resize)

croped = img[120:268,300:360]
cv.imshow("croped",croped)

cv.waitKey(0)

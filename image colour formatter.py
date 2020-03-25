import cv2
from random import randint

def nothing(x):
    pass

# Read in the image
img = cv2.imread('red-rose.jpg')

# Create a window
cv2.namedWindow('Rose')

# create trackbars for color change
cv2.createTrackbar('R','Rose',0,255,nothing)
cv2.createTrackbar('G','Rose',0,255,nothing)
cv2.createTrackbar('B','Rose',0,255,nothing)

while(1):
    cv2.imshow('Rose',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27: # Esc key
        break

    # get current positions of four trackbars
    nr = cv2.getTrackbarPos('R','Rose')
    ng = cv2.getTrackbarPos('G','Rose')
    nb = cv2.getTrackbarPos('B','Rose')

    # Give a place with random points to give sparkle effect
    for i in range(100):
        img[randint(50,100), randint(100,150)] = [nb, ng, nr]

cv2.destroyAllWindows()
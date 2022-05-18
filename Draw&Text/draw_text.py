# Drawing and putting text on images
import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype= 'uint8')
cv.imshow('Blank', blank)

# Paint image certain color
blank[200:300, 300:400] = 255,0,0
cv.imshow('Blue', blank)

# Draw Rectangle
cv.rectangle(blank, (0,0), (250,300), (255,0,0), thickness=cv.FILLED)
cv.imshow('Rectange', blank)

# Draw Circle
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,0), thickness = cv.FILLED)
cv.imshow('Circle', blank)

# Draw Line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness = 3)
cv.imshow('Line', blank)

# Writing Text on an Image
cv.putText(blank, 'Hello World', (225,205), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), thickness = 2)
cv.imshow('Text', blank)
cv.waitKey(0)

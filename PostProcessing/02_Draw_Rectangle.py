import cv2
import numpy as np

def drawRect(image, point1, point2, color=(255, 0, 0), thickness=3, lineType=cv2.LINE_AA):
    result = np.copy(image)
    return cv2.rectangle(result, point1, point2, color, thickness, lineType)



imagePath = "../Data/image_01.png"
image = cv2.imread(imagePath, cv2.IMREAD_COLOR)

pt1 = (608, 358)
pt2 = (756, 492)

rect_01 = drawRect(image, pt1, pt2, (0, 0, 255), 5)
rect_02 = drawRect(image, pt1, pt2, (0, 0, 255), 0)
rect_03 = drawRect(image, pt1, pt2, (0, 0, 255), -1)

cv2.namedWindow('input', cv2.WINDOW_NORMAL)
cv2.namedWindow('rect_01', cv2.WINDOW_NORMAL)
cv2.namedWindow('rect_02', cv2.WINDOW_NORMAL)
cv2.namedWindow('rect_03', cv2.WINDOW_NORMAL)
cv2.imshow('input', image)
cv2.imshow('rect_01', rect_01)
cv2.imshow('rect_02', rect_02)
cv2.imshow('rect_03', rect_03)
cv2.waitKey()
cv2.destroyAllWindows()

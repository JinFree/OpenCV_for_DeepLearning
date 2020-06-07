import cv2
import numpy as np
# 다른 경로에서 스크립트를 실행해도 경로 문제 없이 이미지를 열기 위한 코드
import Utils
path_to_image = Utils.path_function("/../Data/image_01.png")

def computeHist(image, mask=None):
    bins = np.arange(256).reshape(256,1)
    if len(image.shape)==2:
        h = np.zeros((300,256,1))
        hist_item = cv2.calcHist([image],[0],None,[256],[0,255]) 
        cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX) 
        hist=np.int32(np.around(hist_item)) 
        pts = np.column_stack((bins,hist)) 
        cv2.polylines(h,[pts],False, 255)
    else:
        h = np.zeros((300,256,3))
        color = [ (255,0,0),(0,255,0),(0,0,255) ] 
        for ch, col in enumerate(color): 
            hist_item = cv2.calcHist([image],[ch],None,[256],[0,255]) 
            cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX) 
            hist=np.int32(np.around(hist_item)) 
            pts = np.column_stack((bins,hist)) 
            cv2.polylines(h,[pts],False,col)
    return np.flipud(h)
    
def histogramEqualize(image):
    if len(image.shape) == 2:
        return cv2.equalizeHist(image)
    else:
        ch1, ch2, ch3 = splitImage(image)
        ch1_eq = histogramEqualize(ch1)
        ch2_eq = histogramEqualize(ch2)
        ch3_eq = histogramEqualize(ch3)
        return mergeImage(ch1_eq, ch2_eq, ch3_eq)
        
Input = cv2.imread(path_to_image, cv2.IMREAD_GRAYSCALE)
Histogram = computeHist(Input)
Histogram_Equalized = histogramEqualize(Input)

cv2.namedWindow("Input", cv2.WINDOW_NORMAL)
cv2.imshow("Input", Input)
cv2.namedWindow("Histogram", cv2.WINDOW_NORMAL)
cv2.imshow("Histogram", Histogram)
cv2.namedWindow("Histogram_Equalized", cv2.WINDOW_NORMAL)
cv2.imshow("Histogram_Equalized", Histogram_Equalized)
cv2.waitKey()

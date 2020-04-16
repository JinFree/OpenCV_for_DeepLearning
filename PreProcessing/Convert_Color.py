import cv2
import numpy as np
# 다른 경로에서 스크립트를 실행해도 경로 문제 없이 이미지를 열기 위한 코드
import Utils
path_to_image = Utils.path_function("/../Data/image_01.png")

def split_channels(input_image):
    return cv2.split(input_image)
   
def merge_channels(channel1, channel2, channel3):
    return cv2.merge((channel1, channel2, channel3))

def convert_colorspace(input_image, flag = cv2.COLOR_BGR2HSV):
    return cv2.cvtColor(input_image, flag)

def histogram_equalize(input_image):
    return cv2.equalizeHist(input_image) 


Input_Color = cv2.imread(path_to_image, cv2.IMREAD_COLOR)

HSV = convert_colorspace(Input_Color, cv2.COLOR_BGR2HSV)

H, S, V = split_channels(HSV)

V_eq = histogram_equalize(V)

HSV_2 = merge_channels(H, S, V_eq)
BGR_2 = convert_colorspace(HSV_2, cv2.COLOR_HSV2BGR)

cv2.namedWindow("Input_Color", cv2.WINDOW_NORMAL)
cv2.imshow("Input_Color", Input_Color)
cv2.namedWindow("HSV", cv2.WINDOW_NORMAL)
cv2.imshow("HSV", HSV)
cv2.namedWindow("H", cv2.WINDOW_NORMAL)
cv2.imshow("H", H)
cv2.namedWindow("S", cv2.WINDOW_NORMAL)
cv2.imshow("S", S)
cv2.namedWindow("V", cv2.WINDOW_NORMAL)
cv2.imshow("V", V)
cv2.namedWindow("V_eq", cv2.WINDOW_NORMAL)
cv2.imshow("V_eq", V_eq)
cv2.namedWindow("HSV_2", cv2.WINDOW_NORMAL)
cv2.imshow("HSV_2", HSV_2)
cv2.namedWindow("BGR_2", cv2.WINDOW_NORMAL)
cv2.imshow("BGR_2", BGR_2)
cv2.imwrite("BGR_2.jpg", BGR_2)
cv2.waitKey()
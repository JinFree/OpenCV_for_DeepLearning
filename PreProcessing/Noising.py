import cv2
import numpy as np
import random
# 다른 경로에서 스크립트를 실행해도 경로 문제 없이 이미지를 열기 위한 코드
import Utils
path_to_image = Utils.path_function("/../Data/image_01.png")

# 소금과 후추 노이즈 함수
def add_salt_and_pepper(input_image, noise_ratio = 0.001):
    image = np.copy(input_image)
    height, width = image.shape[0], image.shape[1]
    num_of_noise_pixel = int(noise_ratio * (height * width))
    if len(image.shape) == 2: # Grayscale Image
        for i in range(num_of_noise_pixel):
            x = np.random.randint(0, width)
            y = np.random.randint(0, height)
            image[y, x] = np.random.randint(0, 2) * 255
    else: # Color Image
        for i in range(num_of_noise_pixel):
            x = np.random.randint(0, width)
            y = np.random.randint(0, height)
            image[y, x, 0] = random.randint(0, 2) * 255
            image[y, x, 1] = random.randint(0, 2) * 255
            image[y, x, 2] = random.randint(0, 2) * 255
    return image

# CMOS 센서 특성 모사 함수
def add_cmos_noise(input_image):
    image = np.copy(input_image)
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            if len(image.shape) == 2:
                value = image[y, x]
                value += random.randint(-5, 5)
                if value > 255:
                    value = 255
                elif value < 0:
                    value = 0
                image[y, x] = value
            else:
                for idx in range(0, 3):
                    value = image[y, x, idx]
                    value += random.randint(-5, 5)
                    if value > 255:
                        value = 255
                    elif value < 0:
                        value = 0
                    image[y, x, idx] = value
    return image
    
Input_Color = cv2.imread(path_to_image, cv2.IMREAD_COLOR)
Input_Gray = cv2.imread(path_to_image, cv2.IMREAD_GRAYSCALE)

Result_Color = add_salt_and_pepper(Input_Color, 0.005)
Result_Gray = add_salt_and_pepper(Input_Gray, 0.005)
Result_Color_Cmos = add_cmos_noise(Input_Color)
Result_Gray_Cmos = add_cmos_noise(Input_Gray)

cv2.namedWindow("Input_Color", cv2.WINDOW_NORMAL)
cv2.imshow("Input_Color", Input_Color)
cv2.namedWindow("Result_Color", cv2.WINDOW_NORMAL)
cv2.imshow("Result_Color", Result_Color)
cv2.namedWindow("Result_Color_Cmos", cv2.WINDOW_NORMAL)
cv2.imshow("Result_Color_Cmos", Result_Color_Cmos)
cv2.namedWindow("Input_Gray", cv2.WINDOW_NORMAL)
cv2.imshow("Input_Gray", Input_Gray)
cv2.namedWindow("Result_Gray", cv2.WINDOW_NORMAL)
cv2.imshow("Result_Gray", Result_Gray)
cv2.namedWindow("Result_Gray_Cmos", cv2.WINDOW_NORMAL)
cv2.imshow("Result_Gray_Cmos", Result_Gray_Cmos)
cv2.waitKey()

import cv2
import numpy as np
# 다른 경로에서 스크립트를 실행해도 경로 문제 없이 이미지를 열기 위한 코드
import Utils
path_to_image = Utils.path_function("/../Data/image_01.png")

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
            image[y, x, 0] = np.random.randint(0, 2) * 255
            image[y, x, 1] = np.random.randint(0, 2) * 255
            image[y, x, 2] = np.random.randint(0, 2) * 255
    return image

Input_Color = cv2.imread(path_to_image, cv2.IMREAD_COLOR)
Input_Gray = cv2.imread(path_to_image, cv2.IMREAD_GRAYSCALE)

Result_Color = add_salt_and_pepper(Input_Color, 0.005)
Result_Gray = add_salt_and_pepper(Input_Gray, 0.005)

cv2.namedWindow("Input_Color", cv2.WINDOW_NORMAL)
cv2.imshow("Input_Color", Input_Color)
cv2.namedWindow("Result_Color", cv2.WINDOW_NORMAL)
cv2.imshow("Result_Color", Result_Color)
cv2.namedWindow("Input_Gray", cv2.WINDOW_NORMAL)
cv2.imshow("Input_Gray", Input_Gray)
cv2.namedWindow("Result_Gray", cv2.WINDOW_NORMAL)
cv2.imshow("Result_Gray", Result_Gray)
cv2.waitKey()

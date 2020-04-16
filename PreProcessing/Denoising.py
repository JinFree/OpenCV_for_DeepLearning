import cv2
import numpy as np
# 다른 경로에서 스크립트를 실행해도 경로 문제 없이 이미지를 열기 위한 코드
import Utils
path_to_image = Utils.path_function("/../Data/image_01.png")


def nothing(x):
    pass

def mean_blur(input_image, kernel_size = 3):
    size = ((kernel_size+1) * 2 - 1, (kernel_size+1) * 2 - 1)
    result = cv2.blur(input_image, size)
    return result

def gaussian_blur(input_image, kernel_size, sigmaX, sigmaY):
    size = ((kernel_size+1) * 2 - 1, (kernel_size+1) * 2 - 1)
    result = cv2.GaussianBlur(input_image, ksize=size, sigmaX=sigmaX, sigmaY=sigmaY)
    return result

def median_blur(input_image, kernel_size):
    ksize = (kernel_size+1) * 2 - 1
    result = cv2.medianBlur(input_image, ksize)
    return result
    
def bilateral_filter(input_image, kernel_size, sigmaColor, sigmaSpace):
    d = (kernel_size+1) * 2 - 1
    result = cv2.bilateralFilter(input_image, d, sigmaColor=sigmaColor, sigmaSpace=sigmaSpace)
    return result
    
Input_Color = cv2.imread(path_to_image, cv2.IMREAD_COLOR)

Input_Gray = cv2.imread(path_to_image, cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('image', cv2.WINDOW_GUI_EXPANDED)

cv2.createTrackbar('BlurSize', 'image', 1, 10, nothing)
cv2.createTrackbar('sigmaX or sigmaColor', 'image', 1, 50, nothing)
cv2.createTrackbar('sigmaY or sigmaSpace', 'image', 1, 50, nothing)

switch = '0:Original\n1:Mean\n2:Gaussian\n3:Median\n4:Bilateral'
cv2.createTrackbar(switch, 'image', 0, 4, nothing)

switch_color = '0:Color\n1:Gray'
cv2.createTrackbar(switch_color, 'image', 0, 1, nothing)

Backup_image = None
Show_Image = None

while True:

    if cv2.waitKey(10) & 0xFF == 27:
        break
    sigma1 = cv2.getTrackbarPos('sigmaX or sigmaColor', 'image')
    sigma2 = cv2.getTrackbarPos('sigmaY or sigmaSpace', 'image')
    size = cv2.getTrackbarPos('BlurSize', 'image')
    s = cv2.getTrackbarPos(switch, 'image')
    s_color = cv2.getTrackbarPos(switch_color, 'image')
    if s_color == 0:
        Backup_image = np.copy(Input_Color)
    if s_color == 1:
        Backup_image = np.copy(Input_Gray)
        
    if s == 0:
        Show_Image = Backup_image
    if s == 1:
        Show_Image = mean_blur(Backup_image, size)
    if s == 2:
        Show_Image = gaussian_blur(Backup_image, size, sigma1, sigma2)
    if s == 3:
        Show_Image = median_blur(Backup_image, size)
    if s == 4:
        Show_Image = bilateral_filter(Backup_image, size, sigma1, sigma2)
        
    cv2.imshow('image', Show_Image)
    

cv2.destroyAllWindows()




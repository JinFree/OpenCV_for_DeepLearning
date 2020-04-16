import cv2
import numpy as np
# 다른 경로에서 스크립트를 실행해도 경로 문제 없이 이미지를 열기 위한 코드
import Utils
path_to_image = Utils.path_function("/../Data/image_01.png")


def nothing(x):
    pass

def draw_rectangle_roi(input_image, x1, y1, x2, y2, color=(255, 0, 0), thickness=3, lineType=cv2.LINE_AA):
    point1 = (x1, y1)
    point2 = (x2, y2)
    return cv2.rectangle(input_image, point1, point2, color, thickness, lineType)

def cut_rectangle_roi(input_image, x1, y1, x2, y2):
    return np.copy(input_image[y1:y2, x1:x2])

def resize_image(input_image, dsize = (300, 400)):
    return cv2.resize(input_image, dsize)

    
Input_Color = cv2.imread(path_to_image, cv2.IMREAD_COLOR)

height, width = Input_Color.shape[0], Input_Color.shape[1]

cv2.namedWindow('image', cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow('ROI', cv2.WINDOW_GUI_EXPANDED)

cv2.createTrackbar('x1', 'image', 0, width, nothing)
cv2.createTrackbar('y1', 'image', 0, height, nothing)
cv2.createTrackbar('x2', 'image', 1, width, nothing)
cv2.createTrackbar('y2', 'image', 1, height, nothing)

Backup_image = None
Show_Image = None
ROI = None
while True:
    Backup_image = np.copy(Input_Color)
    x1 = cv2.getTrackbarPos('x1', 'image')
    y1 = cv2.getTrackbarPos('y1', 'image')
    x2 = cv2.getTrackbarPos('x2', 'image')
    y2 = cv2.getTrackbarPos('y2', 'image')
    
    if abs(x1-x2) > 0  and abs(y2-y1) >0:
        ROI = cut_rectangle_roi(Backup_image, x1, y1, x2, y2)
        ROI = resize_image(ROI, (width, height))
        cv2.imshow('ROI', ROI)
        
    Show_Image = draw_rectangle_roi(Backup_image, x1, y1, x2, y2) 
    cv2.imshow('image', Show_Image)
    if cv2.waitKey(10) & 0xFF == 27:
        cv2.imwrite("ROI.jpg", ROI)
        break
    

cv2.destroyAllWindows()




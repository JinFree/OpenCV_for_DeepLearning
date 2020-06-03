import cv2
import numpy as np

def drawText(image, text, point=(10, 10), font=cv2.FONT_HERSHEY_PLAIN, fontScale=2.0, color=(255,255,255), thickness=3, lineType=cv2.LINE_AA):
    result = np.copy(image)
    return cv2.putText(result, text, point, font, fontScale, color, thickness, lineType)


imagePath = "../Data/image_01.png"
image = cv2.imread(imagePath, cv2.IMREAD_COLOR)


image_text = drawText(image, "cv2.FONT_HERSHEY_SIMPLEX", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 1)
image_text = drawText(image_text, "cv2.FONT_HERSHEY_PLAIN", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 0, 0), 1)
image_text = drawText(image_text, "cv2.FONT_HERSHEY_DUPLEX", (10, 150), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 0, 0), 1)
image_text = drawText(image_text, "cv2.FONT_HERSHEY_COMPLEX", (10, 200), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255, 0, 0), 1)
image_text = drawText(image_text, "cv2.FONT_HERSHEY_TRIPLEX", (10, 250), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255, 0, 0), 1)
image_text = drawText(image_text, "cv2.FONT_HERSHEY_COMPLEX_SMALL", (10, 300), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (255, 0, 0), 1)
image_text = drawText(image_text, "cv2.FONT_HERSHEY_SCRIPT_SIMPLEX", (10, 350), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, (255, 0, 0), 1)
image_text = drawText(image_text, "cv2.FONT_HERSHEY_SCRIPT_COMPLEX", (10, 400), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.0, (255, 0, 0), 1)

cv2.namedWindow('input', cv2.WINDOW_NORMAL)
cv2.namedWindow('result', cv2.WINDOW_NORMAL)
cv2.imshow('input', image)
cv2.imshow('result', image_text)
cv2.waitKey()
cv2.destroyAllWindows()

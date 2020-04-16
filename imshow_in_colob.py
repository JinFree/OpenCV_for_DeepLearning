import cv2
import matplotlib.pyplot as plt

#%matplotlib inline
def imshow(cv_image):
    rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb)
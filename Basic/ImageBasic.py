import cv2

# 다른 경로에서 스크립트를 실행해도 경로 문제 없이 이미지를 열기 위한 코드
import Utils
path_to_image = Utils.path_function("/../Data/image_01.png")


# 입력된 경로의 이미지를 열어서 numpy array로 반환하는 함수
# 원본 이미지의 색상과 무관하게 3채널로 열 때, flag = cv2.IMREAD_COLOR
COLOR = cv2.imread(path_to_image, cv2.IMREAD_COLOR)

# 원본 이미지의 색상과 무관하게 1채널로 열 때, flag = cv2.IMREAD_GRAYSCALE
GRAY = cv2.imread(path_to_image, cv2.IMREAD_GRAYSCALE)

# 원본 이미지 색상 그대로 열 때, flag = cv2.IMREAD_UNCHANGED
UNCHANGED = cv2.imread(path_to_image, cv2.IMREAD_UNCHANGED)

# cv2.namedWindow를 통해 이미지 윈도우를 열 수 있음
cv2.namedWindow("COLOR", cv2.WINDOW_NORMAL)

# cv2.imshow를 통해 이미지 윈도우에 이미지를 보여주게 함
cv2.imshow("COLOR", COLOR)

# cv2.waitKey를 통해 일정 시간 동안 혹은 입력이 있을 때까지 이미지를 보여줌
# 시간은 ms단위
cv2.waitKey(1)

cv2.namedWindow("GRAY", cv2.WINDOW_NORMAL)
cv2.imshow("GRAY", GRAY)
cv2.waitKey(1000)

cv2.namedWindow("UNCHANGED", cv2.WINDOW_NORMAL)
cv2.imshow("UNCHANGED", UNCHANGED)
cv2.waitKey()

cv2.destroyAllWindows()
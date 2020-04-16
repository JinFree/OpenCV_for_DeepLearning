import cv2

# 다른 경로에서 스크립트를 실행해도 경로 문제 없이 이미지를 열기 위한 코드
import Utils
path_to_video = Utils.path_function("/../Data/video_01.avi")

def frameProcessing(frame):
    result = frame
    return result
	
# cv2.VideoCapture를 통해 비디오를 불러올 수 있음
cap = cv2.VideoCapture(path_to_video)

# fps, width, height
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = int(cv2.VideoWriter_fourcc(*'DIVX'))
out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height), True) # True is 3-channel Output, False is 1-channel Output

cv2.namedWindow("Input", cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow("Output", cv2.WINDOW_GUI_EXPANDED)

while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        # Our operations on the frame come here
        output = frameProcessing(frame)
        # Write frame-by-frame
        out.write(output)
        # Display the resulting frame
        cv2.imshow("Input", frame)
        cv2.imshow("Output", output)

    else:
        break

    # waitKey(int(1000.0/fps)) for matching fps of video
    if cv2.waitKey(int(1000.0/fps)) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()

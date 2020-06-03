import cv2
import numpy as np
from pytorch_functions import Inference
path_to_video = 1


def frameProcessing(frame, inference_class):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    inference_result = inference_class.inference_image(frame_rgb)
    class_text, class_prob = inference_class.print_result(inference_result)
    result = cv2.putText(frame, "{}, {}%".format(class_text, class_prob), (100, 100), cv2.FONT_HERSHEY_PLAIN, 5.0, (255,255,255), 3, cv2.LINE_AA)
    return result

inference_class = Inference()
# cv2.VideoCapture를 통해 비디오를 불러올 수 있음
cap = cv2.VideoCapture(path_to_video)

# fps, width, height
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cv2.namedWindow("Input", cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow("Output", cv2.WINDOW_GUI_EXPANDED)

while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        # Our operations on the frame come here
        output = frameProcessing(frame, inference_class)
        # Display the resulting frame
        cv2.imshow("Input", frame)
        cv2.imshow("Output", output)

    else:
        break

    # waitKey(int(1000.0/fps)) for matching fps of video
    if cv2.waitKey(int(1000.0/fps)) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()

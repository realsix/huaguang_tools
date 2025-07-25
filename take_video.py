import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 30.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,1)
#        out.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))   将视频转换为灰色的源
        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('1'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
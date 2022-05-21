cap = cv2.VideoCapture(0)
Setcamera(cap)

# 每0.1S计算一次帧率
t = 0.1
counter = 0
fps = 0
start_time = time.time()

while (True):
    ret, frame = cap.read()
    frame = beauty_face(frame)
    # 测帧率
    counter += 1
    if (time.time() - start_time) > t:
        fps = counter / (time.time() - start_time)
        fps = str(fps)
        counter = 0
        start_time = time.time()
    cv2.putText(frame, "FPS {0}".format(fps), (10, 30), 1, 1.5, (255, 0, 255), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break




cap.release()
cv2.destroyAllWindows()
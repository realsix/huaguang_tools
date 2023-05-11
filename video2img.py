import cv2
import os
path = r"./myvideo2/"
pic = r"./mypic/"

videolist = os.listdir(path)
index = 775
save = 0
for i in videolist:
    cap = cv2.VideoCapture(path+i)
    count = 0
    while True:
        success, img = cap.read()
        # cv2.imshow("img",img)

        count += 1
        if not success:
            break
        if count % 10 == 0:
            cv2.imwrite(pic+str(index)+'.jpg', img)
            # cv2.imwrite(str(index)+'.jpg', img)
            print(f"\r目前是第{i}个视频，图片索引到了{index}", end="")
            index += 1
        save += 1
        cv2.waitKey(1)

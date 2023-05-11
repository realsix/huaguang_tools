import os

import cv2


def makeVideo(path, size,name):
    filelist = os.listdir(path)
    #print(filelist[0].split('.')[0])
    filelist.sort(key=lambda x: int(x.split('.')[0][4:]))
    filelist2 = [os.path.join(path, i) for i in filelist]

    print(filelist2)
    fps = 15  # 我设定位视频每秒1帧，可以自行修改
    # size = (1920, 1080)  # 需要转为视频的图片的尺寸，这里必须和图片尺寸一致
    video = cv2.VideoWriter(path + "\\"+ name+ ".avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps,
                            size)

    for item in filelist2:
        print(item)
        if item.endswith('.jpg'):
            print(item)
            img = cv2.imread(item)
            video.write(img)

    video.release()
    cv2.destroyAllWindows()
    print('视频合成生成完成啦')


if __name__ == '__main__':
    path = r'C:\Users\ReaLSix\Desktop\left/'
    size=(320,240)
    makeVideo(path,size,'left0819')
from control import shijue1
import cv2


a = shijue1.Img()
num = '0'
for i in range(1000):
    a.get_img()
    a.show_image('img')
    a.color_detect_init('blue')
    a.color_detect()
    cv2.imwrite('./'+num+'/'+num + '_' + str(i)+'.jpg', a.img_new)

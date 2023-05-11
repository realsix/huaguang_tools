import os
from sklearn.model_selection import train_test_split
import random
import shutil
imgpath = r'Q:\datasets\custom\ball_final\imgs/'
xmlpath = r'Q:\datasets\custom\ball_final\anno/'
img_list = os.listdir(imgpath)
xml_list = os.listdir(xmlpath)

move_patn = r'Q:\datasets\custom\ball_final/'
for img,xml in list(zip(img_list,xml_list)):
    if img[:-4] == xml[:-4]:
        if random.random() > 0.7:
            shutil.copy(imgpath+img,move_patn + 'train/img')
            shutil.copy(xmlpath + xml, move_patn + 'train/xml')
        else:
            shutil.copy(imgpath + img, move_patn + 'test/img')
            shutil.copy(xmlpath + xml, move_patn + 'test/xml')




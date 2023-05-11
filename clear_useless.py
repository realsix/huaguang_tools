import os

import cv2

path = r'Q:\datasets\custom\footfinal\images'
xml_path = r'Q:\datasets\custom\footfinal\anno'
label_list = []
img_list = []
useless = []


for img in os.listdir(path):
    img_list.append(int(img[:-4]))

for label in os.listdir(xml_path):
    label_list.append(int(label[:-4]))


for img in img_list:
    if img not in label_list:
        useless.append(int(img))

# print(sorted(useless))
# useless=[]
# for xml in label_list:
#     if xml not in img_list:
#         useless.append(xml)
print(sorted(useless))

for img in os.listdir(path):
    if int(img[:-4]) not in useless:
        im = cv2.imread(path+img)
        # cv2.imwrite(r"D:\python\myProject\NLP_project\img/"+img, im)
for img in img_list:
    if img in useless:
        continue
    impath = path+'/'+str(img)+'.jpg'
    print(impath)
    im = cv2.imread(impath)
    cv2.imwrite(r'Q:\datasets\custom\footfinal\finalimg/'+str(img)+'.jpg',im)
import os

path = r'Q:\datasets\custom\footfinal\images/'
count=1000
filelist = os.listdir(path)
#filelist.sort(key=lambda x: int(x.split('.')[0][4:]))
for i in filelist:
    os.rename(path+i,path+str(count)+'.jpg')
    #print(i)
    count+=1

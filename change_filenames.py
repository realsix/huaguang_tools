import os


path = r'Q:\datasets\custom\ball_final\image/'

listpath = os.listdir(path)
for i, name in enumerate(listpath):
    # newname = name.replace('foot2','')
    # os.rename(path+'/'+name,path+'/'+'wonder_'+str(i)+'.jpg')
    os.rename(path + name, path + str(i) + '.jpg')


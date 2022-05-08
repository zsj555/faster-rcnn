import os
import frcnn
import get_map
path = "logs" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称

files.sort() #排序
for file in files: #遍历文件夹
     if file.endswith('.pth'):
          frcnn.string=path+"/"+file
          get_map.run()
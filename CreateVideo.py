import os
from turtle import done
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height,width,channel = frame.shape
size = (height,width)
print(size)
sans = cv2.VideoWriter("sundown.mp4",cv2.VideoWriter_fourcc(*'DIVX'),10,size)
for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    sans.write(frame)
sans.release()
print("done")

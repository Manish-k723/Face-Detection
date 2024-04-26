# import tensorflow
import cv2
from mtcnn import MTCNN

detector = MTCNN()

sample_img = cv2.imread('ActorsFaceData\Rohit Kohli\Image_1.jpg')
results = detector.detect_faces(sample_img)

x,y,width,height = results[0]['box']

face = sample_img[y:y+height,x:x+width] #It will zoom out at the image

color = (0, 255, 0)  # Green color (BGR format)
thickness = 2 
cv2.rectangle(sample_img, (x, y), (x + width, y + height), color, thickness)

cv2.imshow('Detected Face', sample_img)
cv2.waitKey(0)
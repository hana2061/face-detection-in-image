import cv2
import cv2.data
path=cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
modal=cv2.CascadeClassifier(path)

image=cv2.imread("./download.jpg")
faces= modal.detectMultiScale(image , 1.3 , 5)

for face in faces:
    x,y,w,h= face
    rect=cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),2)


cv2.imshow("shahrukh",image)
cv2.waitKey(0)
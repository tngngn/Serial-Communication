import cv2
import serial
import time

cap = cv2.VideoCapture(0)
ser = serial.Serial("COM4",'9600',timeout=2)

m = 0

#tracker = cv2.TrackerMOSSE_create()
tracker = cv2.TrackerCSRT_create()
success, img = cap.read()
bbox = cv2.selectROI("Tracking", img, False)
tracker.init(img, bbox)


def drawBox(img, bbox):
x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
cv2.rectangle(img, (x,y), ((x+w),(y+h)), (0,250,20), 3, 1)


while True:


timer = cv2.getTickCount()
success, img = cap.read()
success, bbox = tracker.update(img)



g = int(bbox[0])
i = int(g/10)

print(str(i))

if success:
drawBox(img, bbox)
else:
cv2.putText(img,"Lost",(15,75),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,(0,250,20),1)

ser.write((str(i)+'a').encode('utf-8'))


fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
cv2.putText(img,str(fps),(15,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,(0,250,20),1)
cv2.putText(img,str(bbox),(15,75),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,(0,250,20),1)
cv2.putText(img,str(i),(15,100),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,(0,250,20),1)
cv2.imshow("Tracking",img)

if cv2.waitKey(1) & 0xff == ord('q'):
break

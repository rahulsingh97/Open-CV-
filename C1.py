import cv2

cap=cv2.VideoCapture(0)
cap.set(3,1280) #Width
cap.set(4,720) #Height
cap.set(10,100) #Bightness

while True:
    success, img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'): #q to exit
        break

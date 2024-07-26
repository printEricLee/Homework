import cv2 

cap = cv2.VideoCapture('train_video/thumb.mp4')

while True:  
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
        cv2.imshow('video', frame)
    else:
        break
    if cv2.waitKey(10) == ord('q'):
        break
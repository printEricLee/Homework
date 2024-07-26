import cv2

# for img and etc
# Load the image using Pillow
img = cv2.imread('train_pic/preview.jpg')

# change img size
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

# Display the image using OpenCV
cv2.imshow('img', img)
cv2.waitKey(2000) # 0 == alwaty show 1000 == 1 s ....
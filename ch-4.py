import cv2
import numpy as np

img = np.zeros((512,512, 3), np.uint8)

# print(img)
# img[:] = 255, 174, 0 #! opencv uses BGR instead of RGB
# img[200:300, 200:300] = 0, 174, 255

# cv2.line(img, (0,0), (300, 300), (0, 174, 255), 3)
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 174, 255), 3) #& img.shape[height(0) : width(1) : channels(2)]
cv2.rectangle(img, (0,0), (250,350), (0, 0, 255), 3)
# cv2.rectangle(img, (0,0), (250,350), (0, 0, 255), cv2.FILLED) #* fill the rectange
cv2.circle(img, (256,256), 64, (255, 174, 0), 3)

cv2.putText(img, "namaste", (100,400), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 3)
# cv2.putText(img, "text", coordinates, font, scale, colour, thickness)

cv2.imshow("Image", img)
cv2.waitKey(0)
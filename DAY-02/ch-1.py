import cv2

#& to import images
# img = cv2.imread("Resources/one piece.png")
# cv2.imshow("Output", img)
# cv2.waitKey(0) #& 0 means to wait for infinite time
# cv2.destroyAllWindows()


#& to import video
# vid = cv2.VideoCapture("Resources/video.mp4")

# while True:
#     success, frame = vid.read()
#     cv2.imshow("Video", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# vid.release()


#& to capture webcam live video
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
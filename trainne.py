import cv2

camera = cv2.VideoCapture(0)
amostra = 1

while True:
    check, img = camera.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        imgR = cv2.resize(imgGray, (220, 220))
        cv2.imwrite(f"fotos/p/im{amostra}.jpg", imgR)
        amostra += 1

    cv2.imshow('camera', img)
    cv2.waitKey(1)


import cv2
import pickle
import numpy as np

vagas= []
with open('vagas.pkl', 'rb') as arquivo:
    vagas = pickle.load(arquivo)

video = cv2.VideoCapture('video.mp4')

while True:
    check, img = video.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgTh  = cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,25,16)
    imgMedian = cv2.medianBlur(imgTh,5)
    kernel = np.ones((3,3),np.int8)
    imgDil = cv2.dilate(imgMedian, kernel)

    vagasAbertas = 0

    for x,y,l,a in vagas:
        vaga = imgDil[y:y+a, x:x+l]
        count = cv2.countNonZero(vaga)
        #cv2.putText(img, str(count),(x,y+ a - 10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)
        cv2.rectangle(img, (x,y),(x+l,y+a), (255,0,0),2)

        if count <700:
            cv2.rectangle(img,(x,y), (x+l,y+a), (0,255,0),2)
            vagasAbertas+=1
        else:
            cv2.rectangle(img, (x,y), (x+l,y+a),(0,0,255),2)

    cv2.putText(img,f"Vagas Disponiveis: {vagasAbertas} de 69",(35,35), cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0),2)

    cv2.imshow('Estacionamento', img)
    cv2.waitKey(10)
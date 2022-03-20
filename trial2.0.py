# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 15:42:41 2021

@author: shash
"""


import cv2 as cv
import mediapipe as mp
import os

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
drawing_styles = mp.solutions.drawing_styles


cap = cv.VideoCapture(0)

## Video Writer
fourcc = cv.VideoWriter_fourcc(*'DIVX')
out = cv.VideoWriter('output2.0.avi', fourcc, 20.0, (640, 480))

fingerClick = []

folderPath = "sounds"
mylist = os.listdir(folderPath)
print(mylist)


with mp_hands.Hands(min_detection_confidence = 0.6) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret :
            print("Can't receive frame (streaming end?). Exting...")
            continue
        
        frame = cv.flip(frame, 1)
        
        ## Optional Writablity to pass by ref
        #frame.flags.writeable = False
        results = hands.process(frame)
        
        #lmlist = hands.findPositions(results)
        #print(lmlist)
        
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                          drawing_styles.get_default_hand_landmark_style(),
                                          drawing_styles.get_default_hand_connection_style())
                
        
           # for ()
        
        
        
        out.write(frame)
        
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break
    

## Releasing everything
        
cap.release()
out.release()
cv.destroyAllWindows()
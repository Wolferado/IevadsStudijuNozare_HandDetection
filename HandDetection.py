#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Installing necessary libraries
get_ipython().system('pip install mediapipe opencv-python')


# In[7]:


import mediapipe as mp 
import cv2
import numpy as np
import uuid
import os

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Create a directory if doesn't exist
if os.path.exists('Output Images') == False:
    os.mkdir('Output Images')

# Enable a camera
cap = cv2.VideoCapture(0)
            
def writeLetter(letter):
    cv2.putText(image, letter, (10,30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

def defineLetter(hand):
    # Letter A
    if (results.multi_hand_landmarks[hand].landmark[3].x > results.multi_hand_landmarks[hand].landmark[4].x and 
        results.multi_hand_landmarks[hand].landmark[4].y > results.multi_hand_landmarks[hand].landmark[10].y and
        results.multi_hand_landmarks[hand].landmark[4].y < results.multi_hand_landmarks[hand].landmark[11].y and
        results.multi_hand_landmarks[hand].landmark[12].y > results.multi_hand_landmarks[hand].landmark[11].y and 
        results.multi_hand_landmarks[hand].landmark[16].y > results.multi_hand_landmarks[hand].landmark[15].y and 
        results.multi_hand_landmarks[hand].landmark[20].y > results.multi_hand_landmarks[hand].landmark[19].y and
        results.multi_hand_landmarks[hand].landmark[2].z < results.multi_hand_landmarks[hand].landmark[5].z):
        writeLetter("A")

    # Letter B
    elif (results.multi_hand_landmarks[hand].landmark[3].x < results.multi_hand_landmarks[hand].landmark[4].x and
        results.multi_hand_landmarks[hand].landmark[5].y > results.multi_hand_landmarks[hand].landmark[8].y and
        results.multi_hand_landmarks[hand].landmark[9].y > results.multi_hand_landmarks[hand].landmark[12].y and 
        results.multi_hand_landmarks[hand].landmark[13].y > results.multi_hand_landmarks[hand].landmark[16].y and 
        results.multi_hand_landmarks[hand].landmark[17].y > results.multi_hand_landmarks[hand].landmark[20].y and
        results.multi_hand_landmarks[hand].landmark[1].z < results.multi_hand_landmarks[hand].landmark[0].z):
        writeLetter("B")

    # Letter C
    elif (results.multi_hand_landmarks[hand].landmark[1].x < results.multi_hand_landmarks[hand].landmark[2].x and
        results.multi_hand_landmarks[hand].landmark[3].x < results.multi_hand_landmarks[hand].landmark[4].x and
        results.multi_hand_landmarks[hand].landmark[7].x < results.multi_hand_landmarks[hand].landmark[8].x and
        results.multi_hand_landmarks[hand].landmark[9].x < results.multi_hand_landmarks[hand].landmark[10].x and
        results.multi_hand_landmarks[hand].landmark[11].x < results.multi_hand_landmarks[hand].landmark[12].x and
        results.multi_hand_landmarks[hand].landmark[13].x < results.multi_hand_landmarks[hand].landmark[14].x and
        results.multi_hand_landmarks[hand].landmark[15].x < results.multi_hand_landmarks[hand].landmark[16].x and
        results.multi_hand_landmarks[hand].landmark[17].x < results.multi_hand_landmarks[hand].landmark[18].x and
        results.multi_hand_landmarks[hand].landmark[19].x < results.multi_hand_landmarks[hand].landmark[20].x and
        results.multi_hand_landmarks[hand].landmark[5].x < results.multi_hand_landmarks[hand].landmark[6].x and
        results.multi_hand_landmarks[hand].landmark[1].y > results.multi_hand_landmarks[hand].landmark[4].y and
        results.multi_hand_landmarks[hand].landmark[5].y > results.multi_hand_landmarks[hand].landmark[6].y):
        writeLetter("C")

    # Letter D
    elif (results.multi_hand_landmarks[hand].landmark[4].x > results.multi_hand_landmarks[hand].landmark[1].x and
        results.multi_hand_landmarks[hand].landmark[8].y < results.multi_hand_landmarks[hand].landmark[7].y and
        results.multi_hand_landmarks[hand].landmark[12].y < results.multi_hand_landmarks[hand].landmark[11].y and
        results.multi_hand_landmarks[hand].landmark[16].y > results.multi_hand_landmarks[hand].landmark[14].y and
        results.multi_hand_landmarks[hand].landmark[20].y > results.multi_hand_landmarks[hand].landmark[19].y and
        results.multi_hand_landmarks[hand].landmark[4].z < results.multi_hand_landmarks[hand].landmark[8].z):
        writeLetter("D")

    # Letter E (make it more constant or overlaps many letters)
    elif (results.multi_hand_landmarks[hand].landmark[20].x > results.multi_hand_landmarks[hand].landmark[17].x and
        results.multi_hand_landmarks[hand].landmark[4].x > results.multi_hand_landmarks[hand].landmark[16].x and
        results.multi_hand_landmarks[hand].landmark[16].x > results.multi_hand_landmarks[hand].landmark[13].x and
        results.multi_hand_landmarks[hand].landmark[12].x > results.multi_hand_landmarks[hand].landmark[9].x and
        results.multi_hand_landmarks[hand].landmark[8].x > results.multi_hand_landmarks[hand].landmark[5].x and
        results.multi_hand_landmarks[hand].landmark[1].y > results.multi_hand_landmarks[hand].landmark[4].y and
        results.multi_hand_landmarks[hand].landmark[20].z < results.multi_hand_landmarks[hand].landmark[4].z):
        writeLetter("E")

    # Letter F
    elif (results.multi_hand_landmarks[hand].landmark[1].x < results.multi_hand_landmarks[hand].landmark[2].x and
        results.multi_hand_landmarks[hand].landmark[3].x+10 > results.multi_hand_landmarks[hand].landmark[4].x and
        results.multi_hand_landmarks[hand].landmark[5].x < results.multi_hand_landmarks[hand].landmark[6].x and
        results.multi_hand_landmarks[hand].landmark[7].x < results.multi_hand_landmarks[hand].landmark[8].x and
        results.multi_hand_landmarks[hand].landmark[9].x < results.multi_hand_landmarks[hand].landmark[10].x and
        results.multi_hand_landmarks[hand].landmark[11].x < results.multi_hand_landmarks[hand].landmark[12].x and
        results.multi_hand_landmarks[hand].landmark[13].x < results.multi_hand_landmarks[hand].landmark[14].x and
        results.multi_hand_landmarks[hand].landmark[15].x < results.multi_hand_landmarks[hand].landmark[16].x and
        results.multi_hand_landmarks[hand].landmark[17].x < results.multi_hand_landmarks[hand].landmark[20].x and
        results.multi_hand_landmarks[hand].landmark[2].y > results.multi_hand_landmarks[hand].landmark[4].y and
        results.multi_hand_landmarks[hand].landmark[4].z > results.multi_hand_landmarks[hand].landmark[20].z):
        writeLetter("F") 
    
    # Letter G
    elif (results.multi_hand_landmarks[hand].landmark[7].x < results.multi_hand_landmarks[hand].landmark[6].x and
        results.multi_hand_landmarks[hand].landmark[11].x < results.multi_hand_landmarks[hand].landmark[10].x and 
        results.multi_hand_landmarks[hand].landmark[15].x < results.multi_hand_landmarks[hand].landmark[14].x and
        results.multi_hand_landmarks[hand].landmark[19].x < results.multi_hand_landmarks[hand].landmark[18].x and
        results.multi_hand_landmarks[hand].landmark[4].x > results.multi_hand_landmarks[hand].landmark[17].x and
        results.multi_hand_landmarks[hand].landmark[3].x < results.multi_hand_landmarks[hand].landmark[4].x and
        results.multi_hand_landmarks[hand].landmark[1].y > results.multi_hand_landmarks[hand].landmark[3].y):
        writeLetter("G")

    # Letter H
    elif (results.multi_hand_landmarks[hand].landmark[13].x < results.multi_hand_landmarks[hand].landmark[16].x and
        results.multi_hand_landmarks[hand].landmark[17].y > results.multi_hand_landmarks[hand].landmark[20].y and
        results.multi_hand_landmarks[hand].landmark[9].y > results.multi_hand_landmarks[hand].landmark[12].y and
        results.multi_hand_landmarks[hand].landmark[5].y > results.multi_hand_landmarks[hand].landmark[8].y and
        results.multi_hand_landmarks[hand].landmark[1].y > results.multi_hand_landmarks[hand].landmark[4].y and
        results.multi_hand_landmarks[hand].landmark[1].x > results.multi_hand_landmarks[hand].landmark[4].x and
        results.multi_hand_landmarks[hand].landmark[13].y < results.multi_hand_landmarks[hand].landmark[16].y):
        writeLetter("H") 

    # Letter I
    elif (results.multi_hand_landmarks[hand].landmark[3].x > results.multi_hand_landmarks[hand].landmark[4].x and
        results.multi_hand_landmarks[hand].landmark[17].y > results.multi_hand_landmarks[hand].landmark[20].y and
        results.multi_hand_landmarks[hand].landmark[13].y < results.multi_hand_landmarks[hand].landmark[16].y and
        results.multi_hand_landmarks[hand].landmark[9].y < results.multi_hand_landmarks[hand].landmark[12].y and
        results.multi_hand_landmarks[hand].landmark[5].y < results.multi_hand_landmarks[hand].landmark[8].y and
        results.multi_hand_landmarks[hand].landmark[1].y > results.multi_hand_landmarks[hand].landmark[3].y):
        writeLetter("I")

    # Letter J
    elif (results.multi_hand_landmarks[hand].landmark[1].x < results.multi_hand_landmarks[hand].landmark[4].x and
        results.multi_hand_landmarks[hand].landmark[17].x < results.multi_hand_landmarks[hand].landmark[20].x and
        results.multi_hand_landmarks[hand].landmark[1].y < results.multi_hand_landmarks[hand].landmark[4].y and
        results.multi_hand_landmarks[hand].landmark[5].y < results.multi_hand_landmarks[hand].landmark[7].y and
        results.multi_hand_landmarks[hand].landmark[9].y < results.multi_hand_landmarks[hand].landmark[11].y and
        results.multi_hand_landmarks[hand].landmark[13].y < results.multi_hand_landmarks[hand].landmark[15].y and
        results.multi_hand_landmarks[hand].landmark[17].y < results.multi_hand_landmarks[hand].landmark[20].y):
        writeLetter("J")

    # Letter K (must complete)
    elif (results.multi_hand_landmarks[hand].landmark[1].x < results.multi_hand_landmarks[hand].landmark[4].x and
        results.multi_hand_landmarks[hand].landmark[8].x > results.multi_hand_landmarks[hand].landmark[5].x and
        results.multi_hand_landmarks[hand].landmark[12].x > results.multi_hand_landmarks[hand].landmark[9].x and
        results.multi_hand_landmarks[hand].landmark[13].x < results.multi_hand_landmarks[hand].landmark[15].x and
        results.multi_hand_landmarks[hand].landmark[17].x < results.multi_hand_landmarks[hand].landmark[19].x and
        results.multi_hand_landmarks[hand].landmark[12].y < results.multi_hand_landmarks[hand].landmark[9].y and
        results.multi_hand_landmarks[hand].landmark[1].y < results.multi_hand_landmarks[hand].landmark[4].y and
        results.multi_hand_landmarks[hand].landmark[8].y < results.multi_hand_landmarks[hand].landmark[5].y and
        results.multi_hand_landmarks[hand].landmark[8].z < results.multi_hand_landmarks[hand].landmark[15].z and
        results.multi_hand_landmarks[hand].landmark[12].z < results.multi_hand_landmarks[hand].landmark[19].z):
        writeLetter("K")

    # Letter L
    elif (results.multi_hand_landmarks[hand].landmark[2].x < results.multi_hand_landmarks[hand].landmark[4].x and
        results.multi_hand_landmarks[hand].landmark[6].y > results.multi_hand_landmarks[hand].landmark[8].y and
        results.multi_hand_landmarks[hand].landmark[11].y < results.multi_hand_landmarks[hand].landmark[12].y and
        results.multi_hand_landmarks[hand].landmark[15].y < results.multi_hand_landmarks[hand].landmark[16].y and
        results.multi_hand_landmarks[hand].landmark[19].y < results.multi_hand_landmarks[hand].landmark[20].y and
        results.multi_hand_landmarks[hand].landmark[10].z <= results.multi_hand_landmarks[hand].landmark[5].z):
        writeLetter("L")

    # Letter M
    elif (results.multi_hand_landmarks[hand].landmark[1].x > results.multi_hand_landmarks[hand].landmark[4].x and
        results.multi_hand_landmarks[hand].landmark[17].x < results.multi_hand_landmarks[hand].landmark[20].x and
        results.multi_hand_landmarks[hand].landmark[3].x > results.multi_hand_landmarks[hand].landmark[20].x and
        results.multi_hand_landmarks[hand].landmark[1].y > results.multi_hand_landmarks[hand].landmark[4].y and
        results.multi_hand_landmarks[hand].landmark[17].y < results.multi_hand_landmarks[hand].landmark[20].y and
        results.multi_hand_landmarks[hand].landmark[13].y > results.multi_hand_landmarks[hand].landmark[16].y and
        results.multi_hand_landmarks[hand].landmark[9].y > results.multi_hand_landmarks[hand].landmark[12].y and
        results.multi_hand_landmarks[hand].landmark[5].y > results.multi_hand_landmarks[hand].landmark[8].y and
        results.multi_hand_landmarks[hand].landmark[4].z < results.multi_hand_landmarks[hand].landmark[8].z):
        writeLetter("M")

    # Letter N
    elif (results.multi_hand_landmarks[hand].landmark[1].x > results.multi_hand_landmarks[hand].landmark[4].x and
        results.multi_hand_landmarks[hand].landmark[1].y > results.multi_hand_landmarks[hand].landmark[4].y and
        results.multi_hand_landmarks[hand].landmark[17].y < results.multi_hand_landmarks[hand].landmark[20].y and
        results.multi_hand_landmarks[hand].landmark[13].y < results.multi_hand_landmarks[hand].landmark[16].y and
        results.multi_hand_landmarks[hand].landmark[9].y > results.multi_hand_landmarks[hand].landmark[12].y and
        results.multi_hand_landmarks[hand].landmark[5].y > results.multi_hand_landmarks[hand].landmark[8].y and
        results.multi_hand_landmarks[hand].landmark[4].z < results.multi_hand_landmarks[hand].landmark[8].z):
        writeLetter("N")

    # Letter O (have to finish)
    elif (results.multi_hand_landmarks[hand].landmark[1].x < results.multi_hand_landmarks[hand].landmark[3].x and
        results.multi_hand_landmarks[hand].landmark[3].x > results.multi_hand_landmarks[hand].landmark[4].x and
        results.multi_hand_landmarks[hand].landmark[5].x < results.multi_hand_landmarks[hand].landmark[7].x and
        results.multi_hand_landmarks[hand].landmark[7].x < results.multi_hand_landmarks[hand].landmark[8].x and
        results.multi_hand_landmarks[hand].landmark[1].y > results.multi_hand_landmarks[hand].landmark[3].y and
        results.multi_hand_landmarks[hand].landmark[3].y > results.multi_hand_landmarks[hand].landmark[4].y and
        results.multi_hand_landmarks[hand].landmark[5].y > results.multi_hand_landmarks[hand].landmark[7].y and
        results.multi_hand_landmarks[hand].landmark[7].y < results.multi_hand_landmarks[hand].landmark[8].y and
        results.multi_hand_landmarks[hand].landmark[9].y > results.multi_hand_landmarks[hand].landmark[12].y and
        results.multi_hand_landmarks[hand].landmark[13].y > results.multi_hand_landmarks[hand].landmark[16].y and
        results.multi_hand_landmarks[hand].landmark[17].y > results.multi_hand_landmarks[hand].landmark[20].y):
        writeLetter("O")

    # Letter P (have to finish)
    elif (results.multi_hand_landmarks[hand].landmark[1].x < results.multi_hand_landmarks[hand].landmark[3].x and
        results.multi_hand_landmarks[hand].landmark[9].x < results.multi_hand_landmarks[hand].landmark[12].x and
        results.multi_hand_landmarks[hand].landmark[17].x < results.multi_hand_landmarks[hand].landmark[19].x and
        results.multi_hand_landmarks[hand].landmark[13].x < results.multi_hand_landmarks[hand].landmark[16].x and
        results.multi_hand_landmarks[hand].landmark[19].x < results.multi_hand_landmarks[hand].landmark[20].x and
        results.multi_hand_landmarks[hand].landmark[17].y > results.multi_hand_landmarks[hand].landmark[19].y and
        results.multi_hand_landmarks[hand].landmark[19].y < results.multi_hand_landmarks[hand].landmark[20].y and
        results.multi_hand_landmarks[hand].landmark[3].y > results.multi_hand_landmarks[hand].landmark[4].y and
        results.multi_hand_landmarks[hand].landmark[1].y > results.multi_hand_landmarks[hand].landmark[3].y and
        results.multi_hand_landmarks[hand].landmark[5].y > results.multi_hand_landmarks[hand].landmark[8].y):
        writeLetter("P")

    # Letter R


    # Letter S


    # Letter T


    # Letter U


    # Letter V


    # Letter Z


    else:
        return "Letter not found"


# Create a mask for the hands
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.7, max_num_hands=1) as hands:
    while cap.isOpened():
        ret, frame = cap.read()

        # Color and Flag Setup
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, 1)
        image.flags.writeable = False

        # Detections
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Change masks of the hands (remove comment sign to make hand masks visible)
        # if results.multi_hand_landmarks:
        #    for num, hand in enumerate(results.multi_hand_landmarks):
        #        mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
        #            mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=4),
        #            mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2))
        
        if results.multi_handedness != None:
            try:
                index = results.multi_handedness[0].classification[0].index
                defineLetter(index)
            except:
                print()

        # Open a window to show the hands
        cv2.imshow('Hand Tracking', image)
        
        # Exit statement
        if cv2.waitKey(10) & 0xFF == 27:
            #cv2.imwrite(os.path.join('Output Images', "{}.png".format(uuid.uuid1())), image) # Saves the image
            break

cap.release()
cv2.destroyAllWindows()


# "Sign Language Detection and Display" Prototype

## IMPORTANT NOTE!
This project has been **archived** due to unability to develop it further.

Reasons:
- Mediapipe library is unable to get installed on Python with version newer or equal 3.9.

Even though it is theoretically (even practically) possible, I'm not willing to get out of my way to downgrade Python's version for the sake of this project, no matter the good that can come out of it.

Note will be removed, if my decision will change. 
##

This repository contains a Jupiter Notebook with created program _(prototype)_, that takes your Webcam Video as an input and scans it for any hand signs _(from the Latvian Sign Language)_. The goal of the program is to display needed sign based on the hand and fingers positions.

Created program language is Python.

MediaPipe Hands Solution API is used to track hands and make it available to detect hands and display necessary letters based on the hand landmarks.

API: _https://google.github.io/mediapipe/solutions/hands_

The prototype was created with a purpose to make deaf and/or numb people communicate easier with other people who don't know the sign language.

The list of available signs is available here: 

<img src="https://github.com/Wolferado/IevadsStudijuNozare_HandDetection/blob/main/Images%20for%20Markdown/available_signs.png" width="60%" height="60%" alt="https://github.com/Wolferado/IevadsStudijuNozare_HandDetection/blob/main/Images%20for%20Markdown/available_signs.png">

<div align="center">

The view of the program:
  
<img src="https://github.com/Wolferado/IevadsStudijuNozare_HandDetection/blob/main/Images%20for%20Markdown/letterA_detection.jpeg" width="49%" height="49%" alt="https://github.com/Wolferado/IevadsStudijuNozare_HandDetection/blob/main/Images%20for%20Markdown/letterA_detection.jpeg">
<img src="https://github.com/Wolferado/IevadsStudijuNozare_HandDetection/blob/main/Images%20for%20Markdown/letterU_detection.jpeg" width="49%" height="49%" alt="https://github.com/Wolferado/IevadsStudijuNozare_HandDetection/blob/main/Images%20for%20Markdown/letterU_detection.jpeg">
  
</div>

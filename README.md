# "Sign Language Detection and Display" Prototype

> [!WARNING]
> This project has been archived due to these reasons:
> - It has basic functionality that was necessary to develop during production time for university course.

> [!IMPORTANT]
> Bear in mind that this project has been created in 2021 and is extremely outdated, both in terms of code writing and logic thinking.
> 
> Recent changes in the code are necessary for bachelor's thesis.

> [!NOTE]
> This repository contains a Jupiter Notebook with created program _(prototype)_, that takes your Webcam Video as an input and scans it for static hand signs _(from the Latvian Sign Language)_.
>
> The goal of the program is to display needed sign based on the hand and fingers positions.

[MediaPipe Hands Solution API](https://github.com/google-ai-edge/mediapipe) is used to track hands and make it available to detect hands and display necessary letters based on the hand landmarks.

Documentation used: [MediaPipe Hands Solution API Docs](https://github.com/google-ai-edge/mediapipe/blob/master/docs/solutions/hands.md)

### The table of available signs is available here _(only outlined signs are implemented)_: 

<img src="https://github.com/Wolferado/IevadsStudijuNozare_HandDetection/blob/main/Images%20for%20Markdown/available_signs.png" width="40%" height="40%" alt="https://github.com/Wolferado/IevadsStudijuNozare_HandDetection/blob/main/Images%20for%20Markdown/available_signs.png">

### The view of the program:

<div align="start">
  
<img src="https://github.com/Wolferado/IevadsStudijuNozare_HandDetection/blob/main/Images%20for%20Markdown/letterA_detection.jpeg" width="45%" height="45%" alt="https://github.com/Wolferado/IevadsStudijuNozare_HandDetection/blob/main/Images%20for%20Markdown/letterA_detection.jpeg">
<img src="https://github.com/Wolferado/IevadsStudijuNozare_HandDetection/blob/main/Images%20for%20Markdown/letterU_detection.jpeg" width="45%" height="45%" alt="https://github.com/Wolferado/IevadsStudijuNozare_HandDetection/blob/main/Images%20for%20Markdown/letterU_detection.jpeg">
  
</div>

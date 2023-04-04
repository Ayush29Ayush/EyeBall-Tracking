#compile and Run or share in any language
"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
import winsound
import os
import pyttsx3
import time

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

duration = 1000 # milliseconds
freq = 440 # Hz

engine = pyttsx3.init()

total_time = 0

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_right():
        text = "Looking right"
        start = time.time()
        if start != -1234:
            time.sleep(1/60)
            end = time.time()
            elapsed_time = end - start
            # print(elapsed_time)
            total_time = elapsed_time+total_time
            print(total_time, "Right")
            if(total_time>2):
                engine.say("Looking Right, please look at center")
                engine.runAndWait()
                total_time = 0
    
    elif gaze.is_left():
        
        text = "Looking left"
        start = time.time()
        if start != -1234:
            time.sleep(1/60)
            end = time.time()
            elapsed_time = end - start
            # print(elapsed_time)
            total_time = elapsed_time+total_time
            print(total_time, "Left")
            if(total_time>2):
                engine.say("Looking Left, please look at center")
                engine.runAndWait()
                total_time = 0

    elif gaze.is_center():
        text = "Looking center"
        total_time = 0

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
   
webcam.release()
cv2.destroyAllWindows()

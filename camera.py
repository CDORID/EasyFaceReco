# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:41:26 2019

@author: Romain

improving the model has to be a priority 

https://www.learnopencv.com/face-detection-opencv-dlib-and-deep-learning-c-python/


get more computing power : 
    
    https://towardsdatascience.com/inference-on-the-edge-21234ea7633
    
use strategies over the cv function : 
    
    https://www.analyticsvidhya.com/blog/2019/03/opencv-functions-computer-vision-python/
        - adding image rotation
        - image translation : or decoupage
"""



import cv2
import pandas as pd


def init(video_width, video_height, distance_parameter ):
    
    print('Initializing Camera...')
    users = pd.read_csv('users.csv')
    max_id = max(users['id_user'])
    print(max_id)
    
    
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);

    font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, video_width) # set video widht
    cam.set(4, video_height) # set video height
    
# Define min window size to be recognized as a face
    minW = distance_parameter*cam.get(3)
    minH = distance_parameter*cam.get(4)
    
    return cam, recognizer, minW, minH, font, faceCascade, users, max_id
    
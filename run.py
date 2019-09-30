''''
Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition    
and Marcelo Rovai - MJRoBot.org @ 21Feb18    

Developed by Romain VIGIE

'''
import cv2
import numpy as np
import os 

import pandas as pd
import argparse


import camera
import user_functions
import model
import popups

## defining arguments thanks to the parser


parser = argparse.ArgumentParser(description='Welcome')
parser.add_argument('-photos', type=int, 
                    dest = 'photo_number', help='number of photo taken for the training', default = 90)
parser.add_argument('-w', dest='video_width', type = int, 
                    default=1080, help='width of the video taken')
parser.add_argument('--h', dest='video_height', type = int, 
                    default=720, help='height of the video taken')
parser.add_argument('-d', dest='distance', type = float, 
                    default=0.95, help='index over the distance covered over 100')

args = parser.parse_args()
print(args)


photo_number = args.photo_number  ##number of photos taken for the recognition
video_width = args.video_width
video_height = args.video_height
distance = args.distance#index between 0 and 1, the higher, the more distance covered
distance_parameter = 1-distance



cam, recognizer, minW, minH, font, faceCascade, users, max_id  = camera.init(video_width, video_height, distance_parameter)
 
 
while True:
    id=0
    ret, img = cam.read()
    img = cv2.flip(img, 1) 

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        confidence = 100 - confidence
        # Check if confidence is less than 100 ==> "0" is perfect match 
        if (confidence > 50):
            
            id = list(users['name'][users['id_user'] == id])[0]
            confidence = "  {0}%".format(round(confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(confidence))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    
    
    
    if k == 27:
        break
    
    
    ## Press n to add a New user
    if k == ord('n'):
        count, name, face_id = user_functions.get_face(max_id,photo_number,video_width,video_height)
        
        cam.release()
        cv2.destroyAllWindows()
        
        if count == photo_number :
            
            new_user = pd.DataFrame({'name':[str(name)],'id_user':[face_id]})
            users = users.append(new_user)
            users.to_csv('users.csv',index = False)
             
            model.train() 
            
            ##reset camera 
            cam, recognizer, minW, minH, font, faceCascade, users, max_id  = camera.init(video_width, video_height, distance_parameter)
 

        else:         
            del_user_id = face_id
            path = 'dataset'
            imagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
            
            for imagePath in imagePaths:
                
                photo = 0
                if int(os.path.split(imagePath)[-1].split(".")[1]) == del_user_id : 
                    os.remove(imagePath)
                    photo += 1
                    print(':)')
                else :
                    pass
                
            cam, recognizer, minW, minH, font, faceCascade, users, max_id  = camera.init(video_width, video_height, distance_parameter)
 
    #press d to Delete an user  
    if k == ord('d'):
            user_functions.delete()
            
            model.train()
            popups.timed_popup("Modèle réentrainé",3)
            
            cam.release()
    
            cv2.destroyAllWindows()
            
            ##reset camera 
            cam, recognizer, minW, minH, font, faceCascade, users, max_id  = camera.init(video_width, video_height, distance_parameter)
 
    #press l to get the List of the users registered      
    if k == ord('l'):
            user_functions.list_users()
    
        #press e to know if you Exist in the program    
    if k == ord('e'):
            user_functions.check_user()

        
    
    else:
        pass

# Do a bit of cleanup
        
popups.timed_popup("\n [INFO] Exiting Program and cleanup stuff",3)
cam.release()
cv2.destroyAllWindows()

''''
Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition    
and Marcelo Rovai - MJRoBot.org @ 21Feb18    

Developed by Romain

'''

import cv2
import os
import pandas as pd
from tkinter import * 
#import importlib
import popups
import model

def list_users():
    df = pd.read_csv('users.csv')
    print(df['name'])
    
    
def ask_delete():
    who = popups.popup('Quel utilisateur voulez-vous supprimer ?')  
    return who
    
def delete(who=None):
    
    users = pd.read_csv('users.csv')    
    if who == None : 
        who = ask_delete()
        
    del_user_id = users[users['name']==str(who)]['id_user']
        
    try :
        del_user_id = int(del_user_id)
    except TypeError:
        popups.timed_popup("Utilisateur non-existant, annulation du processus",3)
        return
        
    users = users[users['id_user']!= del_user_id]
    users.to_csv('users.csv', index = False)     
    
    
    path = 'dataset'
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
    
    for imagePath in imagePaths:
        
        photo = 0
        if int(os.path.split(imagePath)[-1].split(".")[1]) == del_user_id : 
            os.remove(imagePath)
            photo += 1
        
        else :
            pass
    
    popups.timed_popup(str("Photos de "+who+" supprimées :)"),3)


    

#https://stackoverflow.com/questions/4140437/interactively-validating-entry-widget-content-in-tkinter

# get and verify the popup name
def ask_name():
    new_name = popups.popup(message = "Bienvenue nouvel utilisateur ! Comment vous appelez-vous?")
    users = pd.read_csv('users.csv')
    list_names = list(users['name'])

    while new_name in list_names :
       
        new_name = popups.popup('Désolé, ce nom est déjà pris :( \n Pouvez vous rajouter votre nom de famille ? Ou sa première lettre ? :)')
    
    return new_name

def check_user() : 
    new_name = popups.popup(message = 'Quel est votre nom cher utilisateur potentiel ?')
    users = pd.read_csv('users.csv')
    list_names = list(users['name'])

    if new_name in list_names :
       
        popups.popup_no_input("Il y a quelqu'un de ce nom dans nos données")
    
    else : 
        popups.popup_no_input('Nous ne connaissons personne avec ce nom!')


    
def get_face(max_id, photo_number,video_width, video_height) :

    cam = cv2.VideoCapture(0)
    cam.set(3, video_width) # set video width
    cam.set(4, video_height) # set video height

    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
    face_id = max_id + 1
    
    name = ask_name()
    popups.timed_popup('Nous allons prendre une série de photo de vous. \n Regardez la caméra et veuillez patienter un instant :)')

# Initialize individual sampling face count
    count = 0

    while(True):

        ret, img = cam.read()
        img = cv2.flip(img, 1) # flip video image vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1

        # Save the captured image into the datasets folder
        
       
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= photo_number: # Take a certain number of face sample and stop video       
            break
    
    
    



# Do a bit of cleanup
    popups.timed_popup('Fin de la capture',2)

    cam.release()
    
    cv2.destroyAllWindows()
    

        

    return count, name, face_id



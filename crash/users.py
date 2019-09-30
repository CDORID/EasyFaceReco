# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 14:19:35 2019

@author: Romain
"""

import pandas as pd
import os
import importlib

def list_users():
    df = pd.read_csv('users.csv')
    print(df['name'])
    
def delete():
    
    users = pd.read_csv('users.csv')    
    who = input('\n type the userid to be deleted ==>  ')    
    del_user_id = users[users['name']==str(who)]['id_user']
        
    try :
        del_user_id = int(del_user_id)
    except TypeError:
        print('Non-existing user')
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
    
    print(photo, 'photos deleted')
    
    importlib.import_module('model').train()
    print('model retrained')
    

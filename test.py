# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:20:57 2019

@author: Romain
"""
import argparse

photo_number = 120 ##number of photos taken for the recognition
video_width = 1080
video_height = 720
distance = 0.9 #index between 0 and 1, the higher, the more distance covered


distance_parameter = 1-distance

parser = argparse.ArgumentParser(description='Welcome')
parser.add_argument('-photos', type=int, 
                    dest = 'photo_number', help='number of photo taken for the training', default = 90)
parser.add_argument('-w', dest='video_width', type = int, 
                    default=1080, help='width of the video taken')
parser.add_argument('--h', dest='video_height', type = int, 
                    default=720, help='height of the video taken')
parser.add_argument('-d', dest='distance', type = float, 
                    default=0.95, help='index over the distance covered')

args = parser.parse_args()
print(args)

photo_number = args.photo_number  ##number of photos taken for the recognition
video_width = args.video_width
video_height = args.video_height
distance = args.distance#index between 0 and 1, the higher, the more distance covered

print(photo_number)
print(distance)
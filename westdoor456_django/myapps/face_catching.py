# -*- coding: utf-8 -*-
import cv2
import face_recognition
from time import sleep
from myapps import cfr
from time import sleep

def face_catch(camera_no):
    captured = cv2.VideoCapture(camera_no)
    for count in range(5):
        ret, frame = captured.read()
        sleep(0.5)
        cv2.imwrite('myapps/reg_faces/'+str(count)+'.jpg', frame)
        cv2.imwrite('dashboard/static/face_recogg/face_catch/'+str(count)+'.jpg', frame)


def face_catching():
    face_catch(0)
    
    pictures = []
    for count in range(5):
        pictures.append(face_check(count, 'myapps/reg_faces/'+str(count)+'.jpg'))
    pictures = sorted(pictures, key=lambda picture: picture['confidence'])
    print(pictures[2:])

def get_face_location(path):
    image = face_recognition.load_image_file(path)
    return face_recognition.face_locations(image)

def face_check(count, path):
    if not get_face_location(path):
        return {'no': count, 'age':0, 'gender':0, 'confidence':0}
    res = cfr.cfr(path)
    if not res['faces']:
        return {'no': count, 'age':0, 'gender':0, 'confidence':0}
    face = res['faces'][0]
    gender_value = face['gender']['value']
    gender_confidence = face['gender']['confidence']
    age = face['age']['value']
    ages = age.split('~')
    age_value = (int(ages[0]) + int(ages[1]))/2
    #age_value = int(ages[0])
    age_confidence = face['age']['confidence']
    return {'no': count, 'age':age_value, 'gender':gender_value,'confidence':age_confidence+gender_confidence}

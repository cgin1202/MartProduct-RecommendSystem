import cv2
import face_recognition
import os
import sys

def get_face_location(img_path):
    image = face_recognition.load_image_file(img_path)
    return face_recognition.face_locations(image)


def face_trim(img_path):
    org_image = cv2.imread(img_path)
    face_locations = get_face_location(img_path)
    if face_locations:
        print(face_locations)
        y = face_locations[0][0]
        w = face_locations[0][1]
        h = face_locations[0][2]
        x = face_locations[0][3]
        img_trimed = org_image[y:h, x:w]
        img_path_split = os.path.splitext(img_path)
        img_trimed_path = img_path_split[0] + '_trimed' + img_path_split[1] 
        cv2.imwrite(img_trimed_path, img_trimed)
        return img_trimed_path
    else:
        print("No faces")
        return

if len(sys.argv) is 1:
    print("no image...");
img_path = './images/'
img_path += sys.argv[1]
trim_image = face_trim(img_path)

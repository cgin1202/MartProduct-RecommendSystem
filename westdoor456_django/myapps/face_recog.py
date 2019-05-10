import face_recognition
import cv2
import os
from . import camera
import numpy as np

#from pydb import dbconnection

class FaceRecog():
    def __init__(self, camera_no = 0):

        #conn = dbconnection()
        #curs = conn.cursor()
        self.camera = camera.VideoCamera(camera_no)
        self.camera_no = camera_no
        self.product_no = camera_no
        self.now_no = "Unknown"

        self.known_face_encodings = []
        self.known_face_names = []
        
        dirname = 'myapps/faces'
        files = os.listdir(dirname)
        for filename in files:
            name, ext = os.path.splitext(filename)
            if ext == '.jpg':
                self.known_face_names.append(name)
                pathname = os.path.join(dirname, filename)
                img = face_recognition.load_image_file(pathname)
                face_encoding = face_recognition.face_encodings(img)[0]
                self.known_face_encodings.append(face_encoding)


        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True

    def __del__(self):
        del self.camera

    def get_frame(self, mycol):
        frame = self.camera.get_frame()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        if self.process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            self.face_locations = face_recognition.face_locations(rgb_small_frame)
            self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

            self.face_names = []
            for face_encoding in self.face_encodings:

                name = "Unknown"
                
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding, 0.4)
                if True in matches:
                    first_match_index = matches.index(True)
                    name = self.known_face_names[first_match_index]
                '''
                distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                min_value = min(distances)

                if min_value < 0.4:
                    index = np.argmin(distances)
                    name = self.known_face_names[index]
                '''
                self.face_names.append(name)
        
        self.process_this_frame = not self.process_this_frame

        #디비 연동
        for id in self.face_names:
            self.now_no = id
            if id=="Unknown":
                continue
            mycol.update({'no':int(id)}, {'$inc':{'ratings.%d'%self.product_no:0.1}})


        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        return frame

    def get_jpg_bytes(self, mycol):
        frame = self.get_frame(mycol)
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpg = cv2.imencode('.jpg', frame)
        return jpg.tobytes()


if __name__ == '__main__':
    face_recog = FaceRecog()
    print(face_recog.known_face_names)
    while True:
        frame = face_recog.get_frame()

        # show the frame
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

    # do a bit of cleanup
    cv2.destroyAllWindows()
    print('finish')
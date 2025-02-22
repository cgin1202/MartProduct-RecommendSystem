import face_recognition
import cv2
import os
from pydb import dbconnection

conn = dbconnection()
curs = conn.cursor()

path = "./faces/"
file_list = os.listdir(path)
known_face_encodings = [
]
known_face_names = [
]

def face_compare(camera_no):
    video_capture = cv2.VideoCapture(camera_no)
    for file in file_list:
        fname, ext = os.path.splitext(file)
        if(ext in ['.jpg', '.jpeg', '.png']):
            face_image = face_recognition.load_image_file("./faces/"+fname+ext)
            face_encoding = face_recognition.face_encodings(face_image)
            if face_encoding:
                face_encoding = face_encoding[0]
                known_face_encodings.append(face_encoding)
                known_face_names.append(fname)

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding, 0.4)
                name = "Unknown"

                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame
        for id in face_names:
            if id=="Unknown":
                continue
            sql = "INSERT INTO datas (client_id, camera_id) VALUES (%s,%s)"
            val = (id,camera_no)
            curs.execute(sql, val)
            conn.commit()


        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

import face_recognition
import cv2
import pymongo as mongo

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

count = 0

github_icon = cv2.imread("GitHub.jpg")
github_icon = cv2.resize(github_icon, (30, 30))

facebook_icon = cv2.imread("Facebook.png")
facebook_icon = cv2.resize(facebook_icon, (30, 30))

# Load a sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file("obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

nick_image = face_recognition.load_image_file("nick.jpg")
nick_face_encoding = face_recognition.face_encodings(nick_image)[0]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    count = count + 1
    if(count == 360):
        count = 0

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    face_locations = face_recognition.face_locations(small_frame)
    # Only process every other frame of video to save time
    if (count % 30 == 0):
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces(
                [obama_face_encoding, nick_face_encoding], face_encoding)
            name = "Unknown"

            if match[0]:
                name = "Obama"

            if match[1]:
                name = "Nick"

            face_names.append(name)

        # process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35),
                      (right, bottom), (0, 0, 255), cv2.FILLED)

        # Draw a label with a name below the face
        if(name == "Unknown"):
            cv2.rectangle(frame, (left, bottom),
                          (right, bottom + 35), (255, 255, 255), cv2.FILLED)
            frame[bottom:bottom + facebook_icon.shape[0],
                  left + 5:left + 5 + facebook_icon.shape[1]] = facebook_icon
            frame[bottom:bottom + github_icon.shape[0],
                  left + facebook_icon.shape[1] + 15:left + facebook_icon.shape[1] + 15 + github_icon.shape[1]] = github_icon
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6),
                    font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

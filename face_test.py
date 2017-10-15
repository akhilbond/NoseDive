import face_recognition
import cv2
import pymongo as mongo
import os
from account import Account
import webbrowser
import sys
from twilio.rest import Client

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)

class Button(object):
    def __init__(self,topleft,bottomright,link):
        self.topleft = topleft
        self.bottomright = bottomright
        self.link = link

def click_and_keep(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        fb_button = param[0]
        twitter_button = param[1]
        insta_button = param[2]

        prof = ""

        if(x>fb_button.topleft[0] and x<fb_button.bottomright[0] and y<fb_button.bottomright[1] and y>fb_button.topleft[1]):
            webbrowser.open_new(str(fb_button.link))
            prof = "Facebook"
        elif(x>twitter_button.topleft[0] and x<twitter_button.bottomright[0] and y<twitter_button.bottomright[1] and y>twitter_button.topleft[1]):
            if twitter_button.link is not '':
                webbrowser.open_new(str(twitter_button.link))
                prof = "Twitter"
        elif(x>insta_button.topleft[0] and x<insta_button.bottomright[0] and y<insta_button.bottomright[1] and y>insta_button.topleft[1]):
            if insta_button.link is not '':
                webbrowser.open_new(str(insta_button.link))
                prof = "Instagram"

        account_sid = "ACf91e60bf6394982df564444b5db4c508"
        auth_token  = "59bb2da30e29d7414d9d629f3d73f3ee"
        client = Client(account_sid, auth_token)
        data = "Someone has scanned your ", prof, " profile from Nosedive!"
        userPhone = 0

        for i in range(len(accounts_list)):
            if(Prof == "Facebook"):
                if fb_button.link == ("facebookURL:"+accounts_list[i].fb):
                    userPhone = accounts_list[i].phone
            if(Prof == "Twitter"):
                if twitter_button.link == ("twitterURL:"+accounts_list[i].twitter):
                    userPhone = accounts_list[i].phone
            if(Prof == "Instagram"):
                if insta_button.link == ("instagramURL:"+accounts_list[i].insta):
                    userPhone = accounts_list[i].phone
            if(Prof == ""):
                

        message = client.messages.create(
        	to="+1" + userPhone,
        	from_="+3363447154",
        	body=data)







video_capture = cv2.VideoCapture(0)

count = 0

insta_icon = cv2.imread("Instagram.png")
insta_icon = cv2.resize(insta_icon, (30, 30))

twitter_icon = cv2.imread("Twitter.jpg")
twitter_icon = cv2.resize(twitter_icon, (30, 30))

facebook_icon = cv2.imread("Facebook.png")
facebook_icon = cv2.resize(facebook_icon, (30, 30))

# Load a sample picture and learn how to recognize it.

fb_button = []
insta_button = []
twitter_button = []

image_encoding_list = []
accounts_list = []

for file in os.listdir('./photos'):
    if file.endswith(".jpg"):
        temp_img = face_recognition.load_image_file('./photos/' + str(file))
        temp_encoding = face_recognition.face_encodings(temp_img)[0]
        image_encoding_list.append(temp_encoding)

f = open("emails.txt")

for line in f:
    info = line.split(",")

    name = info[0].split(":")[1]
    number = info[1].split(":")[1]
    fb = info[2].split(":")[1]
    twitter = ''
    insta = ''

    if (len(info) > 3):
        tmp = info[3].split(":")
        if(tmp[0] == "twitterURL"):
            twitter = tmp[1]
        else:
            insta = tmp[1]

    if (len(info) > 4):
        tmp = info[4].split(":")
        if(tmp[0] == "instagramURL"):
            insta = tmp[1]
        else:
            twitter = tmp[1]

    account = Account(name,number,fb)
    if twitter is not '':
        account.addTwitter(twitter)
    if insta is not '':
        account.addInsta(insta)
    accounts_list.append(account)

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

cv2.setMouseCallback("Video", click_and_keep)

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
        name = 'Unknown'
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces(image_encoding_list, face_encoding)

            for i in range(len(match)):
                if match[i]:
                    name = accounts_list[i].name

            face_names.append(name)

        # process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4


        #insta = Button()
        #twitter = Button()

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35),
                      (right, bottom), (0, 0, 255), cv2.FILLED)

        # Draw a label with a name below the face
        if(name != "Unknown"):
            for i in range(len(accounts_list)):
                if name == accounts_list[i].name:
                    twitter = accounts_list[i].twitter
                    insta = accounts_list[i].insta
                    fb = accounts_list[i].fb

            cv2.rectangle(frame, (left, bottom),
                          (right, bottom + 35), (255, 255, 255), cv2.FILLED)
            if(bottom<=440):
                fb_button = Button((left+5,bottom),(left + 5 + facebook_icon.shape[1],bottom + facebook_icon.shape[0]),str(fb))

                twitter_button = Button((left + facebook_icon.shape[1] + 15,bottom),(left + facebook_icon.shape[1] + 15 + facebook_icon.shape[1],bottom + facebook_icon.shape[0]),str(twitter))

                insta_button = Button((left + facebook_icon.shape[1] + facebook_icon.shape[1] + 30,bottom),(left + facebook_icon.shape[1] + 30 + facebook_icon.shape[1]+facebook_icon.shape[1],bottom + facebook_icon.shape[0]),str(insta))

                frame[bottom:bottom + facebook_icon.shape[0],
                     left + 5:left + 5 + facebook_icon.shape[1]] = facebook_icon
                if(twitter is not ''):
                    frame[bottom:bottom + facebook_icon.shape[0],
                         left + facebook_icon.shape[1] + 15:left + facebook_icon.shape[1] + 15 + facebook_icon.shape[1]] = twitter_icon


                if(insta is not ''):
                    frame[bottom:bottom + facebook_icon.shape[0],
                         left + facebook_icon.shape[1] + facebook_icon.shape[1] + 30:left + facebook_icon.shape[1] + 30 + facebook_icon.shape[1]+facebook_icon.shape[1]] = insta_icon


        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6),
                    font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.namedWindow("Video")
    cv2.setMouseCallback("Video", click_and_keep, (fb_button,twitter_button,insta_button))
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

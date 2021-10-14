# pip install python-facepp

from __future__ import print_function, unicode_literals

import json
from facepplib import FacePP, exceptions

face_detection=""
faceset_initialize=""
face_search=""
face_landmarks=""
dense_facial_landmarks=""
face_attributes=""
beauty_score_and_emotion_recognition=""

def face_comparing(app):
    """compare two faces and decides whether they are same person"""
    print('[Face camparing]')

#compare two images of website:
    x= input('enter the url')
    y = input('enter the other url')
    img_url1 = x
    img_url2 = y
    #img_url1="https://urbanasian.com/wp-content/uploads/2017/11/Aamir-Khan.jpg"
    #img_url2="http://www.suntiros.com/wp-content/uploads/2017/01/Aamir-Khan-Latest-Hair-Style-Pictures-Pics.jpg"
#compare two local drive images:

    #img_url1=""
    #img_url2=""


# compare two diffrent images
   #img_url2=""

    cmp_ = app.compare.get(image_url1=img_url1,image_url2=img_url2)

    print('image1','=',cmp_.image1)
    print('image2','=',cmp_.image2)

    print('thresholds','=',json.dumps(cmp_.thresholds,indent=4))
    print('confidence','=',cmp_.confidence)

    if cmp_.confidence>70:
       print("both faces are same")
    else:
       print("not same")

if __name__=='__main__':
    api_key='xQLsTmMyqp1L2MIt7M3l0h-cQiy0Dwhl'
    api_secret='TyBSGw8NBEP9Tbhv_JbQM18mIlorY6-D'

    try:
        app_=FacePP(api_key=api_key,api_secret=api_secret)
        funcs=[
            
            face_detection,
            face_comparing,
            faceset_initialize,
            face_search,
            face_landmarks,
            dense_facial_landmarks,
            face_attributes,
            beauty_score_and_emotion_recognition,
        ]
        face_comparing(app_)

    except exceptions.BaseFacePPError as e:
       print('Error:',e)

    
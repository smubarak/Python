import os
import cv2
import numpy as np
from PIL import Image


recognizer = cv2.face.createLBPHFaceRecognizer()
path = 'faces'

def getImageWithID(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faces = []
    IDs   = []
    for imageName in imagePaths:
        faceImage    = Image.open(imageName).convert('L')
        user_face_np = np.array(faceImage,'uint8')
        user_id      = int(os.path.split(imageName)[-1].split('.')[1])
        faces.append(user_face_np)
        IDs.append(user_id)
        cv2.imshow('Training',user_face_np)
        cv2.waitKey(30)
    return np.array(IDs),faces


user_ids,user_faces = getImageWithID(path)
recognizer.train(user_faces,user_ids)
recognizer.save('recognizer/training_data.yml')
cv2.destroyAllWindows()
        
        
    


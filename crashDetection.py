import cv2
import random
import datetime
from collections import deque

'''
A method that loads the ml model and for a frame, returns true if an accident is detected for a frame. 
'''
def checkIfAccidentIsDetected(frame): 
    #Sandesh do your thing, I think ideally we should cumilataive average of multiple frames.
    #Feel free to change the implementation as you deem fit.
    if random.randint(1,1000)%997 == 0: 
        return True
    return False


cap = cv2.VideoCapture("./input.mp4")
while not cap.isOpened():
    cap = cv2.VideoCapture("./input.mp4")
    cv2.waitKey(1000)
    print("Wait for the header")
    
pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
frameList = deque([])
while True:
    flag, frame = cap.read()
    if flag:
        accidentDetected = checkIfAccidentIsDetected(frame)
        if accidentDetected: 
            # If the accident is detected we will take the last 30*60 frame assuming 30fps and stich it into video
            ct = datetime.datetime.now()
            videoTitle = "%s.mp4"%(ct.timestamp())
            writer = cv2.VideoWriter(videoTitle, cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 30, (512, 512))
            for currentFrame in frameList:
                cv2.imshow(currentFrame)
                writer.write(currentFrame)
            writer.release()
            # once the video is created, we will clear the framlist
            frameList.clear()
        else: 
            if (len(frameList)>1800): 
                frameList.pop()
            frameList.appendleft(frame)
            

    else:
        # The next frame is not ready, so we try to read it again
        cap.set(cv2.CAP_PROP_POS_FRAMES, pos_frame-1)
        print("frame is not ready")
        # It is better to wait for a while for the next frame to be ready
        cv2.waitKey(1000)
        

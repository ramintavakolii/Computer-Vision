import numpy as np
import cv2

# create a VideoCapture object
cap = cv2.VideoCapture('eggs.avi')

# get the dimensions of the frame
# you can also read the first frame to get these

#--------------------------------- first methode -------------------------------------
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # width of the frame
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # height of the frame
print('w =',w)
print('h =',h)
print('---------------------------------')

#--------------------------------- second methode -------------------------------------
ret, I = cap.read()
# print('ret =',ret)
print('Shape(I) = ', I.shape)


fourcc = cv2.VideoWriter_fourcc(*'XVID') # choose codec
print('fourcc = ' ,fourcc)

# opencv 2.x:
#w = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)) 
#h = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)) 
#fourcc = cv2.cv.CV_FOURCC(*'XVID')

# create VideoWriter object w by h, 30 frames per second
out = cv2.VideoWriter('eggs-reverse.avi',fourcc, 30.0, (w,h))
'''
creates a VideoWriter object named out,which is configured to write frames to the file 'eggs-reverse.avi' using the 
specified codec (fourcc), frame rate (30.0), and frame dimensions ((w, h)).
This object will be used to write the frames of the reversed video to the output file.
'''

buffer = []
print('buffre type =', type(buffer))
while True:
    ret, I = cap.read()
    if ret == False: # end of video (or error)
        break
    buffer.append(I) # add frame I at the end of the buffer
    # write the current frame I
    # out.write(I)


# Reverse Buffer
buffer.reverse()

# Write frames to the output video
for frame in buffer:
    out.write(frame)   


cap.release()
out.release()

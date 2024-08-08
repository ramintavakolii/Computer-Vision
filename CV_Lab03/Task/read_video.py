import numpy as np
import cv2

# create a VideoCapture object
cap = cv2.VideoCapture('kntu-computer.avi')

print('cap = ', cap)
print('did cap opened? ', cap.isOpened())

# sometimes this is needed:
# if not cap.isOpened():
#    cap.open();


while True:

    # Capture frame-by-frame
    ret, I = cap.read()

    print('ret =',ret)
    print('Shape(I) =',I.shape)

    if ret == False:  # end of video (perhaps)
        print('Reading Unsuccessfully')
        break

    # Display I
    cv2.imshow('win1', I)

    key = cv2.waitKey()  # ~ 30 frames per second
    # print(key)

    if key & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

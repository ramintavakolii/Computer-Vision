import cv2
import numpy as np

def rotate_around_center(center, angle):

    # Calculate sine and cosine of the angle
    cos_theta = np.cos(angle)
    sin_theta = np.sin(angle)

    # Get the translation components
    tx = center[0] * (1 - cos_theta) + center[1] * sin_theta
    ty = center[1] * (1 - cos_theta) - center[0] * sin_theta

    # Construct the rotation matrix
    rotation_matrix = np.array([[cos_theta, -sin_theta, tx],
                                [sin_theta, cos_theta, ty],
                                [0, 0, 1]])
    return rotation_matrix


I = cv2.imread('./Code/Images/karimi.jpg', 0)

# centre of the image
c = np.array([[I.shape[1]/2.0], [I.shape[0]/2.0]])
print(c.shape)

height, width = I.shape
center = (width/2, height/2)

for theta in range(0, 360):
    th = theta * np.pi / 180  # convert to radians

    # rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=theta, scale=1)

    rotate_matrix = rotate_around_center(center, th)

    J = cv2.warpPerspective(I, rotate_matrix, (I.shape[1] + 300, I.shape[0] + 300))
    
    cv2.imshow('J', J)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

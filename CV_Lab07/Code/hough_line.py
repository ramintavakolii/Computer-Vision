import numpy as np
import cv2
import time



def draw_line(I,rho,theta):
    "draws a line in image 'I' given 'rho' and 'theta'"
    
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    
    cv2.line(I,(x1,y1),(x2,y2),(0,0,255),1)

    
I = cv2.imread('./Code/Images/highway.jpg')
G = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY) # -> grayscale
print(G.shape)

# find the edges
E = cv2.Canny(G,100,200) 

# mininum votes to be considered a line
min_votes = 750 

# 1 pixel: resolution of the parameter "rho" (distance to origin)
distance_resolution = 5

# pi/180 radians: resolution (bin size) of the parameter "theta" 
angle_resolution = 1*np.pi/180 

# Record the current time
start_time = time.time()

L = cv2.HoughLines(E,distance_resolution,angle_resolution,min_votes)
# Calculate the elapsed time
elapsed_time = time.time() - start_time
print("Time taken to execute cv2.HoughLines():", np.round(elapsed_time,4), "seconds")

print(L[0])
# draw the lines 
for [[rho,theta]] in L:
    draw_line(I,rho,theta)

cv2.imshow("E",E)
cv2.imshow("I",I)
cv2.waitKey(0)
cv2.destroyAllWindows()


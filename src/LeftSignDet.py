import cv2
import numpy as np
scale_identity = 1.1
min_neighbots = 3


Stop_Cascade = cv2.CascadeClassifier("TrafficsignDetection/Signs/Scascade.xml")

def LsignDetect(image):
    img = cv2.cvtColor(image.copy(), cv2.COLOR_RGB2GRAY)
    hsv = cv2.cvtColor(image.copy(), cv2.COLOR_RGB2HSV)
    lower1 = np.array([0, 100, 20])
    upper1 = np.array([10, 255, 255])
 
    # upper boundary RED color range values; Hue (160 - 180)
    lower2 = np.array([160,100,20])
    upper2 = np.array([179,255,255])
 
    lower_mask = cv2.inRange(image, lower1, upper1)
    upper_mask = cv2.inRange(image, lower2, upper2)
 
    full_mask = lower_mask + upper_mask;
    
    Stop_sign = Stop_Cascade.detectMultiScale(image, scale_identity,min_neighbots)
    if (len(Stop_sign)>0):
        contours, hierarchy = cv2.findContours(full_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 150):
                return True
    return False
	

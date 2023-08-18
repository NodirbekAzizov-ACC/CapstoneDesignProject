import cv2
import numpy as np

def TraffLightDett(image):
    detected = False
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 0, 0])
    upper = np.array([179, 100, 130])
    R_lower = np.array([161, 155, 84])
    R_upper = np.array([179, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)
    Rmask = cv2.inRange(hsv, R_lower, R_upper)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 1600):
			print("black")
            Rcontours, Rhierarchy = cv2.findContours(Rmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            for Rpic, Rcontour in enumerate(Rcontours):
                area = cv2.contourArea(Rcontour)
                if (area > 400):
					print("Red")
                    detected = True

    return detected

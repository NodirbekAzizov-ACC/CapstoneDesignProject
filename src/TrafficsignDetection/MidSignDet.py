import cv2

scale_identity = 1.1
min_neighbots = 3


Left_Cascade = cv2.CascadeClassifier(
"TrafficsignDetection/Signs/Lcascade.xml")

Right_Cascade = cv2.CascadeClassifier(
"TrafficsignDetection/Signs/Rcascade.xml")

Park_Cascade = cv2.CascadeClassifier(
"TrafficsignDetection/Signs/Pcascade.xml")


def MsignDetect(image):
    img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
	
    left_sign = Left_Cascade.detectMultiScale(image, scale_identity,
    min_neighbots)
	
    right_sign = Right_Cascade.detectMultiScale(image, scale_identity, 
    min_neighbots)
	
    park_sign = Park_Cascade.detectMultiScale(image, scale_identity, 
    min_neighbots)
    if len(park_sign) != 0:
        return "Park Sign"
    return "None"
"""
    if len(left_sign) > len(right_sign):
        return "left"
    elif len(left_sign) < len(right_sign):
        return "right"
"""    


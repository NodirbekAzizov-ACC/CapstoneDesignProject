import cv2

scale_identity = 1.1
min_neighbots = 3


Stop_Cascade = cv2.CascadeClassifier("TrafficsignDetection/Signs/Scascade.xml")

def LsignDetect(image):
    img = cv2.cvtColor(image.copy(), cv2.COLOR_RGB2GRAY)
    R_lower = np.array([160,100,20])
    R_upper = np.array([179,255,255])
    Rmask = cv2.inRange(hsv, R_lower, R_upper)
    Rcontours, Rhierarchy = cv2.findContours(Rmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            for Rpic, Rcontour in enumerate(Rcontours):
                area = cv2.contourArea(Rcontour)
                if (area > 450):
                    Stop_sign = Stop_Cascade.detectMultiScale(image, scale_identity,
                    min_neighbots)
                    BE_sign = BE_Cascade.detectMultiScale(image, scale_identity, 
                    min_neighbots)
                    print("Red detected")
                    if len(Stop_sign) > len(BE_sign):
                        print("Sign Detected")
                        return True
	return False

	

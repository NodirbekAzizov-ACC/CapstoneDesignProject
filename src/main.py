from LineDetection import *
from time import sleep, time
from TrafficLightDet import TraffLightDett
from LeftSignDet import LsignDetect
from ControlCar import *
from SPedestrian import SObjectDet




cap = cv2.VideoCapture(0)
speed = 30
action = 'n'
stop = time()
start = time()
#StoptDetected = False
#TrafficLightDetected = 0
distanceS = 15
try:
    while (cap.isOpened()):
        success, frame = cap.read()
        lineDet, trafLight, MidSign = ImageSeperation(frame)
        cv2.imshow("hhh", trafLight)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            Destroy()
            break
        if success is False:
            Destroy()
            break
        
        if action != 'n':
            start = time()
            stop = time()
            speed = 15
        stop = time()
                       
        if stop - start > 1.5:
            speed = 30
        
        if TraffLightDett(trafLight):
            stopCar()
            start = time()
            stop = time()
            print("Red")
            continue
        action = Control(lineDet, speed)
        
except KeyboardInterrupt:
    pass
finally:
    Destroy()
    cap.release()
    cv2.destroyAllWindows()
    
    


# **************************************************
"""
image = cv2.imread("TrafficsignDetection/Stop.jpg")
(lineDet, trafSign, trafLight, MidSign, Sobject) = ImageSeperation(image)
LsignDetect(trafSign)
cv2.imshow("sa", trafSign)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""






    

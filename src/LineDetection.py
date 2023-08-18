from time import sleep, time
from Imports import *
from ControlCar import *
import numpy as np

theta = np.pi / 180
def LineDetect(lineDet):
    direction = 'n'
    gray = cv2.cvtColor(lineDet, cv2.COLOR_BGR2GRAY)
    blur_gray = cv2.GaussianBlur(gray, (1, 1), 0)
    
    edges = cv2.Canny(blur_gray, 50, 150)
    cv2.imshow("edges", edges)
    #line_image = np.copy(lineDet)*0
    lines = cv2.HoughLinesP(edges, 1, theta, 0, np.array([]), 
    1,0)
    points = []
    count = 0
    if lines is not None:
        for line in lines:
            if line is not None:
                x1, y1, x2, y2 = line[0]
            if x1 > 320 and x2 > 320:
                    direction = 'l'
                    break
            if x1 < 320 and x2 < 320:
                    direction = 'r'
                    break
            if x1 > 320 and x2 < 320:
                if y1 > y2:
                    direction = 'l'
                    break
                else:
                    direction = 'r'
                    break
            if x1 < 320 and x2 > 320:
                if y1 > y2:
                    direction = 'r'
                    break
                else:
                    direction = 'l'
                    break
    return direction

def Control(lineDet, speed):
    direction= LineDetect(lineDet)
 
    if direction == 'n':
        FastForward(speed)
        print("Fast forward")
        return 'n'
    else:
        if direction == 'r':
            StrongTurnR()
            print("Strong Right")
            return "t"
        elif direction == "l":
            StrongTurnL()
            print("Strong Left")
            return 't'
        else:
            stopCar()
            
def ImageSeperation(image):
    lineDet = image[460:479, 5:624]
    trafLight = image[0:200, 0:200]
    MidSign = image[0:140, 250:390]
    return (lineDet, trafLight, MidSign)
    
    
    
    

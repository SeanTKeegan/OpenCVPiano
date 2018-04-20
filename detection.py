import cv2, os
import numpy as np


class Detection(object):

    THRESHOLD = 1500


    def __init__(self, image):
        self.previous_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def __del__(self):
        print "detection deleted"

    def get_active_cell(self, image, webcam):

        # obtain motion between previous and current image
        current_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        delta = cv2.absdiff(self.previous_gray, current_gray)
        threshold_image = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
        
        # store current image
        self.previous_gray = current_gray

        # set cell width
        height, width = threshold_image.shape[:2]
        height = height / 3
        cell_width = width/7

        # store motion level for each cell
        cells = np.array([0, 0, 0, 0, 0, 0, 0])
        cells[0] = cv2.countNonZero(threshold_image[0:height, 0:cell_width])
        cells[1] = cv2.countNonZero(threshold_image[0:height, cell_width:cell_width*2])
        cells[2] = cv2.countNonZero(threshold_image[0:height, cell_width*2:cell_width*3])
        cells[3] = cv2.countNonZero(threshold_image[0:height, cell_width*3:cell_width*4])
        cells[4] = cv2.countNonZero(threshold_image[0:height, cell_width*4:cell_width*5])
        cells[5] = cv2.countNonZero(threshold_image[0:height, cell_width*5:cell_width*6])
        cells[6] = cv2.countNonZero(threshold_image[0:height, cell_width*6:width])

        # visual black & white 'piano keys'
        image[0:height, 0:cell_width] = (0,0,0)
        image[0:height, cell_width:cell_width*2] = (225,225,225)
        image[0:height, cell_width*2:cell_width*3] = (0,0,0)
        image[0:height, cell_width*3:cell_width*4] = (225,225,225)
        image[0:height, cell_width*4:cell_width*5] = (0,0,0)
        image[0:height, cell_width*5:cell_width*6] = (225,225,225)
        image[0:height, cell_width*6:width] = (0,0,0)

        buttonColour = (225,225,225)

    
        # round duration button
        cv2.circle(image,(cell_width/4,(height*2)-(height/4)), cell_width/4, buttonColour, -1)
        # actual area checked if touched for button -> comment in for degugging
        # image[(height+(height/2)):height*2, 0:cell_width/2] = (225,0,225)

        # round frequency button
        cv2.circle(image,(cell_width/4,(height*2)+(height/4)), cell_width/4, (0,225,225), -1)
        # image[height*2+10:height*2+(height/2), 0:cell_width/2] = (225,225,225)

        cv2.imshow('OpenCV Detection', image)
        cv2.waitKey(10)

        
        # actual area checked if touched for button
        checkDurationCell = cv2.countNonZero(threshold_image[(height+(height/2)):height*2, 0:cell_width/2])
        checkFreqCell = cv2.countNonZero(threshold_image[height*2:height*2+(height/2), 0:cell_width/2])

        # toggle duration between 'ON' & 'OFF'
        if(checkDurationCell >= self.THRESHOLD):
            webcam.toggleDuration = not webcam.toggleDuration
            
        if (webcam.toggleDuration):
            webcam.turnOn((cell_width/4)-20,(height*2)+10)
        else:
            webcam.turnOff((cell_width/4)-20,(height*2)+10)
        
        # toggle freq between 'ON' & 'OFF'
        if(checkFreqCell >= self.THRESHOLD):
            webcam.toggleFreq = not webcam.toggleFreq
            
        # if (webcam.toggleDuration):
        #     webcam.switchTextOn((cell_width/4)-20,(height*2)+10)
        # else:
        #     webcam.switchTextOff((cell_width/4)-20,(height*2)+10)
  


        # obtain the most active cell
        top_cell =  np.argmax(cells)

        # return the most active cell, if threshold met
        if(cells[top_cell] >= self.THRESHOLD):
            return top_cell
        else:
            return None

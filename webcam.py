import cv2, signal, sys
from threading import Thread

class Webcam:

    toggleDuration = True
    toggleFreq = True

    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)
        self.current_frame = self.video_capture.read()[1]

    def __del__(self):
        if self.video_capture.is_alive():
            self.camThread.join()
            self.camThread.release()
            self.video_capture.release()
            self.camThread.setDaemon = False
            cv2.destroyAllWindows()

    # create thread for capturing images
    def start(self):
        self.camThread = Thread(target=self._update_frame, args=())
        self.camThread.start()
        self.camThread.setDaemon = True


    def _update_frame(self):
        while(True):
            self.current_frame = self.video_capture.read()[1]

    # get the current frame
    def get_current_frame(self):
        return self.current_frame

    def turnOn(self,width,height):
        cv2.putText(self.current_frame, 'SUSTAIN ON', (width,height), cv2.FONT_ITALIC, 0.6, (0,255,255))

    def turnOff(self,width,height):
        cv2.putText(self.current_frame, 'SUSTAIN OFF', (width,height), cv2.FONT_ITALIC, 0.6,(0,255,255))
    
    def switchTextOn(self,width,height):
        cv2.putText(self.current_frame, 'PITCH ON', (width,height), cv2.FONT_ITALIC, 0.6, (0,255,255))

    def switchTextOff(self,width,height):
        cv2.putText(self.current_frame, 'PITCH OFF', (width,height), cv2.FONT_ITALIC, 0.6,(0,255,255))
    
    def writeFreqNumber(self,width,height,num):
        digit = str(num)
        cv2.putText(self.current_frame, digit, (width,height), cv2.FONT_ITALIC, 1,(0,255,255))
        cv2.putText(self.current_frame, 'Change Pitch', (width-(width/18),height+(height/4)), cv2.FONT_ITALIC, .5,(0,255,255))
        cv2.putText(self.current_frame, '(turn on pitch 1st) ', (width-(width/12),height+(height/4)+20), cv2.FONT_ITALIC, .5,(0,255,255))




  





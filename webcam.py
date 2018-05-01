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

    def turnOn(self,height,width):
        cv2.putText(self.current_frame, 'SUSTAIN ON', (height,width), cv2.FONT_ITALIC, 0.8, (0,255,255))

    def turnOff(self,height,width):
        cv2.putText(self.current_frame, 'SUSTAIN OFF', (height,width), cv2.FONT_ITALIC, 0.8,(0,255,255))
    
    def switchTextOn(self,height,width):
        cv2.putText(self.current_frame, 'PITCH ON', (height,width), cv2.FONT_ITALIC, 0.8, (0,255,255))

    def switchTextOff(self,height,width):
        cv2.putText(self.current_frame, 'PITCH OFF', (height,width), cv2.FONT_ITALIC, 0.8,(0,255,255))
   


  





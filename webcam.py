import cv2, signal, sys
from threading import Thread

class Webcam:

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
   





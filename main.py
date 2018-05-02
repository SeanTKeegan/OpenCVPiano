import sys
import cv2, time, sound, os
from webcam import Webcam
from detection import Detection


# musical notes (C, D, E, F, G, A, B) -> one octave
NOTES = [262, 294, 330, 350, 393, 441, 494]

# initialise webcam and start thread

webcam = Webcam()
webcam.start()
# factor = 1

#initialise type of wave
param = (sys.argv)
wave = 'sine'
if len(param) == 1:
    wave = 'sine'
    print 'Playing with: sine wave'
elif len(param) == 2:
    wave = param[1]
    print 'Playing with: ',param[1], ' wave'


# initialise detection with first webcam frame
image = webcam.get_current_frame()
detection = Detection(image)

# initialise switch
switch = True

while True:

    if(webcam.toggleDuration):
        duration = 2
        # factor = 2
    else:
        duration = 0.5
        # factor = 1

    # get current frame from webcam
    image = webcam.get_current_frame()

    # use motion detection to get active cell

    cell = detection.get_active_cell(image,webcam)
    if cell == None: continue

    # if switch on, play note
    if switch:
            sound.playTone(0.5,44100,duration,NOTES[cell],detection.num, wave)

    # alternate switch
    switch = not switch

    # 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# close app
del detection
del webcam
cv2.destroyAllWindows()
os._exit(0)

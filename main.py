from webcam import Webcam
from detection import Detection
#import winsound

# musical notes (C, D, E, F, G, A, B)
NOTES = [262, 294, 330, 350, 393, 441, 494]

# initialise webcam and start thread
webcam = Webcam()
webcam.start()

# initialise detection with first webcam frame
image = webcam.get_current_frame()
detection = Detection(image)

# initialise switch
switch = True

while True:

    # get current frame from webcam
    image = webcam.get_current_frame()

    # use motion detection to get active cell
    cell = detection.get_active_cell(image)
    if cell == None: continue

    # if switch on, play note
    if switch:
        #winsound.Beep(NOTES[cell], 1000)
        print NOTES[cell]

    # alternate switch
    switch = not switch

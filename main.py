import cv2, time, sound, os
from webcam import Webcam
from detection import Detection

# musical notes (C, D, E, F, G, A, B) -> one octave
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

        sound.playTone(0.5,44100,1.0,NOTES[cell])
        # print NOTES[cell]

    # alternate switch
    switch = not switch

    # 'q' to quit (currently working on this - not working yet)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

del detection
del webcam
cv2.destroyAllWindows()
os._exit(0)




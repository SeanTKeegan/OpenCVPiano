# OpenCVPiano
This is an OpenCV application which plays a piano. Based on RDMilligan's https://rdmilligan.wordpress.com/2015/10/22/paper-piano-using-python-and-opencv/

This version has the Winsound calls removed and for the time-being simply prints the note (frequency) associated with the area where motion is detected.

Simply run `main.py`

Stay very still when you run it :guardsman: and move slowly to see the output. :turtle:

## Known issues with this version:
   - Winsound (which produces the tones) only works on Windows. A package which works ideally on MacOS and Linux is needed.

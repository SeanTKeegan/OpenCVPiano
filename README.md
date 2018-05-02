# OpenCVPiano :musical_keyboard:
This is an OpenCV application which plays a piano. Based on RDMilligan's https://rdmilligan.wordpress.com/2015/10/22/paper-piano-using-python-and-opencv/

Simply run `main.py`. Stay very still when you run it :guardsman: and move slowly to see the output. :turtle:

## Required (Mac OS):

* Python 2.7
* openCV 2
* pyaudio

```bash

# installing pyaudio with pip and brew

brew install portaudio
brew link portaudio
pip install pyaudio

```

![OpenCVPiano](media/Screenshot-of-OpenCVPiano.png)

## How to Interact

* stuff about sawtooth selection here
* stuff about the UI 
  * keyboard


**The buttons can be interacted with in the same way as with the keyboard at the top of the screen.** 

#### Sustain Button:
This button controls the duration at which each note is played. This can be toggled on and off by hitting it with your hand.

#### Pitch Button & Up/Down Buttons:
By default the frequency of the note is 1. This corresponds to the keys at the top of the screen - starting on middle C. By raising this number to 2, the user can change the octave of the corresponding note on the keyboard.

To successfully change the frequency value, the user must first 'turn on' pitch by selecting the pitch button at the left-hand side of the screen. Once this button has been selected, the user may now toggle the value of the frequency. The up and down buttons are on the right-hand side of the screen, along with the current value for frequency.

The frequency value resets to the default value of 1 by 'turning off' the pitch.



## How it Works







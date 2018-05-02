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
This button controls the duration that each note is played. This can be toggled on and off by hitting it with your hand.

#### Pitch Button & Up/Down Buttons:
By default the frequency of the note is 1. This corresponds to the keys at the top of the screen - starting on middle C. By raising this number to 2, the user can change the octave of the corresponding note on the keyboard.

To successfully change the frequency value, the user must first 'turn on' pitch by selecting the pitch button at the left-hand side of the screen. Once this button has been selected, the user may now toggle the value of the frequency. The up and down buttons are on the right-hand side of the screen, along with the current value for frequency.

The frequency value resets to the default value of 1 by 'turning off' the pitch.



## How it Works

#### Keyboard:
An array stores the dimensions of each of the keyboard keys. Black and white pixels are drawn over the area of each respective key into the camera feed image. In order to detect if a key has been hit, the application subtracts each frame from the previous and checks for a substantial difference (in accordance to some threshold).

The key with the most activity is returned. This can now be used to trigger the correct auditory response.

```python

# store motion level for each cell
cells = np.array([0, 0, 0, 0, 0, 0, 0]

# ...

# visual black & white 'piano keys'
image[0:height, 0:cell_width] = (0,0,0)

# ...

# obtain the most active cell
top_cell =  np.argmax(cells)

# return the most active cell, if threshold met
if(cells[top_cell] >= self.THRESHOLD):
    return top_cell
else:
    return None

```

In the main, once the information has been received about which key has been hit, the correct sound can be triggered. The camera feed continues if nothing has been hit.

```python

# if switch on, play note
if switch:
        sound.playTone(0.5,44100,duration,NOTES[cell],detection.num, wave)

# alternate switch
switch = not switch

```


#### Buttons:
Detection for button clicks is the same as that for the keyboard keys. Each button however, has a little extra functionality to allow for smooth interaction.

```python

# adjust freq number up and down
    if(checkUpArrow >= self.THRESHOLD and time.time() - self.previousTime >= 2):
        self.num += 1
        self.previousTime = time.time()

```

The if statement in the above code checks if the difference between that specific area of the screen is substantially different than that of the same area one frame previous (i.e. each frame from the live camera feed is differenced). This check is also done for each of the piano keys. 

The if statement also checks if the current timestamp is at least 2 more seconds than the last button click. This check was introduced to ensure that the button would "click" once, and not a multiple of times when a user tries to hit in once.

When both of these conditions are met, the frequency number is updated; in this case incremented. It is important that the frequency number belongs to the detection class. This is so the variable can be statically updated. The timestamp is also recorded for the next check.


```python

# toggle duration between 'ON' & 'OFF'
if(checkDurationCell >= self.THRESHOLD and time.time() - self.previousTime >= 2):
    webcam.toggleDuration = not webcam.toggleDuration
    self.previousTime = time.time()
            
```

The code for toggling on and off the duration functionality has the same conditions as the previous code, however the code inside the if statement is slightly different. If the duration is "on" it will be turned "off" and vice-versa. Again the timestamp is recorded. This allows for the user to be able to toggle on and off this option.


#### Sound






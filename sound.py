import pyaudio
import numpy as np
import time
from threading import Thread

samplesOfNote = [] # global variable for the samples of chosen note

# create thread for capturing images
# def start():
#     audioThread.start()
#     audioThread.setDaemon = True

def playTone(volume,sampleRate,duration,freq,factor,wave):
	# audioThread = Thread()
	# audioThread.start()

	p = pyaudio.PyAudio()

	volume = 0.5     # range [0.0, 1.0]
	fs = sampleRate  # sampling rate, Hz, must be integer
	f = freq         # sine frequency

	# generate samples, note conversion to float32 array
	if wave == 'saw':
		samples = (2 * (np.arange(fs*duration) * (f/fs) % 1) -1).astype(np.float32)
	#elif wave == "square":
		#samples = (np.power((-1),(np.floor(2 * (fs*duration) * (f/fs))))).astype(np.float32)
	else:
		samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

	samplesOfNote = samples
	print samplesOfNote

	# for paFloat32 sample values must be in range [-1.0, 1.0]
	stream = p.open(format=pyaudio.paFloat32,
	                channels=1,
	                rate=fs,
	                output=True)

	# play sound
	stream.write(volume*(speedxFactor(samplesOfNote,factor)))

	stream.stop_stream()
	stream.close()

	p.terminate()
	# audioThread.setDaemon = False


def speedxFactor(sound_array, factor):
    # Changes the frequency - in turn changing the pitch of the note & duration (speed changes)

    # if the factor is 2, indices will get half the samples of the original sound
    # eg sound_array = 88200 & indices = 44100
    indices = np.round(np.arange(0, len(sound_array), factor))
    indices = indices[indices < len(sound_array)].astype(int)

    # return the smaller array of samples
    return sound_array[indices.astype(int)]

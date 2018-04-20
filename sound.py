import pyaudio
import numpy as np

samplesOfNote = [] # global variable for the samples of chosen note

def playTone(volume,sampleRate,duration,freq,factor):

	p = pyaudio.PyAudio()

	volume = 0.5     # range [0.0, 1.0]
	fs = sampleRate  # sampling rate, Hz, must be integer
	f = freq         # sine frequency

	# generate samples, note conversion to float32 array
	samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

	samplesOfNote = samples
	# print samplesOfNote.shape

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

def speedxFactor(sound_array, factor):
    # Changes the frequency - in turn changing the pitch of the note & duration (speed changes)
   
    # if the factor is 2, indices will get half the samples of the original sound
    # eg sound_array = 88200 & indices = 44100
    indices = np.round(np.arange(0, len(sound_array), factor))
    indices = indices[indices < len(sound_array)].astype(int)
    
    # return the smaller array of samples
    return sound_array[indices.astype(int)]

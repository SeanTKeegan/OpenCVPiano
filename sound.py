import pyaudio
import numpy as np

def playTone(volume,sampleRate,duration,freq):

	p = pyaudio.PyAudio()

	volume = 0.5     # range [0.0, 1.0]
	fs = sampleRate  # sampling rate, Hz, must be integer
	f = freq         # sine frequency

	# generate samples, note conversion to float32 array
	samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

	# for paFloat32 sample values must be in range [-1.0, 1.0]
	stream = p.open(format=pyaudio.paFloat32,
	                channels=1,
	                rate=fs,
	                output=True)

	# play sound
	stream.write(volume*samples)

	stream.stop_stream()
	stream.close()

	p.terminate()

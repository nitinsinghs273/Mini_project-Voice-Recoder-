import sounddevice as sd
from scipy.io.wavfile import write
freq = 44100
duration = 5

recording = sd.rec(int(duration*freq), samplerate=freq, channels=2)
sd.wait()
write("recording0.wav", freq, recording)

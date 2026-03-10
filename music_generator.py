import numpy as np
from scipy.io.wavfile import write
import tempfile

def generate_music(mood, genre, instrument):

    rate = 44100
    duration = 5

    # Mood frequency
    if mood == "Happy":
        freq = 700
    elif mood == "Sad":
        freq = 300
    elif mood == "Energetic":
        freq = 900
    else:
        freq = 500

    # Genre adjustment
    if genre == "Classical":
        freq += 50
    elif genre == "Rock":
        freq += 150
    elif genre == "Lo-fi":
        freq -= 100

    t = np.linspace(0, duration, int(rate * duration), endpoint=False)

    # Instrument sound
    if instrument == "Piano":
        audio = np.sin(2 * np.pi * freq * t)

    elif instrument == "Guitar":
        audio = np.sign(np.sin(2 * np.pi * freq * t))

    elif instrument == "Flute":
        audio = np.sin(2 * np.pi * freq * t) * np.exp(-t)

    elif instrument == "Drum":
        audio = np.random.uniform(-1, 1, len(t)) * np.exp(-5 * t)

    else:
        audio = np.sin(2 * np.pi * freq * t)

    file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    write(file.name, rate, audio.astype(np.float32))

    return file.name

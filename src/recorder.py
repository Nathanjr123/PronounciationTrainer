import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import requests
import os

class AudioRecorder:
    def __init__(self, sample_rate=44100, duration=5, file_name="assets/recording.wav"):
        self.sample_rate = sample_rate
        self.duration = duration  # Duration of recording in seconds
        self.file_name = file_name
        self.audio_data = None

    def record(self):
        print(f"Recording for {self.duration} seconds...")
        self.audio_data = sd.rec(int(self.duration * self.sample_rate), samplerate=self.sample_rate, channels=2)
        sd.wait()  # Wait until recording is finished
        print("Recording finished.")

    def save_recording(self):
        if self.audio_data is not None:
            # Normalize the audio data to be in the range of -1 to 1
            scaled_data = np.int16(self.audio_data / np.max(np.abs(self.audio_data)) * 32767)
            # Ensure the assets directory exists
            os.makedirs(os.path.dirname(self.file_name), exist_ok=True)
            write(self.file_name, self.sample_rate, scaled_data)  # Save as WAV file
            print(f"Recording saved as {self.file_name}")
        else:
            print("No recording data to save.")

    def play_recording(self):
        if self.audio_data is not None:
            print("Playing the recording...")
            sd.play(self.audio_data, samplerate=self.sample_rate)
            sd.wait()  # Wait until playback is finished
        else:
            print("No recording to play.")

    def transcribe_audio(self, api_key):
        url = "https://api.deepgram.com/v1/listen"
        headers = {
            'Authorization': f'Token {api_key}',
            'Content-Type': 'audio/wav',
        }

        try:
            # Read the saved audio file
            with open(self.file_name, 'rb') as audio_file:
                response = requests.post(url, headers=headers, data=audio_file)

            # Check if the request was successful
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error: {response.status_code}, {response.text}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None
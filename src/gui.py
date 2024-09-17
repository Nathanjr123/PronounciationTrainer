import os
import tkinter as tk
from recorder import AudioRecorder
import librosa
import numpy as np
import soundfile as sf
import pyaudio

class SpeechToTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speech-to-Text Game")
        self.recorder = AudioRecorder()

        # List of words for the user to practice
        self.word_list = ["apple", "banana", "orange", "grape", "pear"]

        # Path to prerecorded pronunciations
        self.pronunciation_folder = os.path.abspath("C:/Users/syllj/Downloads/speechText/assets/pronunciations/")

        # Create dropdown for word selection
        self.selected_word = tk.StringVar()
        self.selected_word.set(self.word_list[0])  # Set default word

        self.word_dropdown = tk.OptionMenu(root, self.selected_word, *self.word_list)
        self.word_dropdown.pack(pady=10)

        # Create buttons for the GUI
        self.record_button = tk.Button(root, text="Record", command=self.start_recording, width=15, height=2)
        self.record_button.pack(pady=10)

        self.play_button = tk.Button(root, text="Play", command=self.play_recording, width=15, height=2)
        self.play_button.pack(pady=10)

        self.save_button = tk.Button(root, text="Save", command=self.save_recording, width=15, height=2)
        self.save_button.pack(pady=10)

        self.compare_button = tk.Button(root, text="Compare Pronunciation", command=self.compare_pronunciation, width=20, height=2)
        self.compare_button.pack(pady=10)

        self.replay_button = tk.Button(root, text="Replay Original Sound", command=self.replay_original_sound, width=20, height=2)
        self.replay_button.pack(pady=10)

        # Add a section for feedback
        self.feedback_label = tk.Label(root, text="Feedback will appear here.", wraplength=300)
        self.feedback_label.pack(pady=20)

    def start_recording(self):
        self.recorder.record()
        self.feedback_label.config(text="Recording...")

    def play_recording(self):
        self.recorder.play_recording()

    def save_recording(self):
        self.recorder.save_recording()
        self.feedback_label.config(text="Recording saved.")

    def compare_pronunciation(self):
        # Save the recording before comparison
        self.save_recording()

        # Load the user's recording
        user_recording, sr_user = librosa.load(self.recorder.file_name)

        # Load the correct pronunciation
        word = self.selected_word.get()
        pronunciation_path = os.path.join(self.pronunciation_folder, f"{word}.mp3")

        # Debugging output
        print(f"Looking for pronunciation file at: {pronunciation_path}")

        if not os.path.exists(pronunciation_path):
            self.feedback_label.config(text=f"Pronunciation file for '{word}' not found.")
            return

        correct_pronunciation, sr_correct = librosa.load(pronunciation_path)

        # Extract MFCC features for comparison
        user_mfcc = librosa.feature.mfcc(y=user_recording, sr=sr_user)
        correct_mfcc = librosa.feature.mfcc(y=correct_pronunciation, sr=sr_correct)

        # Calculate the similarity between the user's recording and the correct pronunciation
        similarity = self.calculate_similarity(user_mfcc, correct_mfcc)

        # Display feedback
        self.feedback_label.config(text=f"Your pronunciation is {similarity:.2f}% similar to the correct pronunciation.")

    def calculate_similarity(self, user_mfcc, correct_mfcc):
        # Average MFCC features
        user_mfcc_mean = np.mean(user_mfcc, axis=1)
        correct_mfcc_mean = np.mean(correct_mfcc, axis=1)

        # Calculate Euclidean distance
        dist = np.linalg.norm(user_mfcc_mean - correct_mfcc_mean)
        
        # Convert distance to similarity
        max_dist = np.linalg.norm(np.ones_like(user_mfcc_mean) * 100)  # Define max distance
        similarity = 100 - (dist / max_dist) * 100
        return similarity

    def replay_original_sound(self):
        word = self.selected_word.get()
        pronunciation_path = os.path.join(self.pronunciation_folder, f"{word}.mp3")

        if not os.path.exists(pronunciation_path):
            self.feedback_label.config(text=f"Pronunciation file for '{word}' not found.")
            return

        # Play the pronunciation file
        self.play_audio(pronunciation_path)

    def play_audio(self, file_path):
        # Read audio file
        data, samplerate = sf.read(file_path)

        # Create a PyAudio object
        p = pyaudio.PyAudio()

        # Open a stream
        stream = p.open(format=pyaudio.paFloat32,
                        channels=len(data.shape),
                        rate=samplerate,
                        output=True)

        # Play audio
        stream.write(data.astype(np.float32).tobytes())

        # Stop and close the stream
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeechToTextApp(root)
    root.mainloop()

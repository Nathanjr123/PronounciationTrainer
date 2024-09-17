
# Speech-to-Text Mini Game with Pronunciation Feedback

## Overview

This mini game allows users to practice their spoken English by speaking into the system, which transcribes their speech and provides real-time feedback on pronunciation. The game is built using Python and Tkinter for the user interface, while speech-to-text and pronunciation feedback are handled via integrated APIs.

### Features
- **Real-time transcription**: Speak into the microphone and see the transcription in real-time or with minimal delay.
- **Pronunciation feedback**: Receive actionable feedback on how to improve your spoken English (e.g., tips on pronouncing certain words).
- **Interactive interface**: Simple Tkinter GUI to interact with the game.
- **Replay Pronunciation**: Option to replay the original pronunciation of each word for comparison.

---

## File Structure

```
/speechText
    /assets
        /pronunciations    # Folder containing prerecorded pronunciation files (e.g., apple.mp3)
    /src
        gui.py             # Main Tkinter interface and game logic
        recorder.py        # Audio recording and playback functionalities
    README.md              # Project documentation and setup instructions
    requirements.txt       # Dependencies for the project
```

---

## Getting Started

### Prerequisites
- Python 3.x installed on your system.
- Install dependencies from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

- You will also need a free API key from a Speech-to-Text provider (e.g., [Deepgram](https://deepgram.com/) or [Google Cloud Speech](https://cloud.google.com/speech-to-text)) to use for the transcription.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://your-repository-url.git
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **API Configuration**:
   - Obtain a free API key from a Speech-to-Text provider.
   - In the `src/recorder.py` file, configure the API call using your key.

---

### Running the Game

To start the mini-game, run the `gui.py` script:

```bash
python src/gui.py
```

This will launch the Tkinter window, where you can:
1. **Select a Word**: Choose a word from the dropdown menu.
2. **Record**: Click the "Record" button to start recording your speech.
3. **Play**: Click the "Play" button to listen to your recorded speech.
4. **Save**: Save your recording if needed.
5. **Compare Pronunciation**: Click "Compare Pronunciation" to get feedback on how closely your pronunciation matches the correct pronunciation.
6. **Replay Original Sound**: Click "Replay Original Sound" to listen to the prerecorded pronunciation of the selected word.

---

## Algorithms and Approach

### Speech-to-Text Integration
The speech-to-text functionality is implemented using a third-party API. Audio recordings are sent to the API, which returns a transcription of the spoken words.

### Pronunciation Feedback
Feedback on pronunciation is based on the comparison between the user's recording and prerecorded pronunciations using Mel-frequency cepstral coefficients (MFCC). The following algorithms are used:

1. **MFCC Extraction**:
   - **Librosa**: Used to extract MFCC features from the audio recordings.

2. **Similarity Calculation**:
   - **Euclidean Distance**: Calculates the distance between the MFCC features of the user's recording and the correct pronunciation.
   - **Similarity Score**: The distance is converted to a similarity percentage where a higher percentage indicates closer pronunciation to the correct sample.

   ```python
   def calculate_similarity(user_mfcc, correct_mfcc):
       # Average MFCC features
       user_mfcc_mean = np.mean(user_mfcc, axis=1)
       correct_mfcc_mean = np.mean(correct_mfcc, axis=1)

       # Calculate Euclidean distance
       dist = np.linalg.norm(user_mfcc_mean - correct_mfcc_mean)
       
       # Convert distance to similarity
       max_dist = np.linalg.norm(np.ones_like(user_mfcc_mean) * 100)  # Define max distance
       similarity = 100 - (dist / max_dist) * 100
       return similarity
   ```

### Audio Playback
The project uses `soundfile` and `pyaudio` to handle audio playback. These libraries are used to read and play audio files for both user recordings and prerecorded pronunciations.

```python
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
```

---

## Running Tests

Unit tests are provided to verify the functionality of the game and the Speech-to-Text integration.

To run the tests, use:
```bash
pytest tests/
```

---

## Demo

- A short demo video will be provided in the final submission to show the tool in action.

---

## Challenges

- Choosing a free, reliable speech-to-text API that fits the budget.
- Implementing accurate pronunciation feedback to help users improve their spoken English.

---

## Contributing

Feel free to open issues or submit pull requests to improve the game!

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- Speech-to-Text API Providers (e.g., Deepgram, Google Cloud Speech)
- Python Tkinter documentation and community tutorials


import requests

class SpeechToText:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.deepgram.com/v1/listen"

    def transcribe_audio(self, audio_file_path):
        """
        Transcribes the given audio file into text using the Deepgram API.
        
        Parameters:
        audio_file_path (str): Path to the audio file to transcribe.
        
        Returns:
        str: Transcribed text from the audio.
        """
        headers = {
            'Authorization': f'Token {self.api_key}',
            'Content-Type': 'audio/wav'
        }
        
        with open(audio_file_path, 'rb') as audio:
            response = requests.post(self.api_url, headers=headers, data=audio)
        
        if response.status_code == 200:
            result = response.json()
            return result['results']['channels'][0]['alternatives'][0]['transcript']
        else:
            return f"Error: {response.status_code}, {response.text}"

if __name__ == "__main__":
    stt = SpeechToText(api_key="YOUR_DEEPGRAM_API_KEY")
    transcription = stt.transcribe_audio("path_to_your_audio_file.wav")
    print("Transcription:", transcription)

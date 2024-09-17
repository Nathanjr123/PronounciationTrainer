import requests

# Your Deepgram API key
API_KEY = '96f6f3fbaa97a447f7206431dc7250be62208bb2'

def transcribe_audio(file_path):
    url = "https://api.deepgram.com/v1/listen"
    
    headers = {
        'Authorization': f'Token {API_KEY}',
        'Content-Type': 'audio/wav',
    }

    try:
        # Read the audio file in binary mode
        with open(file_path, 'rb') as audio_file:
            response = requests.post(url, headers=headers, data=audio_file)

        # Check if the request was successful
        if response.status_code == 200:
            print("Transcription successful:")
            print(response.json())
        else:
            print(f"Error: {response.status_code}, {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    # Replace with the path to a valid WAV file
    file_path = "assets/sound.mp3"
    transcribe_audio(file_path)

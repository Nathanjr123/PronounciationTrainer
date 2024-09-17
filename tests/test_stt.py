import unittest
from speech_to_text.stt import SpeechToText

class TestSpeechToText(unittest.TestCase):
    def test_transcribe_audio(self):
        stt = SpeechToText(api_key="TEST_API_KEY")
        transcription = stt.transcribe_audio("path_to_test_audio.wav")
        self.assertIsInstance(transcription, str)

if __name__ == "__main__":
    unittest.main()

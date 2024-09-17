import unittest
from speech_to_text.feedback import PronunciationFeedback

class TestPronunciationFeedback(unittest.TestCase):
    def test_analyze_transcription(self):
        feedback = PronunciationFeedback()
        result = feedback.analyze_transcription("I will schedule a meeting at the garage.")
        self.assertIn("Try pronouncing 'schedule' as 'sked-jool'.", result)

if __name__ == "__main__":
    unittest.main()

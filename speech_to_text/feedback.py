class PronunciationFeedback:
    def __init__(self):
        pass

    def analyze_transcription(self, transcription):
        """
        Provides basic feedback on the pronunciation based on specific keywords.

        Parameters:
        transcription (str): The transcribed text.

        Returns:
        str: Feedback on pronunciation.
        """
        feedback = []

        # Check for common mispronounced words and provide feedback
        mispronounced_words = {
            "schedule": "Try pronouncing 'schedule' as 'sked-jool'.",
            "tomato": "In American English, 'tomato' is pronounced 'tuh-may-toh'.",
            "garage": "Garage is pronounced 'guh-raj' in American English."
        }

        words = transcription.split()
        for word in words:
            if word.lower() in mispronounced_words:
                feedback.append(mispronounced_words[word.lower()])

        if not feedback:
            return "Great job! No major pronunciation errors found."
        
        return " ".join(feedback)

if __name__ == "__main__":
    feedback = PronunciationFeedback()
    sample_transcription = "I will schedule a meeting at the garage."
    result = feedback.analyze_transcription(sample_transcription)
    print("Feedback:", result)

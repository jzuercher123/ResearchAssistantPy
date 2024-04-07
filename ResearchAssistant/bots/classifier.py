from transformers import pipeline


class TextClassifierBot:
    def __init__(self):
        self.classification_pipeline = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

    def classify_text(self, text):
        result = self.classification_pipeline(text)
        return result[0]

# Example usage
classifier_bot = TextClassifierBot()
text = "I really enjoyed the movie, it was fantastic!"
classification_result = classifier_bot.classify_text(text)
print(classification_result)
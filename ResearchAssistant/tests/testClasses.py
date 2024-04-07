from researchAssistant.config import HUGGINGFACE_API_KEY
from researchAssistant.ScrapingBotLib import *
from researchAssistant.ResearchApp import DatabaseHandler
from transformers import pipeline

API_KEY = HUGGINGFACE_API_KEY


class DataHandler:
    def __init__(self):
        self.data = {
            "scraper": None,
            "summarizer": None,
            "relevancy_filter": None,
            "text_classifier": None
        }

    def receive(self, data, data_type):
        if data_type:
            self.data[data_type] = data
        else:
            return

    def send(self, data):
        return self.data[data]


class Summarizer:
    def __init__(self, data_handler: DataHandler):
        self.data_handler = data_handler
        self.data_type = "summarizer"
        self.data = None

    def summarize(self, data):
        # Implement text summarization logic here
        pass

    def send_summary(self, summary, recipient):
        # Send the summary to the specified recipient
        pass

    def receive_text(self, text):
        self.data = text


class Scraper:
    def __init__(self, data_handler: DataHandler):
        self.raw_text = None
        self.cleaned_text = None
        self.data_handler = data_handler
        self.data_type = "scraper"

    def scrape(self, url):
        # Implement web scraping logic here
        return extract_text_from_site(url)

    def clean_text(self, html):
        # Implement text cleaning logic here
        self.cleaned_text = clean_html_body(html)
        return self.cleaned_text

    def send_clean_text(self, cleaned_text):
        return self.data_handler.receive(cleaned_text, data_type=self.data_type)


class RelevancyFilter:
    def __init__(self, data_handler: DataHandler):
        self.data = None
        self.data_type = "relevancy_filter"
        self.data_handler = data_handler

    def receive_data(self, data):
        self.data = data

    def is_relevant(self, data):
        # Implement relevancy filtering logic here
        pass

    def send_data(self, data):
        self.data_handler.receive(data, data_type=self.data_type)


class TextClassifier:
    def __init__(self, data_handler):
        self.data_handler = data_handler
        self.data = None
        self.sorted_data = None
        self.data_type = "text_classifier"

    def receive_data(self, data):
        self.data = data

    def sort_data(self, data):
        # Implement data sorting logic here
        pass

    def send_sorted_data(self, data):
        self.data = {"classification": f"{data}"}

    def send_to_db(self, db_handler: DatabaseHandler):
        self.db_handler = db_handler.receive_sorted_data(data='', classification='')
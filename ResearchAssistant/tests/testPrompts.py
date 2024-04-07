from  import HUGGINGFACE_API_KEY

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
API_KEY = HUGGINGFACE_API_KEY


def give_me_keywords_for(topic, number=10)-> dict:
    keywords = {
        "input": f"Give me {str(number)} keywords for this topic: {topic}"
    }
    return keywords


def is_relevant_site(topic, url):
    answer = {
        "input": f"Please only reply to the question with a True or False value.\
         Is {url} web page related to {topic}?"
    }
    return answer


import requests
from bs4 import BeautifulSoup
from researchAssistant.config import HUGGINGFACE_API_KEY
from urllib.parse import urljoin

# TODO: Make SummarizerBot() next in a new file

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-xxl"
headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}


# Bot which utilizes a hugging face api {api_here} to do the following:
# 1. Extract data from a web page, save text in an attribute, also save links on web page
# 2. Says if page relevant to topic? True or False value returned
#    --> If True: pass data to SummaryBot
#    --> If false: move to next link in series, retry 1 and 2
class ScrapingBot:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url
        self.scraped_text = None
        self.cleaned_text = None
        self.links = []

    def scrape_article(self, url):
        return extract_text_from_site(url)

    def spider_website(url, max_pages=10):
        visited_pages = set()
        pages_to_visit = set([url])

        while pages_to_visit and len(visited_pages) < max_pages:
            current_url = pages_to_visit.pop()

            if current_url in visited_pages:
                continue

            try:
                response = requests.get(current_url)
                if response.status_code == 200:
                    visited_pages.add(current_url)
                    print("Visiting:", current_url)

                    soup = BeautifulSoup(response.content, 'html.parser')

                    for link in soup.find_all('a', href=True):
                        next_link = urljoin(current_url, link['href'])
                        if next_link not in visited_pages:
                            pages_to_visit.add(next_link)
            except Exception as e:
                print("Error accessing:", current_url)
                print(e)

        return visited_pages

    def clean_text(self, html):
        text = get_body_from_html()
        clean_html_body()

    def generate_text(self, text):
        pass



def clean_html_body(html):
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.find('body')

    if body:
        text = body.get_text()

        # Clean up formatting
        text = ' '.join(text.split())  # Remove extra whitespaces and newlines

        return text
    else:
        return None


# process a list of query strings whereby each new element is placed into
# the url below. replace https://example.com with your website.
def process_query_strings(query_strings):
    if not query_strings:
        return

    query_string = query_strings[0].strip()  # pull first item from query string
    url = f"https://example.com/{query_string}"  # place item in url

    response = requests.get(url)  # send get request with url
    print(f"URL: {url}, Response: {response.text}")  # print html response

    remaining_query_strings = query_strings[1:]  #
    process_query_strings(remaining_query_strings)


# get html content from a website
def extract_text_from_site(site):
    response = requests.get(url=site)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.prettify()


# get title content
def get_title_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    title_element = soup.find('title').get_text()
    if title_element:
        return title_element
    else:
        return "title not found"

def get_body_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    body_element = soup.find('body').get_text()
    if body_element:
        return body_element
    else:
        return "body not found"


def make_section_into_list(html, html_tag):
    soup = BeautifulSoup(html, 'html.parser')
    section = soup.find(f"{html_tag}")
    if section:
        text = section.get_text()
        # Clean up formatting
        return text.split()
    else:
        return f"{html_tag} or {section} or text in {section} do not exist"


# Get each attr from html text and number them
def get_attrs_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    tag_types = {}
    for tag in soup.find_all():
        tag_type = tag.name
        if tag_type in tag_types:
            tag_types[tag_type] += 1
        else:
            tag_types[tag_type] = 1
        return tag_types


# Get content from blog article (yet to be tested)
def get_article_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find the main article content based on common HTML tags
    article_content = soup.find('article')
    if not article_content:
        article_content = soup.find('div', class_='article-content')
    if article_content:
        # Extract text from the article content
        article_text = ""
        for paragraph in article_content.find_all('p'):
            article_text += paragraph.get_text() + "\n"
        return article_text
    else:
        return "Article content not found"


#  UNCOMMENT TO TEST HUGGINGFACE API
# def api_query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json()
#
#
# output = api_query({
#     "inputs": "What is google.com",
#})

import requests
import threading
import time
import sqlite3
import openai
import queue
import logging
import functools
from researchAssistant.config import API_KEY

# Globals
global threadpool
global tasks

class ThreadPool:
    def __init__(self, num_threads):
        self.tasks = queue.Queue()
        self.workers = []
        for _ in range(num_threads):
            worker = threading.Thread(target=self._work)
            worker.daemon = True
            worker.start()
            self.workers.append(worker)

    def _work(self):
        while True:
            task = self.tasks.get()
            if task is None:
                break
            task()

    def add_task(self, task):
        self.tasks.put(task)

    def wait_completion(self):
        self.tasks.join()

    def shutdown(self):
        for _ in range(len(self.workers)):
            self.tasks.put(None)
        for worker in self.workers:
            worker.join()

    def thread(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self.add_task(func)


        return wrapper


###### class OpenAIAPI:
class OpenAIAPI:
    def __init__(self, API_KEY: str):
        openai.api_key = API_KEY
        self.usage = """
        Class OpenAIAPI(api_key)
             =>> openapi = OpenAIAPI('sdafwerw3423fsdf')
             ==> openapi.query(api_endpoint_url: str, query_string: str) -> str:
                    ==> basic api_query method. Send http headers referenced here: 
                    {https://beta.openai.com/docs/)}
            
        """

    # Query openai to perform a function - Will be used by all bots
    def query(self, prompt_str: str) -> str:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"{prompt_str}"}],
            stream=True
        )
        return response[0].text

    def usage(self):
        print(self.usage)


###### class ResearchBot
class ResearchBot:
    # TODO Create a threading method implementation for this bot and for PromptCorrectionBot
    def __init__(self, api: OpenAIAPI, topic: str):
        self.api = api
        self.topic = topic
        self.running = False
        self.api_key = api.api_key
        self.thread = self.__hash__()

    def stop(self):
        self.running = False
        exit()

    def set_topic(self, topic: str) -> str:
        self.topic = topic
        return topic

    # TODO Finish this method
    def research(self) -> str:
        # TODO Add correct api endpoint url
        self.api.query(api_endpoint_url=API_ENDPOINT_URL, query=self.topic)
        self.running = True
        search_query = ""

    def get_accuracy_grade(self, grade: int) -> int:
         return grade


class PromptCorrectionBot:
    def __init__(self, api: OpenAIAPI, researcher: ResearchBot):
        self.api = api
        self.researcher = researcher
        self.thread = None

    def grade_accuracy(self, text):
        prompt = f"Given text: {text}\nTopic: {self.researcher.topic}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50
        )
        accuracy_text = response.choices[0].text.strip()
        # Perform some logic to determine accuracy rating
        # This is a placeholder logic, you can adjust it based on your requirements
        accuracy_score = len(set(accuracy_text.lower().split()) & set(topic.lower().split())) / len(
            set(topic.lower().split())) * 10
        return round(accuracy_score, 1)

    def suggest_corrections(self, input_text) -> str :
        prompt = f"Original text: {input_text}\nTopic: {self.researcher.topic}\nSuggested corrections:"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50
        )
        return response.choices[0].text.strip()


###### class DatabaseHandler()
class DatabaseHandler:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.data = None

    def receive_sorted_data(self, data, classification):
        self.data = {classification: data}

    def create_table(self, table_name: str, columns: str)-> None:
        columns_str = ', '.join(columns)
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def insert_data(self, table_name: str, data)-> None:
        placeholders = ', '.join(['?'] * len(data))
        insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        self.cursor.execute(insert_query, data)
        self.conn.commit()

    def select_data(self, table_name: str, condition=None)-> any:
        select_query = f"SELECT * FROM {table_name}"
        if condition:
            select_query += f" WHERE {condition}"
        self.cursor.execute(select_query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()


##### class ResearchApp
class ResearchAppCLI:
    def __init__(self, bot: ResearchBot, db: DatabaseHandler):
        self.bot = bot
        self.db = db

    # run app
    def run(self):
        # START PROGRAM CLI
        print("Starting...")
        # Accept api key
        self.bot.api = str(input(">>> API Key: "))

        # set topic
        topic = str(input(">>> Enter topic or keywords to research\
        separated by commas: "))

        # Name database
        db_name = str(input(">>> Enter Database name: "))

        # initiate server to run bots and db
        server = Server(self.bot, db_handler=DatabaseHandler(f"{db_name}"))
        server.start()

        # initiate research bot
        self.bot.running = True
        self.bot.set_topic(topic=topic)
        print("Running... \n")

        # initiate prompt bot
        prompt = PromptCorrectionBot(api=self.bot.api, researcher=self.bot)
        self.bot.research()

        # TODO make variable a passable string from the output of the research to be able to be graded and decide next step
        output = ""

        # pause to not overload system between grading and scraping
        time.sleep(1)
        grade = self.bot.get_accuracy_grade(prompt.grade_accuracy(output))

        # if accuracy is less than 8, promptbot will suggest changes
        # SentimentAnalyzer() will review changes and output a single word topic or set of keywords # TODO Make SentimentBot() class
        # ResearchBot() will accept these keywords and set new topic via ResearchBot.set_topic(changes)
        # while loop with flag set to True to enable looping through the sequence
        flag = True
        while Flag:
            if grade <= 8:
                prompt.suggest_corrections(output)
                # TODO Create a method within the ResearchBot class which will take suggestions and make changes
            else:
                self.bot.set_topic(self.bot.topic)
                self.bot.research()
            time.sleep(1)
            continue


class Server:
    def __init__(self, research_app: ResearchBot, db_handler: DatabaseHandler):
        self.research_app = research_app
        self.db_handler = db_handler
        self.running = False
        self.thread = None

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.run())
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread is not None:
            self.thread.join()

    def run(self):
        while self.running:
            # Perform research
            results = self.research_app.research()

            # Store results in database
            self.db_handler.insert(results)

            # Wait for a while before next iteration
            time.sleep(60)  # adjust this to control the frequency of research




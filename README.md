Brief Explanation of Project Goals and Methodology:
-------------------------------

1. **Define the Topic**: Clearly define the topic that the bot will be researching. This could be a specific keyword, a set of keywords, or a more complex query.
    
2. **Web Scraping**: Use a library like BeautifulSoup in Python to scrape web pages for information related to the defined topic. You’ll need to make HTTP requests to web pages, parse the HTML response to find the information you’re interested in, and handle any pagination or navigation between pages.
    
3. **Information Extraction**: Once you’ve scraped the web pages, you’ll need to extract the relevant information from them. This might involve parsing the text content of the pages, extracting metadata, or even downloading images or other resources.
    
4. **Database Storage**: After extracting the information, you’ll need to store it in a database. The specific type of database you use (SQL, NoSQL, etc.) will depend on the nature of the data you’re working with.
    
5. **Continuous Operation**: To have the bot operate continuously, you could host it on a server and use a task scheduler like cron to run your script at regular intervals.
    
6. **Handling Updates**: Depending on your specific use case, you might also need to handle updates to the data. This could involve checking for new information on a regular basis, or maintaining a history of changes to the data over time.
    
7. **Legal and Ethical Considerations**: Always respect the terms of service of the websites you’re scraping, and do not scrape websites that explicitly disallow it. Be mindful of the amount of requests you’re making to avoid causing issues for the website. Also, consider the privacy implications of the data you’re collecting.

Overall Process Algorithm:
---------------------------------------
1. Scraper scrapes web articles given a topic to start from (the scraper scrapes from google search)
2. Scraper sends cleaned_text to RelevancyFilter()
3. RelevancyFilter() determines if articles are relevant
4. If relevant: send CleanedText() to Summarizer(); else: 
5. Summarizer() summarizes text in summary
6. Summarizer sends summary to TextClassifier()
7. TextClassifier() Finally passes results to DatabaseHandler() 
8. DatabaseHandler() saves  

More Visual:
----------------------------------------------------
Scraper -->  RelevancyFilter --> Summarizer --> Text_Classifier --> DatabaseHandler



References:
-------------------------------------------------
#python #API  #coding 
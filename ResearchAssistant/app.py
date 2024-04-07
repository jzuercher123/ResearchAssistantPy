import ResearchApp


def change_topic():
    topic = str(input("topic: "))
    return topic


if __name__ == "__main__":
    with open("api_key.txt", "rb") as f:
        key = f.read()
        openapi = ResearchApp.OpenAIAPI(api_key=key)
    bot = ResearchApp.ResearchBot(api=openapi, topic=change_topic())
    research_app = ResearchApp.ResearchAppCLI(bot=bot, db=ResearchApp.DatabaseHandler("db_example"))
    research_app.run()



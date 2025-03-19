import dotenv
import os
from src.logs import Logs
from src.utils_02_html_to_markdown import HtmlToMarkdown


dotenv.load_dotenv(override=True)
SCRAPING_PATH = os.getenv('OUTPUT_PATH') + 'scraping/'

if __name__ == "__main__":
    logs = Logs()

    #00 INIT
    if logs.status:
        exit(0)
    logs.logging_msg("[main | __main__] START", 'WARNING')
    
    #01 scraping

    #02 transform HTML to markdown and clean data
    HtmlToMarkdown(logs, SCRAPING_PATH)

    #03 save in txt file

    #04 Global DB


    logs.logging_msg("[main | __main__] END", 'WARNING')
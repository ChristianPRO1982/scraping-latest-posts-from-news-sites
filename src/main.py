import dotenv
import os
from src.logs import Logs
from src.utils_02_html_to_markdown import HtmlToMarkdown
from src.utils_03_save_txt import MarkdownToTxt


dotenv.load_dotenv(override=True)
SCRAPING_PATH = os.getenv('OUTPUT_PATH') + 'scraping/'
MARKDOWN_FILES_PATH = os.getenv('OUTPUT_PATH') + 'markdown_files/'

if __name__ == "__main__":
    logs = Logs()

    #00 INIT
    if logs.status: exit(0)
    logs.logging_msg("[main | __main__] START", 'WARNING')
    
    #01 scraping

    #02 transform HTML to markdown and clean data
    html_to_markdown = HtmlToMarkdown(logs, SCRAPING_PATH)
    if not html_to_markdown.status: exit(1)

    #03 save in txt file
    markdown_to_txt = MarkdownToTxt(logs, html_to_markdown, MARKDOWN_FILES_PATH)
    if not markdown_to_txt.status: exit(2)

    #04 Global DB


    logs.logging_msg("[main | __main__] END", 'WARNING')
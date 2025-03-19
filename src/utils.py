import os
import pandas as pd
from bs4 import BeautifulSoup
import html2text



class CleanJsonScraped:
    def __init__(self, logs, json_path:str):
        self.logs = logs
        self.json_path = json_path
        self.df = None
        self.DEBUG = os.getenv('DEBUG')
        
        self.logs.logging_msg(f"[{self.__class__.__name__} | __init__] START")


    def read_and_clean_csv_file(self, file_path):
        prefix = f'[{self.__class__.__name__} | read_and_clean_csv_file]'

        try:
            self.logs.logging_msg(f"{prefix} start", 'DEBUG')
            self.df = pd.read_json(file_path)
            return True
        
        except Exception as e:
            self.df = None
            self.logs.logging_msg(f"{prefix} {e}", 'ERROR')
            return False


    def clean_html_to_markdown(self, html_content):
        prefix = f'[{self.__class__.__name__} | clean_html_to_markdown'

        try:
            self.logs.logging_msg(f"{prefix} start", 'DEBUG')
            
            soup = BeautifulSoup(html_content, "html.parser")
            
            # Suppress unnecessary tags
            for tag in soup(["script", "style", "meta", "noscript"]):
                tag.decompose()
            
            # Convert to markdown
            markdown_converter = html2text.HTML2Text()
            markdown_converter.body_width = 0  # Prevents unwanted line wrapping
            markdown_converter.ignore_images = False  # Keep image links
            markdown_converter.ignore_links = False   # Keep hyperlinks
            
            markdown_text = markdown_converter.handle(str(soup))
            print(markdown_text)
            return markdown_text
        
        except Exception as e:
            self.logs.logging_msg(f"{prefix} {e}", 'ERROR')
            return None
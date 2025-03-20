import pandas as pd
from bs4 import BeautifulSoup
import html2text
from urllib.parse import urlparse



class CleanJsonScraped:
    def __init__(self, logs, json_path:str):
        self.logs = logs
        self.json_path = json_path
        self.df = None
        self.articles = None

        self.status = True
        
        self.logs.logging_msg(f"[{self.__class__.__name__} | __init__] START")
        self.read_json_file(json_path)
        self.read_json()


    def read_json(self):
        prefix = f'[{self.__class__.__name__} | read_json]'

        try:
            self.logs.logging_msg(f"{prefix} start", 'DEBUG')

            self.articles = []
            
            for index, row in self.df.iterrows():
                content = self.clean_html_to_markdown(row['content'])

                if content:
                    self.articles.append(Article(
                        self.logs,
                        row['url'],
                        row['title'],
                        row['author'],
                        row['date'],
                        content
                        ))

        except Exception as e:
            self.logs.logging_msg(f"{prefix} {e}", 'ERROR')
            self.status = False


    def read_json_file(self, file_path:str)->bool:
        prefix = f'[{self.__class__.__name__} | read_and_clean_csv_file]'

        try:
            self.logs.logging_msg(f"{prefix} start", 'DEBUG')
            self.df = pd.read_json(file_path)
            return True
        
        except Exception as e:
            self.df = None
            self.logs.logging_msg(f"{prefix} {e}", 'WARNING')
            return False


    def clean_html_to_markdown(self, html_content:str)->str:
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
            
            return markdown_text
        
        except Exception as e:
            self.logs.logging_msg(f"{prefix} {e}", 'WARNING')
            return None


####################################################################################################


class Article:
    def __init__(self, logs, url:str, title:str, author:str, date:str, content:str):
        self.logs = logs
        self.domain = urlparse(url).netloc
        self.url = url
        self.title = title
        self.author = author
        self.date = date
        self.content = content
import os
from src.utils import CleanJsonScraped



class HtmlToMarkdown:
    def __init__(self, logs, scraping_path:str):
        self.logs = logs
        self.scraping_path = scraping_path
        self.logs.logging_msg(f"[{self.__class__.__name__} | __init__] START")
        self.json_files = None
        self.news_sites = None

        self.status = True

        self.list_json_files()
        self.clean_json()


    def list_json_files(self):
        prefix = f'[{self.__class__.__name__} | list_json_files]'
        
        try:
            self.logs.logging_msg(f"{prefix} start", 'DEBUG')
            
            self.json_files = [f for f in os.listdir(self.scraping_path) if f.endswith('.json')]
            self.logs.logging_msg(f"{prefix} found {len(self.json_files)} json files", 'DEBUG')
            
            for json_file in self.json_files:
                self.logs.logging_msg(f"{prefix} processing file: {json_file}", 'DEBUG')
            
        except Exception as e:
            self.logs.logging_msg(f"{prefix} {e}", 'ERROR')
            self.status = False
    

    def clean_json(self):
        prefix = f'[{self.__class__.__name__} | clean_json]'

        try:
            self.logs.logging_msg(f"{prefix} start", 'DEBUG')

            self.news_sites = []

            for json_file in self.json_files:
                file_path = f"{self.scraping_path}{json_file}"
                self.logs.logging_msg(f"{prefix} processing file: {file_path}", 'DEBUG')
                self.news_sites.append(CleanJsonScraped(self.logs, file_path))
            
        except Exception as e:
            self.logs.logging_msg(f"{prefix} {e}", 'ERROR')
            self.status = False
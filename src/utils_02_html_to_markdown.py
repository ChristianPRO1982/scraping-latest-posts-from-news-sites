import os
from src.utils import CleanJsonScraped



class HtmlToMarkdown:
    def __init__(self, logs, scraping_path:str):
        self.logs = logs
        self.scraping_path = scraping_path
        self.logs.logging_msg(f"[{self.__class__.__name__} | __init__] START")
        self.scraping_json = None

        self.status = True

        self.list_json_files()


    def list_json_files(self):
        prefix = f'[{self.__class__.__name__} | list_json_files]'
        
        try:
            self.logs.logging_msg(f"{prefix} start", 'DEBUG')
            
            self.scraping_json = []
            
            json_files = [f for f in os.listdir(self.scraping_path) if f.endswith('.json')]
            self.logs.logging_msg(f"{prefix} found {len(json_files)} json files", 'DEBUG')
            
            for json_file in json_files:
                self.logs.logging_msg(f"{prefix} processing file: {json_file}", 'DEBUG')
                self.scraping_json.append(json_file)
            
        except Exception as e:
            self.logs.logging_msg(f"{prefix} {e}", 'ERROR')
            self.status = False
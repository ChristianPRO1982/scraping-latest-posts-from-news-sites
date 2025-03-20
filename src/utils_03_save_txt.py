


class MarkdownToTxt:
    def __init__(self, logs, html_to_markdown, markdown_files_path:str):
        self.logs = logs
        self.html_to_markdown = html_to_markdown
        self.markdown_files_path = markdown_files_path

        self.logs.logging_msg(f"[{self.__class__.__name__} | __init__] START")
        self.status = True
        self.list_html()


    def list_html(self):
        prefix = f'[{self.__class__.__name__} | list_html]'
        
        try:
            self.logs.logging_msg(f"{prefix} start", 'DEBUG')

            for news_site in self.html_to_markdown.news_sites:
                for article in news_site.articles:
                    self.logs.logging_msg(f"{prefix} {article.title}", 'DEBUG')
                    self.save_txt(article)

        except Exception as e:
            self.logs.logging_msg(f"{prefix} {e}", 'ERROR')
            self.status = False


    def save_txt(self, article):
        prefix = f'[{self.__class__.__name__} | save_txt]'

        try:
            self.logs.logging_msg(f"{prefix} start", 'DEBUG')

            complete_markdown = self.generate_complete_markdown(article)

            if complete_markdown:
                file_path = f"{self.markdown_files_path}{article.url.replace('/', '_')}.md"
                file_path = file_path.replace('\n', '').replace('\r', '')
                with open(file_path, 'w') as file:
                    file.write(complete_markdown)

        except Exception as e:
            self.logs.logging_msg(f"{prefix} {e}", 'WARNING')


    def generate_complete_markdown(self, article):
        prefix = f'[{self.__class__.__name__} | generate_complete_markdown]'

        try:
            self.logs.logging_msg(f"{prefix} start", 'DEBUG')

            url = article.url
            domain = article.domain
            title = article.title
            author = article.author
            date = article.date
            content = article.content

            complete_markdown = f"# {domain} - {title}\n\n"
            complete_markdown += f"**Source :** *[{url}]({url})*\n\n"
            complete_markdown += f"**Auteur :** {author}\n\n"
            complete_markdown += f"**Date :** {date}\n\n___\n\n"
            complete_markdown += f"{content}"

            return complete_markdown

        except Exception as e:
            self.logs.logging_msg(f"{prefix} {e}", 'WARNING')
            return None
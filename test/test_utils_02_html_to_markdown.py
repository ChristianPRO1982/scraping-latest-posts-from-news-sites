import pytest
from src.utils_02_html_to_markdown import HtmlToMarkdown
from src.logs import Logs

logs = Logs()

def test_HtmlToMarkdown():
    assert HtmlToMarkdown(logs, './test/').status == True
    assert HtmlToMarkdown(logs, './nope/').status == False
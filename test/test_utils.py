import pytest
from src.utils import CleanJsonScraped
from src.logs import Logs

logs = Logs()

def test_read_and_clean_csv_file():
    clean_json = CleanJsonScraped(logs, './test/test.json')
    
    assert clean_json.read_and_clean_csv_file('./test/test.json') == True
    assert clean_json.read_and_clean_csv_file('') == False
    assert clean_json.read_and_clean_csv_file('test.json') == False
    assert clean_json.read_and_clean_csv_file('test') == False

def test_clean_html_to_markdown():
    clean_json = CleanJsonScraped(logs, './test/test.json')
    
    assert clean_json.clean_html_to_markdown('test') == 'test\n'
    assert clean_json.clean_html_to_markdown('<html><head><title>Test 01</title></head><body><h1>Test 01</h1><p>Author: PyTest</p><h2>Titre 2</h2><p>Date: 13 mai 2020</p><p>Content</p></body></html>') == '''# Test 01

Author: PyTest

## Titre 2

Date: 13 mai 2020

Content\n'''
    assert clean_json.clean_html_to_markdown('<html><head><title>Example 02</title></head><body><h1>Example 02</h1><p>Author: ExampleAuthor</p><p>Date: 14 juin 2021</p><h2>Titre 2</h2><h3>Titre 3</h3><p><em>Example</em> content</p></body></html>') == '''# Example 02

Author: ExampleAuthor

Date: 14 juin 2021

## Titre 2

### Titre 3

 _Example_ content\n'''
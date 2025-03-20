# scraping-latest-posts-from-news-sites

[![Latest Release](https://img.shields.io/github/release/ChristianPRO1982/scraping-latest-posts-from-news-sites.svg)](https://github.com/ChristianPRO1982/scraping-latest-posts-from-news-sites/releases/latest)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/github/license/ChristianPRO1982/scraping-latest-posts-from-news-sites.svg)](https://github.com/ChristianPRO1982/scraping-latest-posts-from-news-sites/blob/main/LICENSE)

To keep an eye on NLP topics from news websites

[Flowchart](https://github.com/ChristianPRO1982/ai-subject-monitoring-project?tab=readme-ov-file#NS-flowchart)

## files

### .env

```bash
DEBUG=1 # 0: off, 1: on, 2: on with debug messages, 3: on with only SQL queries, 4: for pytest
LOG_RETENTION_DAYS=63
LOGS_PATH='./logs/'

OUTPUT_PATH='./scrapy_news/scrapy_news/output/'
```

## launchers

### app

```bash
PYTHONPATH=$(pwd) python src/main.py
```

### Scrapy

```bash
scrapy crawl larevueia -O output/scraping/larevueia.json --set LOG_LEVEL=WARNING --logfile=output/scrapy_logs/scrapy.log
```

### Pytest

```bash
PYTHONPATH=$(pwd) pytest
```

or

```bash
rm ???.db && PYTHONPATH=$(pwd) pytest
```
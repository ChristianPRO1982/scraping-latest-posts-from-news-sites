import dotenv
import os
from logs import init_log, logging_msg
import utils



##################################################
##################################################
##################################################

############
### MAIN ###
############
dotenv.load_dotenv(override=True)
init_log()
logging_msg("START PROGRAM", "WARNING")

<<<<<<< HEAD
logging_msg("utils.parse_json START", 'WARNING')
RSS_FEEDS = utils.parse_json(os.getenv("RSS_FEEDS"))
FOLDER_PATH = os.getenv("FOLDER_PATH")
PREFIX = os.getenv("PREFIX")
=======
RSS_FEEDS = utils.parse_json(os.getenv("RSS_FEEDS"))
FOLDER_PATH = os.getenv("FOLDER_PATH")
PREFIX = os.getenv("PREFIX")
FFMPEG_PATH = os.getenv("FFMPEG_PATH")
>>>>>>> 014f12c221f5ee051161d3136d3060a6da193ddd

if utils.init():
    for podcast in RSS_FEEDS:
        category = podcast["category"]
        name = podcast["name"]
        rss_feed = podcast["rss_feed"]
<<<<<<< HEAD
        logging_msg(f"utils.parse_rss_feed {name} START", 'WARNING')
        stop_and_go = utils.parse_rss_feed(category, name, rss_feed)
        if stop_and_go:
            logging_msg("utils.download_podcast START", 'WARNING')
            utils.download_podcast(FOLDER_PATH, PREFIX)
    
    logging_msg("utils.transcribe_all_podcasts START", 'WARNING')
    stop_and_go = utils.transcribe_all_podcasts()
    if stop_and_go:
        logging_msg("utils.summarize START", 'WARNING')
        # utils.summarize()
=======
        logging_msg(f"Processing {name}...")
        logging_msg("utils.parse_rss_feed START")
        stop_and_go = utils.parse_rss_feed(category, name, rss_feed)
        if not stop_and_go:
            continue
        logging_msg("utils.download_podcast START")
        stop_and_go = utils.download_podcast(FOLDER_PATH, PREFIX)
        if not stop_and_go:
            continue
        logging_msg("utils.transcribe_all_podcasts START")
        stop_and_go = utils.transcribe_all_podcasts(FOLDER_PATH, PREFIX, FFMPEG_PATH)
        if not stop_and_go:
            continue
>>>>>>> 014f12c221f5ee051161d3136d3060a6da193ddd

logging_msg("END PROGRAM", "WARNING")

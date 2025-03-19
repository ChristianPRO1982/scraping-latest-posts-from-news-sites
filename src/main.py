import os
import dotenv
from logs import Logs


dotenv.load_dotenv(override=True)


if __name__ == "__main__":
    logs = Logs()

    if not logs.status:
        pass
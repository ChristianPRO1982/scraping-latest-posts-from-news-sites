


class GlobalDB:
    def __init__(self, logs):
        self.logs = logs

        self.logs.logging_msg(f"[{self.__class__.__name__} | __init__] START")
        self.status = True
import logging


class Logger:
    """logger class for set logs to metro.log"""
    def __init__(self):
        self.format = ' %(levelname)s: %(asctime)s - %(message)s'
        self.level = logging.DEBUG
        logging.basicConfig(filename='metro.log', format=self.format, level=self.level)


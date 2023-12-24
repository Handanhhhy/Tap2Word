import logging
import sys


class Logger:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    def log2file(self):
        file_handler = logging.FileHandler('output.log', encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(self.formatter)
        self.logger.addHandler(file_handler)

    def log2console(self):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(self.formatter)
        self.logger.addHandler(console_handler)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

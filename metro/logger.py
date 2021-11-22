import logging

fmt = '%(name)s >>> %(levelname)s: %(asctime)s - %(message)s'
level = logging.DEBUG
logging.basicConfig(filename='metro.log', format=fmt, level=level)


class Logger:
    """logger class for set logs to metro.log"""
    logger = None

    @classmethod
    def set_logger(cls, logger_name):
        cls.logger = logging.getLogger(logger_name)

    @classmethod
    def debug(cls, msg):
        logging.debug(msg)

    @classmethod
    def info(cls, msg):
        logging.info(msg)

    @classmethod
    def warning(cls, msg):
        logging.warning(msg)

    @classmethod
    def error(cls, msg):
        logging.error(msg)

    @classmethod
    def critical(cls, msg):
        logging.critical(msg)

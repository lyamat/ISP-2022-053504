import logging


def init_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("[%(levelname)s] %(asctime)s  — %(message)s")

    sh = logging.StreamHandler()
    sh.setFormatter(formatter)

    fh = logging.FileHandler(filename="universal_parser/logs/test.log")
    fh.setFormatter(formatter)

    logger.addHandler(sh)
    logger.addHandler(fh)
    logger.propagate = True
    return logger

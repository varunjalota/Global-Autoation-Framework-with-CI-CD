import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="reportlog.log", format="%(asctime)s: %(levelname)s: %(message)s",
                            datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.DEBUG)
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger

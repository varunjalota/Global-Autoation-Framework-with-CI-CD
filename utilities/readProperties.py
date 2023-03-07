import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getapplicationurl():
        url = config.get('common info', 'baseURL')
        return url

import configparser

config = configparser.ConfigParser()
config.read('conf/application.conf')


# API-Service calling URL
api_base_service_url = "/glens"
PORT = 5901
RETRY_COUNT = 1


# getting details from the configuration file for the Logger
LOG_LEVEL = config.get('LOG', 'log_level')
LOG_BASEPATH = config.get('LOG', 'base_path')
LOG_FILE_NAME = LOG_BASEPATH + config.get('LOG', 'file_name')
LOG_HANDLERS = config.get('LOG', 'handlers')
LOGGER_NAME = config.get('LOG', 'logger_name')

# getting mysql details

USER_NAME = config.get('MYSQL', 'user_name')
PASSWORD = config.get('MYSQL', 'pass')
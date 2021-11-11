# from scripts.constants import app_constants
# import copy

from scripts.constants import app_constants
from scripts.utilities.mongoUtility import MongoUtility
from scripts.logging.monitoring import logger as log
from scripts.utilities.mysql_utility import MySQLUtility
from datetime import datetime
from dateutil import relativedelta
import time


class DewHandler(object):
    def __init__(self):
        try:
            self.mysql_obj = MySQLUtility()
        except Exception as e:
            log.error(str(e), exc_info=True)
            raise Exception("Exception while establishing connection to Mysql database")

    def show_sql_data(self):
        try:
            table_data = self.mysql_obj.read()
            final_json = dict()
            final_json['table_data'] = table_data
            # final_json = {"ok": "data he"}
            return final_json
        except Exception as e:
            log.error(str(e))
            raise Exception("Exception in List Reports Handler")


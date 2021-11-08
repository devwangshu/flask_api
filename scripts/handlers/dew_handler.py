# from scripts.constants import app_constants
# import copy

from scripts.constants import app_constants
from scripts.utilities.mongoUtility import MongoUtility
from scripts.logging.monitoring import logger as log
from datetime import datetime
from dateutil import relativedelta
import time


class DewHandler(object):
    def __init__(self):
        try:
            self.mongo_obj = MongoUtility()
        except Exception as e:
            log.error(str(e), exc_info=True)
            raise Exception("Exception while establishing connection to database")

    def show_sql_data(self):
        try:
            # data = self.mongo_obj.read_without_inputjson('monitoring_email', 'email_status')
            # reports = self.mongo_obj.read_without_inputjson('monitoring_email', 'reports_collection')
            #
            # final_json = dict()
            # table_data = list()
            # for each in data:
            #     if each['service_name'] not in table_data:
            #         table_data.append(each['service_name'])
            # for each in reports:
            #     if each['to_be_monitored'] == 'Yes':
            #         if each['service_name'] not in table_data:
            #             table_data.append(each['service_name'])
            #
            # final_json['table_data'] = table_data
            final_json = {"ok": "data he"}
            return final_json
        except Exception as e:
            log.error(str(e))
            raise Exception("Exception in List Reports Handler")


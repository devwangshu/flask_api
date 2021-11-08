# from scripts.constants import app_constants
# import copy

from scripts.constants import app_constants
from scripts.utilities.mongoUtility import MongoUtility
from scripts.logging.monitoring import logger as log
from datetime import datetime
from dateutil import relativedelta
import time


class MonitoringHandler(object):
    def __init__(self):
        try:
            self.mongo_obj = MongoUtility()
        except Exception as e:
            log.error(str(e), exc_info=True)
            raise Exception("Exception while establishing connection to database")

    def list_report_services(self):
        try:
            data = self.mongo_obj.read_without_inputjson('monitoring_email', 'email_status')
            reports = self.mongo_obj.read_without_inputjson('monitoring_email', 'reports_collection')
            final_json = dict()
            table_data = list()
            for each in data:
                if each['service_name'] not in table_data:
                    table_data.append(each['service_name'])
            for each in reports:
                if each['to_be_monitored'] == 'Yes':
                    if each['service_name'] not in table_data:
                        table_data.append(each['service_name'])

            final_json['table_data'] = table_data
            return final_json
        except Exception as e:
            log.error(str(e))
            raise Exception("Exception in List Reports Handler")

    def service_email_details(self, input_json):
        try:
            service_name = input_json.get('service_name')
            data = self.mongo_obj.read({'service_name': service_name},
                                       'monitoring_email', 'email_status')
            final_json = app_constants.Settings.email_status_json
            table_data = list()
            vendor_list = list()
            count = 0
            for each in data:
                count = count + 1
                if count == 1:
                    final_json['frequency'] = each['report_type']
                    date = each['timestamp']
                    if each['report_type'] == 'daily':
                        time1 = datetime.fromtimestamp(int(date) / 1000) + relativedelta.relativedelta(days=1)
                    elif each['report_type'] == 'quarterly':
                        time1 = datetime.fromtimestamp(int(date) / 1000) + relativedelta.relativedelta(months=6)
                    elif each['report_type'] == 'monthly':
                        time1 = datetime.fromtimestamp(int(date) / 1000) + relativedelta.relativedelta(months=1)
                    elif each['report_type'] == 'weekly':
                        time1 = datetime.fromtimestamp(int(date) / 1000) + relativedelta.relativedelta(weeks=1)
                    else:
                        time1 = datetime.fromtimestamp(int(date) / 1000) + relativedelta.relativedelta(years=1)
                    time1 = time1.strftime('%d-%m-%y %H:%M:%S')
                    final_json['time'] = time1
                if each['vendor'].capitalize() not in vendor_list:
                    vendor_list.append(each['vendor'].capitalize())
                table_json = dict()
                date = each['timestamp']
                table_json['date'] = datetime.fromtimestamp(int(date) / 1000).strftime('%d-%m-%y %H:%M:%S')
                table_json['status'] = each['status'].capitalize()
                table_json['vendor'] = each['vendor'].capitalize()
                if 'message' in each:
                    table_json['message'] = each['message']
                else:
                    table_json['message'] = ''
                table_data.append(table_json)
            if len(table_data) == 0:
                data = self.mongo_obj.read({'service_name': service_name},
                                           'monitoring_email', 'reports_collection')
                final_json = app_constants.Settings.email_status_json
                table_data = list()
                vendor_list = list()
                count = 0
                for each in data:
                    count = count + 1
                    if count == 1:
                        final_json['frequency'] = each['report_type']
                        date = each['timestamp']
                        if each['report_type'] == 'daily':
                            time1 = datetime.fromtimestamp(int(date) / 1000) + relativedelta.relativedelta(days=1)
                        elif each['report_type'] == 'quarterly':
                            time1 = datetime.fromtimestamp(int(date) / 1000) + relativedelta.relativedelta(months=6)
                        elif each['report_type'] == 'monthly':
                            time1 = datetime.fromtimestamp(int(date) / 1000) + relativedelta.relativedelta(months=1)
                        elif each['report_type'] == 'weekly':
                            time1 = datetime.fromtimestamp(int(date) / 1000) + relativedelta.relativedelta(weeks=1)
                        else:
                            time1 = datetime.fromtimestamp(int(date) / 1000) + relativedelta.relativedelta(years=1)
                        time1 = time1.strftime('%d-%m-%y %H:%M:%S')
                        final_json['time'] = time1
                    if each['vendor'].capitalize() not in vendor_list:
                        vendor_list.append(each['vendor'].capitalize())
            final_json[app_constants.Settings.KEY_TABLE_DATA][app_constants.Settings.KEY_BODY_CONTENT] = table_data
            vendors_string = ''
            for each in range(len(vendor_list)):
                if each == len(vendor_list) - 1:
                    vendors_string += vendor_list[each]
                    break
                vendors_string += vendor_list[each] + ', '
            final_json['vendor'] = vendors_string
            return final_json
        except Exception as e:
            log.error(str(e))
            raise Exception("Exception in Listing the Email Status")

    def status_upload_handler(self, input_json):
        try:
            print(input_json)

            self.mongo_obj.insert_one(input_json, 'monitoring_email', 'email_status')
            return 'added data'
        except Exception as e:
            log.error(str(e))
            raise Exception("Exception in Listing the Email Status")

    def report_setup_details(self, input_json):
        try:
            data = input_json.get('data')
            json_data = dict()
            find = self.mongo_obj.read({'service_name': data['reportName']}, 'monitoring_email', 'reports_collection')
            count = 0
            for each in find:
                print(each)
                count += 1
            if count > 0:
                raise Exception('Report service already added')
            json_data['service_name'] = data['reportName']
            json_data['report_type'] = data['frequency']
            json_data['vendor'] = data['vendor']
            json_data['to_be_monitored'] = data['toBeMonitored']
            json_data['timestamp'] = time.mktime(
                datetime.strptime(data['time'], "%d-%m-%Y %H:%M:%S").timetuple()) * 1000
            self.mongo_obj.insert_one(json_data, 'monitoring_email', 'reports_collection')
            return 'added data'
        except Exception as e:
            log.error(str(e))
            raise Exception("Same Report Service is already added")

import json
import traceback
import base64

from flask import request, Blueprint, make_response
from scripts.constants import app_constants
from scripts.handlers.reports_details_handler import MonitoringHandler
from scripts.logging.monitoring import logger as log


Monitoring = Blueprint("Monitoring_Services", __name__)


@Monitoring.route(app_constants.EndPoints.api_list_services, methods=[app_constants.POST])
def list_Services():
    if request.method == app_constants.POST:
        try:
            monitoring_obj = MonitoringHandler()
            content = request.get_data()
            data = monitoring_obj.list_report_services()
            resp_data = app_constants.result_success_template(data)
            return base64.b64encode((json.dumps(resp_data)).encode()), {'Content-Type': 'text/plain; charset=utf-8',
                                                                   'Server': "GLens",
                                                                   'X-Content-Type-Options': "nosniff",
                                                                   'Access-Control-Allow-Origin': '*'}
        except Exception as e:
            log.error(str(e))
            resp = app_constants.result_error_template(str(e))
            return base64.b64encode(json.dumps(resp).encode()), {'Content-Type': 'text/plain; charset=utf-8',
                                                                 'Server': "GLens", 'X-Content-Type-Options': "nosniff",
                                                                 'Access-Control-Allow-Origin': '*'}
    else:
        log.error(app_constants.method_not_supported)
        return base64.b64encode(json.dumps(app_constants.method_not_supported).encode()), {
            'Content-Type': 'text/plain; charset=utf-8',
            'Server': "GLens", 'X-Content-Type-Options': "nosniff",
            'Access-Control-Allow-Origin': '*'}


@Monitoring.route(app_constants.EndPoints.api_status_upload, methods=[app_constants.POST])
def status_upload_service():

    if request.method == app_constants.POST:
        try:
            monitoring_obj = MonitoringHandler()
            content = json.loads(request.get_data().decode('utf8').replace("'", '"'))
            res_data = monitoring_obj.status_upload_handler(content)
            data = app_constants.result_success_template(res_data)
            return base64.b64encode((json.dumps(data)).encode()), {'Content-Type': 'text/plain; charset=utf-8',
                                                                   'Server': "GLens",
                                                                   'X-Content-Type-Options': "nosniff",
                                                                   'Access-Control-Allow-Origin': '*'}
        except Exception as e:
            log.error(str(e))
            resp = app_constants.result_error_template(str(e))
            return base64.b64encode(json.dumps(resp).encode()), {'Content-Type': 'text/plain; charset=utf-8',
                                                                 'Server': "GLens", 'X-Content-Type-Options': "nosniff",
                                                                 'Access-Control-Allow-Origin': '*'}
    else:
        log.error(app_constants.method_not_supported)
        return base64.b64encode(json.dumps(app_constants.method_not_supported).encode()), {
            'Content-Type': 'text/plain; charset=utf-8',
            'Server': "GLens", 'X-Content-Type-Options': "nosniff",
            'Access-Control-Allow-Origin': '*'}

@Monitoring.route(app_constants.EndPoints.api_service_mail_status, methods=[app_constants.POST])
def Service_Mail_Status():

    if request.method == app_constants.POST:
        try:
            monitoring_obj = MonitoringHandler()
            content = json.loads(base64.b64decode(request.get_data()))
            res_data = monitoring_obj.service_email_details(content)
            data = app_constants.result_success_template(res_data)
            print(data)
            return base64.b64encode((json.dumps(data)).encode()), {'Content-Type': 'text/plain; charset=utf-8',
                                                                   'Server': "GLens",
                                                                   'X-Content-Type-Options': "nosniff",
                                                                   'Access-Control-Allow-Origin': '*'}
        except Exception as e:
            log.error(str(e))
            resp = app_constants.result_error_template(str(e))
            return base64.b64encode(json.dumps(resp).encode()), {'Content-Type': 'text/plain; charset=utf-8',
                                                                 'Server': "GLens", 'X-Content-Type-Options': "nosniff",
                                                                 'Access-Control-Allow-Origin': '*'}
    else:
        log.error(app_constants.method_not_supported)
        return base64.b64encode(json.dumps(app_constants.method_not_supported).encode()), {
            'Content-Type': 'text/plain; charset=utf-8',
            'Server': "GLens", 'X-Content-Type-Options': "nosniff",
            'Access-Control-Allow-Origin': '*'}


@Monitoring.route(app_constants.EndPoints.api_report_setup, methods=[app_constants.POST])
def service_report_setup():

    if request.method == app_constants.POST:
        try:
            monitoring_obj = MonitoringHandler()
            content = json.loads(base64.b64decode(request.get_data()))
            res_data = monitoring_obj.report_setup_details(content)
            data = app_constants.result_success_template(res_data, message='Successfully added the reports data')
            print(data)
            return base64.b64encode((json.dumps(data)).encode()), {'Content-Type': 'text/plain; charset=utf-8',
                                                                   'Server': "GLens",
                                                                   'X-Content-Type-Options': "nosniff",
                                                                   'Access-Control-Allow-Origin': '*'}
        except Exception as e:
            log.error(str(e))
            resp = app_constants.result_error_template(str(e))
            return base64.b64encode(json.dumps(resp).encode()), {'Content-Type': 'text/plain; charset=utf-8',
                                                                 'Server': "GLens", 'X-Content-Type-Options': "nosniff",
                                                                 'Access-Control-Allow-Origin': '*'}
    else:
        log.error(app_constants.method_not_supported)
        return base64.b64encode(json.dumps(app_constants.method_not_supported).encode()), {
            'Content-Type': 'text/plain; charset=utf-8',
            'Server': "GLens", 'X-Content-Type-Options': "nosniff",
            'Access-Control-Allow-Origin': '*'}
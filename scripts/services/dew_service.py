import json
import base64

from flask import request, Blueprint, make_response
from scripts.constants import app_constants
from scripts.handlers.dew_handler import DewHandler
from scripts.logging.monitoring import logger as log


dew_service_blue = Blueprint("Dew_Services", __name__)


@dew_service_blue.route(app_constants.EndPoints.api_show_data, methods=[app_constants.POST])
@dew_service_blue.route("/show_data", methods=[app_constants.POST])
def list_data():
    if request.method == app_constants.POST:
        try:
            monitoring_obj = DewHandler()
            content = request.get_data()
            data = monitoring_obj.show_sql_data()
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



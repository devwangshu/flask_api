from scripts.constants import app_configurations
from posixpath import join as urljoin

# Methods

GET = 'GET'
POST = 'POST'

# Error message constants

method_not_supported = 'Method not supported!'
access_token_not_validated = 'Access token is a not valid token'
success_status_code = 200
created_status_code = 201
internal_server_error_code = 500
bad_request_error_code = 400


class EndPoints(object):
    api_list_services = urljoin(app_configurations.api_base_service_url, "list_services")
    api_service_mail_status = urljoin(app_configurations.api_base_service_url, 'service_mail_statuses')
    api_status_upload = urljoin(app_configurations.api_base_service_url, 'status_upload')
    api_report_setup = urljoin(app_configurations.api_base_service_url, 'report_setup')

    # dew
    api_show_data = urljoin(app_configurations.api_base_service_url, "show_data")

class Settings:
    KEY_GLENS = 'glens'
    KEY_STATUS = 'status'
    KEY_FAILED = 'failed'
    KEY_SUCCESS = 'success'
    KEY_MESSAGE = 'message'
    KEY_DATA = 'data'
    EMPTY_MESSAGE = ''
    KEY_HEADER_CONTENT = 'header_content'
    KEY_BODY_CONTENT = 'body_content'
    KEY_TABLE_DATA = 'table_data'
    email_status_json = {
        "table_data": {
            "header_content": [
                {
                    "key": "date",
                    "label": "Date",
                    "type": "text"
                },
                {
                    "key": "status",
                    "label": "Status",
                    "type": "text"
                },
                {
                    "key": "vendor",
                    "label": "Vendor",
                    "type": "text"
                },
                {
                    "key": "message",
                    "label": "Message",
                    "type": "text"
                }
            ],
            "body_content": [

            ]
        }
    }


def result_success_template(data, message='Success', status=True):
    return {'status': status, 'message': message, 'data': data}


def result_error_template(message=None, error_type='application'):
    if message:
        return {
            'status': False,
            'type': error_type,
            'message': message,
            'data': None,
        }
    else:
        return {
            'status': False,
            'type': error_type,
            'message': 'Error while processing the request',
            'data': None,
        }

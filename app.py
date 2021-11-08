from flask import Flask, request, jsonify
from scripts.constants import app_configurations, app_constants
# from flask_cors import CORS
from scripts.services import reports_details_service,dew_service

app = Flask(__name__)
# cores = CORS(app, resource={r"/*": {"orgins": "*"}})

app.register_blueprint(reports_details_service.Monitoring)
app.register_blueprint(dew_service.dew_service_blue)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(app_configurations.PORT), debug=True, threaded=True, use_reloader=False)

from flask import Flask, request, jsonify
from datetime import datetime
from collections import OrderedDict
import json

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Check if required parameters are missing
    if not slack_name or not track:
        error_response = {
            "error": "Missing required parameters",
            "status_code": 400
        }
        return jsonify(error_response), 400, \
            {'Content-Type': 'application/json'}

    # Get the current day of the week
    current_day = datetime.now().strftime('%A')

    # Get the current UTC time
    current_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    github_repo_url = 'https://github.com/Efeoseaje/HNG_Task_1'
    github_file_url = \
        'https://github.com/Efeoseaje/HNG_Task_1/tree/master/blob/main/app.py'

    # Response data
    response_data = OrderedDict([
        ("slack_name", slack_name),
        ("current_day", current_day),
        ("utc_time", current_time),
        ("track", track),
        ("github_file_url", github_file_url),
        ("github_repo_url", github_repo_url),
        ("status_code", 200)
    ])

    # Serialize the ordered dictionary to JSON
    response_json = json.dumps(response_data, indent=2)

    return response_json, 200, {'Content-Type': 'application/json'}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

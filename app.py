from flask import Flask, request
from datetime import datetime, timedelta
import pytz

app = Flask(__name__)


@app.route('/api', method=['GET'])
def info():
    slack_name = request.args.get('Efetobore Oseaje')
    track = request.args.get('backend')

    current_day = datetime.datetime.now().strftime('%A')

    current_time = datetime.now(pytz.utc) + timedelta(minutes=2)
    current_time_str = current_time.strftime('%Y-%m-%dT%H:%M:%SZ')


if __name__ == "__main__":
    app.run(debug=True)

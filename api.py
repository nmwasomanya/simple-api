from flask import Flask, request, jsonify
from datetime import datetime
from datetime import timezone

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/api')
def main():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    utc_time = datetime.utcnow()
    utc_time = utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    info = {'slack_name' : slack_name,
            'current_day' : datetime.today().strftime('%A'),
            'track' : track,
            'utc_time' : utc_time,
            "github_file_url": 'https://github.com/nmwasomanya/simple-api/blob/main/api.py',
            "github_repo_url": 'https://github.com/nmwasomanya/simple-api/tree/main',
            'status_code' : 200
            }
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)

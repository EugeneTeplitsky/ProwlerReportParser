from flask import Flask, request, jsonify, send_file
import os
import json
from io import BytesIO

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_file():
    if not request.data:
        return jsonify({"error": "No file provided"}), 400
    data = request.data
    if data:
        parsed_data = parse_json(data)
        return send_parsed_file(parsed_data)
    return jsonify({"error": "File upload failed"}), 500


def parse_json(data):
    result = {}
    json_data = json.loads(data)
    for item in json_data:
        service = item['Service']
        check_id = item['Check ID'].split(' - ')[0]
        region = item['Region']
        arn = item['Check ID'].split(' - ')[1]

        if service not in result:
            result[service] = {}
        if check_id not in result[service]:
            result[service][check_id] = {}
        if region not in result[service][check_id]:
            result[service][check_id][region] = []
        result[service][check_id][region].append(arn)
    return result


def send_parsed_file(parsed_data):
    buffer = BytesIO()
    buffer.write(json.dumps(parsed_data, indent=4).encode('utf-8'))
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name='parsed_data.json', mimetype='application/json')


if __name__ == '__main__':
    app.run()

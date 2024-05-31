from flask import Flask, request, jsonify, send_file
import pandas as pd
import json
from io import BytesIO

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_file():
    if not request.data:
        return jsonify({"error": "No file part"}), 400
    file = request.data
    if file:
        try:
            df = pd.read_excel(file)
            parsed_data = parse_excel(df)
            return send_parsed_file(parsed_data)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify({"error": "File upload failed"}), 500


def parse_excel(df):
    result = {}
    fail_rows = df[df['Status'] == 'FAIL']
    for _, row in fail_rows.iterrows():
        service = row['Service']
        check_id = row['Check ID'].split(' - ')[0]
        region = row['Region']
        arn = row['Check ID'].split(' - ')[1]
        severity = row['Severity']

        if service not in result:
            result[service] = {}
        if check_id not in result[service]:
            result[service][check_id] = {"severity": severity, "regions": {}}
        if region not in result[service][check_id]["regions"]:
            result[service][check_id]["regions"][region] = []
        result[service][check_id]["regions"][region].append(arn)
    return result


def send_parsed_file(parsed_data):
    buffer = BytesIO()
    buffer.write(json.dumps(parsed_data, indent=4).encode('utf-8'))
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name='parsed_data.json', mimetype='application/json')


if __name__ == '__main__':
    app.run()

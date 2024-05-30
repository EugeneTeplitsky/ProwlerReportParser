# Prowler JSON Parser Microservice

This is a Python Flask microservice that parses JSON data from Prowler security audits (mainly tested on AWS tenancies). The service accepts a JSON file as a request parameter, parses it into a structured format, and returns the resulting JSON object as a downloadable file.

## Features

- Accepts a JSON file containing Prowler security advisories for various AWS services, check IDs, ARNs, and regions.
- Parses the input JSON data into a structured format based on the following hierarchy:
  1. AWS service
  2. Check ID
  3. Region
  4. Array of affected ARNs
- Returns the parsed JSON data as a downloadable file.

## Usage

1. Run the Flask application:

```bash
flask run --debug
```

2. Send a POST request to the `/upload` endpoint with the JSON file as the request body:

```bash
curl -X POST -H "Content-Type: application/json" --data-binary "@path/to/prowler_data.json" http://localhost:5000/upload
```

The service will parse the JSON data and return a downloadable file named `parsed_data.json` containing the structured data.

## Code Structure

- `app.py`: Contains the Flask application and the necessary routes and functions.
- `upload_file()`: The route handler for the `/upload` endpoint. It accepts the JSON file, validates the request, and calls the `parse_json` function.
- `parse_json(data)`: Parses the input JSON data according to the specified structure and returns the structured data.
- `send_parsed_file(parsed_data)`: Converts the parsed data into a JSON string, writes it to a `BytesIO` buffer, and sends it as a downloadable file.

## Security and Performance Considerations

- **Input Validation**: The service validates the presence of request data to prevent issues with malformed or missing data.
- **Error Handling**: Comprehensive error handling is implemented to manage different failure scenarios.
- **Performance**: The service is designed to handle large JSON files efficiently by parsing the data in memory and returning it as a downloadable file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
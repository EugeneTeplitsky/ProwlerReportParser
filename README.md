# Prowler JSON Parser Microservice

This is a Python Flask microservice that parses JSON data from Prowler security audits (mainly tested on AWS tenancies). The service accepts a JSON file as a request parameter, parses it into a structured format, and returns the resulting JSON object as a downloadable file.

## Features

- Accepts an Excel file containing Prowler security advisories with the following columns:
  - Check ID
  - Severity
  - Status
  - Region
  - Service
  - Provider
  - Account ID
- Filters rows with a "FAIL" status.
- Parses the input data into a structured JSON format based on the following hierarchy:
  1. AWS service
  2. Check ID
  3. Severity
  4. Regions
  5. Array of affected ARNs
- Returns the parsed JSON data as a downloadable file.

## Usage

1. Run the Flask application:

```bash
flask run --debug
```

2. Send a POST request to the /upload endpoint with the Excel file as the request body:

```bash
curl -X POST -F "file=@path/to/prowler_data.xlsx" http://localhost:5000/upload
```

The service will parse the Excel data and return a downloadable file named parsed_data.json containing the structured data.

## Code Structure

- `app.py`: Contains the Flask application and the necessary routes and functions.
- `upload_file()`: The route handler for the `/upload` endpoint. It accepts the Excel file, validates the request, and calls the `parse_excel` function.
- `parse_excel(df)`: Parses the input Excel data according to the specified structure and returns the structured data.
- `send_parsed_file(parsed_data)`: Converts the parsed data into a JSON string, writes it to a `BytesIO` buffer, and sends it as a downloadable file.

## Security and Performance Considerations

- **Input Validation**: The service validates the presence of the file in the request to prevent issues with malformed or missing data.
- **Error Handling**: Comprehensive error handling is implemented to manage different failure scenarios.
- **Performance**: The service is designed to handle large Excel files efficiently by parsing the data in memory and returning it as a downloadable file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
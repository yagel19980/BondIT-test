import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)


# Load the CSV and process it
def load_csv():
    df = pd.read_csv('flights.csv')
    df.columns = df.columns.str.strip()  # Strip extra spaces from column names
    return df


# POST to add flight data with new entries
@app.route('/flight', methods=['POST'])
def add_flight():
    df = load_csv()
    new_flights = request.json  # Expecting a JSON array of new flights

    required_fields = ['flight ID', 'Arrival', 'Departure']
    for flight in new_flights:
        if not all(field in flight for field in required_fields):
            return jsonify({'error': f'Missing fields in flight data: {flight}'}), 400

    # Convert JSON data into a DataFrame
    new_df = pd.DataFrame(new_flights)

    # Set the success column to empty string ''
    new_df['success'] = "''"

    # Append the new flights to the existing dataframe
    df = pd.concat([df, new_df], ignore_index=True)

    # Save the updated CSV
    df.to_csv('flights.csv', index=False)

    return jsonify({'message': 'Flights added successfully'}), 200


# GET flight info by flight ID
@app.route('/flight/<string:flight_id>', methods=['GET'])
def get_flight_info(flight_id):
    df = load_csv()
    flight_info = df[df['flight ID'] == flight_id].to_dict(orient='records')
    if flight_info:
        return jsonify(flight_info), 200
    else:
        return jsonify({'error': 'Flight not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)

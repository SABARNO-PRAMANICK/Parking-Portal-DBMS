from flask import Flask, render_template, request, jsonify
from connectivityportal import connect_to_database, insert_data, display_all_data, update_departure_time, search_by_plate_number, close_connection

app = Flask(__name__)

# Initialize database connection
connection = connect_to_database()

# Route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the insert request
@app.route('/insert', methods=['POST'])
def insert():
    data = request.json
    insert_data(connection, [(data['owner'], data['plate'], data['space'], None, None)])
    return jsonify({'message': 'Data inserted successfully'})

# Route to handle the display request
@app.route('/display')
def display():
    data = display_all_data(connection)
    return jsonify(data)

# Route to handle the update request
@app.route('/update', methods=['POST'])
def update():
    data = request.json
    update_departure_time(connection, data['departurePlate'])
    return jsonify({'message': 'Departure time updated successfully'})

# Route to handle the search request
@app.route('/search/<plate>')
def search(plate):
    data = search_by_plate_number(connection, plate)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

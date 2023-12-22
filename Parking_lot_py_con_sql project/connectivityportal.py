import mysql.connector

# Function to connect to the MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='sabarno@123',
            database='parkinginfo'
        )
        if connection.is_connected():
            print("Connected to the MySQL database")
            return connection
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None

# Function to insert data into the parkingspaces table
def insert_data(connection, data):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO parkingspaces (car_owner, plate_number, parking_space_id, time_of_arrival, time_of_departure) VALUES (%s, %s, %s, %s, %s)"
        cursor.executemany(query, data)
        connection.commit()
        print(f"{cursor.rowcount} record(s) inserted successfully")
    except mysql.connector.Error as e:
        print(f"Error: {e}")

# Function to update the time_of_departure for a specific plate number
def update_departure_time(connection, plate_number):
    try:
        cursor = connection.cursor()
        query = "UPDATE parkingspaces SET time_of_departure = NOW() WHERE plate_number = %s"
        cursor.execute(query, (plate_number,))
        connection.commit()
        print(f"Departure time updated for plate number {plate_number}")
    except mysql.connector.Error as e:
        print(f"Error: {e}")

# Function to search for a specific plate number and display the record
def search_by_plate_number(connection, plate_number):
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM parkingspaces WHERE plate_number = %s"
        cursor.execute(query, (plate_number,))
        row = cursor.fetchone()
        if row:
            print("Record found:")
            print(row)
        else:
            print(f"No record found for plate number {plate_number}")
    except mysql.connector.Error as e:
        print(f"Error: {e}")

# Function to display all data from the parkingspaces table
def display_all_data(connection):
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM parkingspaces"
        cursor.execute(query)
        rows = cursor.fetchall()
        print("Parking Spaces Data:")
        for row in rows:
            print(row)
    except mysql.connector.Error as e:
        print(f"Error: {e}")

# Function to close the database connection
def close_connection(connection):
    try:
        connection.close()
        print("Connection closed")
    except mysql.connector.Error as e:
        print(f"Error: {e}")

# Sample data for insertion
sample_data = [
    ('Jane Smith', 'XYZs789', 2, '2023-01-02 11:30:00', None),
    # ... add more data as needed
]

# Main execution
connection = connect_to_database()

if connection:
    insert_data(connection, sample_data)
    display_all_data(connection)

    # Update departure time for a specific plate number
    update_departure_time(connection, 'ABC123')

    # Search for a specific plate number
    search_by_plate_number(connection, 'XYZ789')

    close_connection(connection)


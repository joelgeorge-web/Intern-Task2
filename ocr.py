import mysql.connector
from butler import Client

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="db"
)

api_key = '???'
queue_id = '???'

file_location = "id1.jpg"

results = Client(api_key).extract_document(queue_id, file_location)

# Extract and print the value from 'ID NUMBER'
id_number = next((field.value for field in results.form_fields if field.field_name == 'ID NUMBER'), None)
if id_number:
    print(f"ID Number: {id_number}")

# Extract and print the value from 'Name'
name = next((field.value for field in results.form_fields if field.field_name == 'Name'), None)
if name:
    print(f"Name: {name}")

# Prepare the data for inserting into the database
data = {
    'name': name,
    'id': id_number  # Convert id_number to an integer
}

# Insert the data into the database
cursor = mydb.cursor()
sql = "INSERT INTO data (name, id) VALUES (%(name)s, %(id)s)"
cursor.execute(sql, data)
mydb.commit()
cursor.close()

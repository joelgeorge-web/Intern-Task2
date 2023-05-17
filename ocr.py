import mysql.connector
from butler import Client

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="db"
)

api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnb29nbGUtb2F1dGgyfDExNDk3ODIzODk3ODczMDU0NzM3MiIsImVtYWlsIjoiMjBjdDA5N0BtZ2l0cy5hYy5pbiIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpYXQiOjE2ODQzMDA0NjIzNzZ9.e9xetvl0i9tFVT1JOpRimSMptco5AdLKtKnOYW4Y-N4'
queue_id = '95f84c64-3d4a-4537-b6be-559da7a7240b'

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

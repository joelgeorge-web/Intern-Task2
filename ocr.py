# Make sure to first install the SDK using 'pip install butler-sdk'
from butler import Client

# Specify variables for use in script below
api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnb29nbGUtb2F1dGgyfDExNDk3ODIzODk3ODczMDU0NzM3MiIsImVtYWlsIjoiMjBjdDA5N0BtZ2l0cy5hYy5pbiIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpYXQiOjE2ODQzMDA0NjIzNzZ9.e9xetvl0i9tFVT1JOpRimSMptco5AdLKtKnOYW4Y-N4'
queue_id = '95f84c64-3d4a-4537-b6be-559da7a7240b'

# Specify the path to the file you would like to process
file_location = '/path/to/file'

response = Client(api_key).extract_document(queue_id, file_location)
print(response)
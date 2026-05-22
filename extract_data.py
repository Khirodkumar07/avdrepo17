# import pandas as pd

# print("Extract Data")

# # Sample data
# data = {
#     'Id': [101, 102, 103],
#     'Name': ['Ram', 'Raj', 'Raja'],
#     'Age': [29, 34, 42]
# }

# # Create DataFrame
# df = pd.DataFrame(data)

# # Display the DataFrame
# print(df)


#session-17 content

import requests
import pandas as pd

response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()

df = pd.DataFrame(data)
df = df[["id", "name", "email"]]

print(df)


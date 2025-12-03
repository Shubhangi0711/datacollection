import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"


response = requests.get(url)

data = response.json()

df = pd.DataFrame(data)

print(" API Data ")
print(df)


print("\n API Data Header ")
print(df.columns)

df.to_csv("api_users.csv", index=False)

print("\nData saved to api_users.csv successfully!")

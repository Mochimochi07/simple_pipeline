import requests
import pandas as pd

url = "https://pokeapi.co/api/v2/pokemon"
response = requests.get(url)
data = response.json()
print(data)

df = pd.DataFrame(data)
df.to_csv("pokemon.csv", index=False)

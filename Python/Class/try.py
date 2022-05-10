import requests
from sys import argv, exit 
import json

if argv[1] != 2:
    exit(1)

response = requests.get(
    f"https://itunes.apple.com/search?entity=song&limit=1&term={sys.argv[1]}")

o = response.json()

for result in o["results"]:
    print("Artist Name: ", result["artistName"])

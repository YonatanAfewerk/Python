import requests 
import sys 
import json

if len(sys.argv) != 2:
    sys.exit(1)
    

response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=1&term={sys.argv[1]}")

print(response.json())


 
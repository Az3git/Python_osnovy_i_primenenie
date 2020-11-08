import requests
import json
dicto = {}
headers = {"X-Xapp-Token" : 'eyJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6ImFydHN5Iiwic3ViamVjdF9hcHBsaWNhdGlvbiI6IjVkNDA5OTZlNmU2MDQ5MDAwNzQ5MGZhMiIsImV4cCI6MTYwNTM1OTAyMCwiaWF0IjoxNjA0NzU0MjIwLCJhdWQiOiI1ZDQwOTk2ZTZlNjA0OTAwMDc0OTBmYTIiLCJpc3MiOiJHcmF2aXR5IiwianRpIjoiNWZhNjliMmMwYTZiMjcwMDBkZWQyMmJhIn0.KRM6xcj0gMq5XZ7zW914dcYyuGmjqbj_dzK89ZQBSbA'}
with open('dataset_24476_4.txt') as f:
    for line in f:
        api_url = "https://api.artsy.net/api/artists/" + line
        api_url = api_url[0:-1]
        r = requests.get(api_url, headers=headers)
        
        j = json.loads(r.text)
        
        birthday = j['birthday']

        
        sortable_name = j['sortable_name']
        
        dicto.update({sortable_name : birthday})

ki = sorted(dicto.items(), key=lambda x: (x[1], x[0]))
for el in ki:
    try:
        int(el[0])
    except ValueError:
        print(el[0])
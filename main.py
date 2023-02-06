import requests
import json

# Replace <user_token> with your own Discogs API user token
headers = {
    "Authorization": "Discogs token=<user_token>",
    "User-Agent": "MyApp/1.0"
}

# Search for tracks with the specified query
query = "Shape of You Ed Sheeran"
response = requests.get(
    f"https://api.discogs.com/database/search?q={query}&type=track",
    headers=headers
)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    print(json.dumps(data, indent=4))
    # Get the first track in the list of results
    track = data["results"][0]
    # Get the track title
    track_title = track["title"]
    # Get the track's release title
    release_title = track["release_title"]
    print(f"Track: {track_title} from release {release_title}")
else:
    print("Search failed with status code", response.status_code)
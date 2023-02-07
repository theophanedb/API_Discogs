import discogs_client
import configparser

# Load the user token from the configuration file
config = configparser.ConfigParser()
config.read("./config.ini")
user_token = config["DEFAULT"]["user_token"]

# Create the interface to use the Discogs API
d = discogs_client.Client('Get-Genre-of-Tracks/1.0', user_token=user_token)

print("\nYou are identified as", d.identity())

results = d.search('passion phaxe', type='release')

n_pages = results.pages
page1 = results.page(1)

track = results[0]
properties = ['artists', 'artists_sort', 'changes', 'client', 'community', 
    'companies', 'country', 'credits', 'data', 'data_quality', 'delete', 
    'fetch', 'formats', 'genres', 'id', 'images', 'labels', 'marketplace_stats', 
    'master', 'notes', 'previous_request', 'price_suggestions', 'refresh', 'save', 
    'status', 'styles', 'thumb', 'title', 'tracklist', 'url', 'videos', 'year']

title = track.title
artists = track.artists
year = track.year
country = track.country
genres = track.genres
styles = track.styles
url_cover = track.images[0]["resource_url"]
labels = track.labels

print("\nHere is the result of your request on Discogs:\n", title, artists, year, country, genres, styles, url_cover, labels, sep="\n")

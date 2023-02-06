# https://github.com/joalla/discogs_client
# pip3 install python3-discogs-client
# https://python3-discogs-client.readthedocs.io/en/latest/authentication.html#user-token-authentication

import discogs_client

d = discogs_client.Client(
    'get-tracks-genres/1.0',
    consumer_key='CedjvXvMatXFkOOPzbij',
    consumer_secret='UJYOHeOtuoXcfLoxgZyvbsVaCCibwjkr'
)

request_token, request_secret, authorize_url = d.get_authorize_url()
print("\n", authorize_url)

# authorize_url must be opened to get the verifier code --> user accepts your app’s request to sign in on their behalf
print("\nClick on the above link and accept the request.")
access_granted = False
while not access_granted:
    verifier_code = input("Copy/Paste the code that was given to you: ")
    try:
        access_token, access_secret = d.get_access_token(verifier_code)
        access_granted = True
    except:
        print("The code is incorrect. Please try again.\n")

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

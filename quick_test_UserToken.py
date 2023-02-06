# https://github.com/joalla/discogs_client
# pip3 install python3-discogs-client
# https://python3-discogs-client.readthedocs.io/en/latest/authentication.html#user-token-authentication

import discogs_client

d = discogs_client.Client('get-tracks-genres/1.0', user_token="CGjeLVVheewKeQqLFoMtnXUNPXoIIfqJDxrObpTh")

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

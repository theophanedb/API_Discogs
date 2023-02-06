# pip3 install python3-discogs-client

import discogs_client

d = discogs_client.Client('get-tracks-genres/1.0', user_token="CGjeLVVheewKeQqLFoMtnXUNPXoIIfqJDxrObpTh")

print("\nYou are identified as", d.identity())

results = d.search('Stockholm By Night', type='release')
print(results)
print("\n")

print(results.pages)
print("\n")

artist = results[0].artists[0]
print(artist)
print("\n")

print(artist.name)

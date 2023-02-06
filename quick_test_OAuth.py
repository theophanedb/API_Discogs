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

results = d.search('Stockholm By Night', type='release')
print(results)
print("\n")

print(results.pages)
print("\n")

artist = results[0].artists[0]
print(artist)
print("\n")

print(artist.name)
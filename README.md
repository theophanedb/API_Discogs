# API_Discogs

**This repository presents 3 different ways of using the Discogs API to get information about music tracks.**

<a href="https://www.discogs.com">Discogs<a> is an online music database and a marketplace. 

It is one of the largest database for electronic music and it stores a lot of information for each track/album/artist/label.

## Python scripts
### *quick_test_OAuth.py* / *quick_test_UserToken.py*: these scripts use the **discogs_client** interface (python library) to interact with the API of Discogs

    pip3 install python3-discogs-client

For more information: 
- https://github.com/joalla/discogs_client
- https://python3-discogs-client.readthedocs.io/en/latest/authentication.html#user-token-authentication

### *requests_test.py*: this script uses the **requests** library to get information from the API
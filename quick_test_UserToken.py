import configparser
import discogs_client
import sys

def get_info(QUERIES, USER_TOKEN):

    # Create the interface to use the Discogs API
    d = discogs_client.Client('Get-Genre-of-Tracks/1.0', user_token=USER_TOKEN)

    print("\nYou are identified as", d.identity())

    infos = {}
    for QUERY in QUERIES:
        results = d.search(QUERY, type='release')

        n_pages = results.pages
        page1 = results.page(1)
        

        infos[QUERY] = None
        try: 
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
            infos[QUERY] = [title, artists, year, country, genres, styles, url_cover, labels]
        
        except: 
            print(f"\nWARNING: No track was found for the specified query: {QUERY}\n")

    return infos



if __name__ == '__main__':

    # Load the user token from the configuration file
    CONFIG = configparser.ConfigParser()
    CONFIG.read("./config.ini")
    USER_TOKEN = CONFIG["DEFAULT"]["user_token"]

    DEFAULT_QUERY = ["Passion - Phaxe"]
    QUERIES = []

    if len(sys.argv) == 1:      
        print(f"\nWARNING: No query was given. The default query '{DEFAULT_QUERY}' will be used.\n")
        QUERIES = DEFAULT_QUERY
    else:
        for i in range(1, len(sys.argv)):
            QUERIES.append(sys.argv[i])

    infos = get_info(QUERIES, USER_TOKEN)
    print("\n\n", infos)

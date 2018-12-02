import lyricsgenius as genius
api = genius.Genius("you must apply an api key for yourself here")

artist = api.search_artist("Bob Dylan")
api.save_artist_lyrics(artist)

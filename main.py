import grabber
import spotify_playlist

def playlist_top_100():
    urlPrefix = "https://hitparadeitalia.it/hp_yends/hpe"
    urlSuffix = ".htm"
    yearsRange = range(1947, 2023, 1)
    for year in yearsRange:
        playlist_name = 'Top Hits Italia ' + str(year)
        description = "La Top Hits italiana presa da https://hitparadeitalia.it/ !!! canzoni mancanti: "
        playlist_id = spotify_playlist.create_modify_playlist(user=spotify_playlist.get_user_id(),playlist_name=playlist_name,description=description)
        missing_songs = 0
        if playlist_id is not None:
            for index, song in enumerate(grabber.grab_songs(urlPrefix + str(year) + urlSuffix)):
                track_id = spotify_playlist.search_track(song['track'], song['artist'])
                if track_id is not None:
                    spotify_playlist.add_track_to_playlist(playlist_id=playlist_id, track_uri=[track_id])
                else:
                    missing_songs += 1
            description = description + str(missing_songs)
            spotify_playlist.create_modify_playlist(user=spotify_playlist.get_user_id(),playlist_name=playlist_name,description=description)

def main():
    playlist_top_100()

if __name__ == "__main__":
    main()
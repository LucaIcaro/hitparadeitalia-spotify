import grabber
import spotify_playlist

def playlist_top_100():
    urlPrefix = "https://hitparadeitalia.it/hp_yends/hpe"
    urlSuffix = ".htm"
    yearsRange = range(1947, 2010, 1)
    for year in yearsRange:
        print(year)
        playlist_name = 'Top Hits Italia ' + str(year)
        description = "La Top Hits italiana presa da https://hitparadeitalia.it/ !!! canzoni mancanti: "
        playlist_id = spotify_playlist.get_playlist_id(playlist_name=playlist_name)
        if playlist_id is None:
            playlist_id = spotify_playlist.create_modify_playlist(user=spotify_playlist.get_user_id(),playlist_name=playlist_name,description=description)
        missing_songs = 0
        song_list = []
        missing_song_names = []
        if playlist_id is not None:
            for index, song in enumerate(grabber.grab_songs(urlPrefix + str(year) + urlSuffix)):
                track_id = spotify_playlist.search_track(song['track'], song['artist'])
                if track_id is not None:
                    song_list.append(track_id)
                else:
                    missing_songs += 1
                    missing_song_names.append(song['track'] + " - " + song['artist'])
            spotify_playlist.add_track_to_playlist(playlist_id=playlist_id, track_uri=song_list)
            description = description + str(missing_songs)
            spotify_playlist.create_modify_playlist(user=spotify_playlist.get_user_id(),playlist_name=playlist_name,description=description)
            write_missing_songs(year, missing_song_names)

def clean_playlists():
    yearsRange = range(1947, 2023, 1)
    for year in yearsRange:
        print(year)
        playlist_name = 'Top Hits Italia ' + str(year)
        playlist_id = spotify_playlist.get_playlist_id(playlist_name=playlist_name)
        if playlist_id is not None:
            spotify_playlist.remove_songs_from_playlist(playlist_id=playlist_id)

def write_missing_songs(year, missing_song_names):
    f = open("missing_songs.txt", "a")
    f.write(str(year) + '\n')
    for item in missing_song_names:
        f.write(item + '\n')
    f.write("**************\n")
    f.close()

def main():
    playlist_top_100()
    # clean_playlists()

if __name__ == "__main__":
    main()
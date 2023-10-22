import grabber
import spotify_playlist

def main():
    urlPrefix = "https://hitparadeitalia.it/hp_yends/hpe"
    urlSuffix = ".htm"
    yearsRange = range(1947, 1948, 1)
    for year in yearsRange:
        # print("*************************")
        # print("YEAR ", year)
        # print(grabber.grab_songs(urlPrefix + str(year) + urlSuffix))
        playlist_id = spotify_playlist.create_modify_playlist(user=spotify_playlist.get_user_id(),playlist_name='luca test ' + str(year),description="something")
        if playlist_id is not None:
            for index, song in enumerate(grabber.grab_songs(urlPrefix + str(year) + urlSuffix)):
                track_id = spotify_playlist.search_track(song['track'], song['artist'])
                print(track_id)
                if track_id is not None:
                    spotify_playlist.add_track_to_playlist(playlist_id=playlist_id, track_uri=[track_id])
# todo:
# 1. spotify function that can add or edit tracks
# 2. loop in main to add them
# 3. if create_playlist == none, then skip


if __name__ == "__main__":
    main()
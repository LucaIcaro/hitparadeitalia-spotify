import grabber
import spotify_playlist

def main():
    urlPrefix = "https://hitparadeitalia.it/hp_yends/hpe"
    urlSuffix = ".htm"
    yearsRange = range(1947, 1948, 1)
    for year in yearsRange:
        print("*************************")
        print("YEAR ", year)
        print(grabber.grab_songs(urlPrefix + str(year) + urlSuffix))
        # spotify_playlist.create_modify_playlist(user=spotify_playlist.get_user_id(),playlist_name='luca test ' + year,description="something")

if __name__ == "__main__":
    main()
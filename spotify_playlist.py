import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

def see_album(birdy_uri):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    results = spotify.artist_albums(birdy_uri, album_type='album')
    
    albums = results['items']

    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    album_list = []
    for album in albums:
        album_list.append(album['name'])
    return album_list
        
# print(see_album('spotify:artist:2WX2uTcsvV5OnS0inACecP'))

def see_private_playlists():
    scope = 'playlist-read-private'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    results = sp.current_user_playlists(limit=50)
    private_playlists_list = []
    for item in results['items']:
        private_playlists_list.append(item['name'])
    return private_playlists_list

# scope = 'playlist-read-private,playlist-modify-public'
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
result = sp.search("track:no tengo dinero artist:righeira",limit=1,type="track")
print(result['tracks']['items'][0]['id'])
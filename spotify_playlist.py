import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

scope = 'user-read-private,user-read-email,playlist-read-private,playlist-modify-public,playlist-modify-private'

def see_album(uri):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    results = spotify.artist_albums(uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])
    album_list = []
    for album in albums:
        album_list.append(album['name'])
    return album_list

def see_private_playlists():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    results = sp.current_user_playlists(limit=50)
    private_playlists_list = []
    for item in results['items']:
        private_playlists_list.append(item['name'])
    return private_playlists_list

def get_playlist_id(playlist_name):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    results = sp.current_user_playlists(limit=50)
    for item in results['items']:
        if item['name'] == playlist_name:
            return item['id']
    return None

def check_playlist_exists(playlist_name, playlists_list):
    return (playlist_name in playlists_list)

def search_track(track, artist):
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    search_string = "track:" + track + " " + "artist:" + artist
    result = sp.search(search_string,limit=1,type="track")
    if result['tracks']['total'] != 0:
        return result['tracks']['items'][0]['uri']
    else:
        return None

def create_modify_playlist(user, playlist_name, is_public=None, description=None):
    # This function returns a json payload if the playlist is created
    # but returns None if it gets modified
    playlists_list = see_private_playlists()
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    if not check_playlist_exists(playlist_name, playlists_list):
        results = sp.user_playlist_create(user=user, name=playlist_name, public=is_public, description=description)
        return results['id']
    else:
        playlist_id = get_playlist_id(playlist_name)
        results = sp.user_playlist_change_details(user=user, playlist_id=playlist_id, public=is_public, description=description)
        return results

def get_user_id():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    results = sp.current_user()
    return results['id']

def add_track_to_playlist(playlist_id, track_uri, position=None):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    results = sp.playlist_add_items(playlist_id=playlist_id, items=track_uri, position=position)
    return results
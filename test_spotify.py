import unittest
from unittest.mock import Mock, patch
import spotify_playlist

class TestSeeAlbum(unittest.TestCase):
    @patch('spotify_playlist.SpotifyClientCredentials', Mock())
    @patch('spotify_playlist.spotipy.Spotify')
    def test_see_album(self, mock_spotify):
        # Create a mock Spotify instance
        mock_spotify_instance = mock_spotify.return_value

        # Define the expected API response
        api_response = {
            'items': [
                {'name': 'Album 1'},
                {'name': 'Album 2'},
            ],
            'next': None
        }

        # Set the return value of artist_albums to the expected response
        mock_spotify_instance.artist_albums.return_value = api_response

        # Call the function with a URI
        uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
        result = spotify_playlist.see_album(uri)

        # Assert that the SpotifyClientCredentials was created
        self.assertTrue(mock_spotify.called)

        # Assert that artist_albums was called with the provided URI and album_type
        mock_spotify_instance.artist_albums.assert_called_with(uri, album_type='album')

        # Assert that the function returns the expected album names
        self.assertEqual(result, ['Album 1', 'Album 2'])

    @patch('spotify_playlist.SpotifyOAuth', Mock())
    @patch('spotify_playlist.spotipy.Spotify')
    def test_see_playlists(self, mock_spotify):
        # Create a mock Spotify instance
        mock_spotify_instance = mock_spotify.return_value

        # Define the expected API response
        api_response = {
            'items': [
                {'name': 'Playlist 1'},
                {'name': 'Playlist 2'},
            ],
        }

        mock_spotify_instance.current_user_playlists.return_value = api_response

        result = spotify_playlist.see_private_playlists()

        # Assert that the SpotifyOAuth was created
        self.assertTrue(mock_spotify.called)

        # Assert that artist_albums was called with the provided URI and album_type
        mock_spotify_instance.current_user_playlists.assert_called_with(limit=50)

        # Assert that the function returns the expected album names
        self.assertEqual(result, ['Playlist 1', 'Playlist 2'])

    @patch('spotify_playlist.SpotifyOAuth', Mock())
    @patch('spotify_playlist.spotipy.Spotify')
    def test_get_playlist_id(self, mock_spotify):
        mock_spotify_instance = mock_spotify.return_value
        api_response = {
            'items': [
                {'name': 'Playlist 1', 'id': '12345'},
                {'name': 'Playlist 2', 'id': '67890'},
            ],
        }
        mock_spotify_instance.current_user_playlists.return_value = api_response
        result = spotify_playlist.see_private_playlists()
        self.assertTrue(mock_spotify.called)
        mock_spotify_instance.current_user_playlists.assert_called_with(limit=50)
        self.assertEqual(result, ['Playlist 1', 'Playlist 2'])

    @patch('spotify_playlist.SpotifyClientCredentials', Mock())
    @patch('spotify_playlist.spotipy.Spotify')
    def test_search(self, mock_spotify):
        # Create a mock Spotify instance
        mock_spotify_instance = mock_spotify.return_value

        # Define the expected API response
        api_response = {'tracks':
            {'items':
                 [{
                   'id': 'ABCDEF12345',
                }], }}

        mock_spotify_instance.search.return_value = api_response
        result = spotify_playlist.search_track("track1","artist1")
        mock_spotify_instance.search.assert_called_with("track:track1 artist:artist1",limit=1,type="track")
        self.assertEqual(result, 'ABCDEF12345')


if __name__ == '__main__':
    unittest.main()

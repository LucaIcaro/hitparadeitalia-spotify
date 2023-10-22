import requests
from bs4 import BeautifulSoup
import re

def grab_songs(url):

    response = requests.get(url)
    # fix encoding problems for italian accents
    response.encoding = response.apparent_encoding
    song_list = []
    pattern = r'\([^)]*\)'

    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all the <li> elements with the specified class
        target_elements = soup.find_all('li', class_='p-2 fs-3')
        for element in target_elements:
            # this will return only one element with all the songs
            elements_list = element.get_text()
    else:
        print(f"Failed to retrieve the URL. Status code: {response.status_code}")
    for str in elements_list.split("\n"):
        if len(str.strip()) > 0:
            track_artist = clean_string(str).rsplit(' - ', 1)
            # Remove content within parentheses using regex
            track = re.sub(pattern, '', track_artist[0]).strip()
            artist = re.sub(pattern, '', track_artist[1]).strip()
            track_artist_dict = {'track': track, 'artist': artist}
            song_list.append(track_artist_dict)
    return song_list

def clean_string(str):
    cleaned_string = re.sub(r'\[[^]]*\]', '', str)
    return cleaned_string.strip()

if __name__ == "__main__":
    print("This is just a module")

import requests
from bs4 import BeautifulSoup
import re

def grab_songs(url):
    
    response = requests.get(url)
    # fix encoding problems for italian accents
    response.encoding = response.apparent_encoding
    song_list = []
        
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
        song_list.append(clean_string(str))
    return song_list

def clean_string(str):
    cleaned_string = re.sub(r'\[[^]]*\]', '', str)
    return cleaned_string.strip()

from bs4 import BeautifulSoup

def get_anime_from_file(file):
    animeNames = []
    site = open(file, 'r').read()
    soup = BeautifulSoup(site)
    animeLines = soup.find_all(class_="animetitle")
    for anime in animeLines:
        animeNames.append(anime.find("span").text)
    return animeNames

import requests


url_licence = 'https://raw.githubusercontent.com/manti-by/lessons/master/LICENSE'


def save_licence(url, filename):
    with open(filename, 'wb') as file:
        ufr = requests.get(url)
        file.write(ufr.content)


save_licence(url_licence, 'LICENCE')

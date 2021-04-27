import requests
from bs4 import BeautifulSoup


def find_urls():
    html = requests.get('https://en.wikipedia.org/wiki/Time%27s_List_of_the_100_Best_Novels')
    soup = BeautifulSoup(html.text, 'html.parser')

    items = soup.find('div', id='mw-content-text').find('div', class_='mw-parser-output').find('table',style='text-align:left').find_all('i')[:55]

    urls_list = {}
    for item in items:
        urls_list[item.text] = f"https://en.wikipedia.org/{item.find('a').get('href')}"

    urls_list.pop('A Dance to the Music of Time')
    urls_list.pop('The Death of the Heart')
    urls_list.pop('Light in August')
    urls_list.pop('Lord of the Flies')
    urls_list.pop('Loving')
    urls_list.pop('American Pastoral')

    return urls_list


def books_list(urls_list: list):
    books_list = []
    for title, url in urls_list.items():
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')

        items = soup.find('div', class_='mw-parser-output').find('table', class_='infobox vcard').find('tbody')

        lab_name = items.find_all('th', class_='infobox-label')
        lab_text = items.find_all('td', class_='infobox-data')

        characs = {}

        for key, value in zip(lab_name, lab_text):
            characs[key.text] = value.text

        fin_dict = {
            'Title': title,
            'Author': characs['Author'],
            'Language': characs['Language'],
            'Country': characs['Country'],
            # 'Pages': characs['Pages']
        }
        books_list.append(fin_dict)

    return books_list


books_list = books_list(find_urls())

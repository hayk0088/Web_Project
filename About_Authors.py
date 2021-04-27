import requests
from bs4 import BeautifulSoup

def find_urls():

    html = requests.get('https://en.wikipedia.org/wiki/Time%27s_List_of_the_100_Best_Novels')
    soup = BeautifulSoup(html.text, 'html.parser')

    items = soup.find('div', id='mw-content-text').find('div', class_='mw-parser-output').find('table',style='text-align:left').find_all('a')[1:114:2]

    urls_list = {}
    a = items
    for item in items:
        urls_list[item.text] = f"https://en.wikipedia.org{item.get('href')}"

    urls_list.pop('George Orwell')
    urls_list.pop('James Agee')
    urls_list.pop('John Steinbeck')
    urls_list.pop('Vladimir Nabokov')
    return urls_list


def authors_list(urls_list: list):

    authors_list = []
    for name, url in urls_list.items():
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')

        items = soup.find('div', id='mw-content-text').find('div', class_='mw-parser-output')

        aut_name = items.find_all('th', class_='infobox-label')
        aut_text = items.find_all('td', class_='infobox-data')


        characs = {}
#
        for key, value in zip(aut_name, aut_text):
            print(name, value.find('span', class_='bday').text)
            characs[key.text] = value.find('span', class_='bday').text
            break

        about_dict = {
            'Name': name,
            'Born': characs['Born'],

            #'Nationality': characs['Nationality'],
        }
        authors_list.append(about_dict)


    return authors_list

authors_list = authors_list(find_urls())

print(authors_list)

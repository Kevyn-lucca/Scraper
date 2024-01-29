import requests
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'

def obter_conteudo(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    elementos_card_content = soup.find_all(class_='card-content')

    for card_content in elementos_card_content:

        elementos_h2 = card_content.find_all('h2')
        elementos_location = card_content.find_all(class_='location')
        elementos_a= card_content.find_all('a')

        print('-' * 90)

        for h2 in elementos_h2:
            print(f"Nome da vaga:  {h2.text.strip()}")
            
        for location in elementos_location:
            print(f"Local da vaga: {location.text.strip()}")

        for a in elementos_a:
            print(f"Url da pagina: {a['href']}")    

obter_conteudo(url)
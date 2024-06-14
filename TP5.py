import requests
from bs4 import BeautifulSoup

url = "https://www.turismo.gov.br/agenda-eventos/views/calendario.php"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

# class="new-card-content" = card com as informações dos eventos
# class="categoria" = categoria do evento
# class="dia" = dia do inicio do evento
# class="mes" = mes do inicio do evento
# class="nome" = nome do evento
# class="localizacao " = localização do evento
# class="status" = status do evento

events = soup.find_all("div", class_="new-card-content")

for event in events:
    categoria = event.find("div", class_="categoria")
    dia = event.find("span", class_="dia")
    mes = event.find("span", class_="mes")
    nome = event.find("span", class_="nome")
    localizacao = event.find("span", class_="localizacao")
    status = event.find("span", class_="status")
    
    print(categoria.text.strip())
    print(dia.text.strip())
    print(mes.text.strip())
    print(nome.text.strip())
    print(localizacao.text.strip())
    print(status.text.strip())
    print('\n\n')
    

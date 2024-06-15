import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

conexao = sqlite3.connect('dbEventos.db') # Criando banco de dados
cursor = conexao.cursor() 

# Criando tabelas

cursor.execute('''
               CREATE TABLE Eventos (
                   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   Nome VARCHAR(150) NOT NULL,
                   Tipo VARCHAR(150) NOT NULL
               );
''')
cursor.execute('''
              CREATE TABLE Dados_Evento (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    ID_evento INT,
                    Data DATE NOT NULL,
                    Localizacao VARCHAR(255) NOT NULL,
                    FOREIGN KEY (ID_evento) REFERENCES Eventos(ID)
                );

''')
cursor.execute('''
                CREATE TABLE Metadados (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    ID_evento INT,
                    Metadado VARCHAR(255) NOT NULL,
                    FOREIGN KEY (ID_evento) REFERENCES Eventos(ID)
                );
''')


# Puxando dados da página Web (Web Scraping e Web Crawling)

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
    categoria = event.find("div", class_="categoria").text.strip()
    dia = event.find("span", class_="dia").text.strip()
    mes = event.find("span", class_="mes").text.strip()
    nome = event.find("span", class_="nome").text.strip()
    localizacao = event.find("span", class_="localizacao").text.strip()
    status = event.find("span", class_="status").text.strip()
    
    if 'RJ' in localizacao:
        data = datetime.strptime(f"{dia} {mes} 2024", "%d %b %Y")  
        data_formatada = data.strftime("%Y-%m-%d")
        cursor.execute("INSERT INTO Eventos (Nome,Tipo) VALUES(?,?)", (nome,categoria))
        evento_id = cursor.lastrowid
        cursor.execute("INSERT INTO Dados_Evento (ID_evento,Data,Localizacao) VALUES(?,?,?)", (evento_id,data_formatada,localizacao))
        cursor.execute("INSERT INTO Metadados (ID_evento,Metadado) VALUES(?,?)", (evento_id,status))
        conexao.commit()




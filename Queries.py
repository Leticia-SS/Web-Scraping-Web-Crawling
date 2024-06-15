import sqlite3

conexao = sqlite3.connect('dbEventos.db') # Criando banco de dados
cursor = conexao.cursor() 

cursor.execute('SELECT * FROM Dados_Evento')
resultado = cursor.fetchall()  
print(resultado)
import sqlite3

conexao = sqlite3.connect('dbEventos.db') # Criando banco de dados
cursor = conexao.cursor() 


query_1 = '''
    SELECT e.Nome, de.Data, de.Localizacao, e.Tipo
    FROM Eventos e
    JOIN Dados_Evento de ON e.ID = de.ID_evento;
'''

cursor.execute(query_1)
resultado1 = cursor.fetchall()  
print(resultado1)

query_2 = '''
    SELECT e.Nome, de.Data, de.Localizacao, e.Tipo
    FROM Eventos e
    JOIN Dados_Evento de ON e.ID = de.ID_evento
    WHERE de.Data >= DATE('now')
    ORDER BY de.Data ASC
    LIMIT 2;
'''

cursor.execute(query_2)
resultado2 = cursor.fetchall()  
print(resultado2)


query_3 = '''
SELECT e.Nome, de.Data, de.Localizacao, e.Tipo
FROM Eventos e
JOIN Dados_Evento de ON e.ID = de.ID_evento
WHERE de.Localizacao LIKE '%Búzios/RJ%';
'''

cursor.execute(query_3)
resultado3 = cursor.fetchall()  
print(resultado3)


query_4 = '''
SELECT e.Nome, de.Data, de.Localizacao, e.Tipo
FROM Eventos e
JOIN Dados_Evento de ON e.ID = de.ID_evento
JOIN Metadados m ON e.ID = m.ID_evento
WHERE m.Metadado = 'Acontecendo';
'''

cursor.execute(query_4)
resultado4 = cursor.fetchall()  
print(resultado4)

query_5 = '''
SELECT e.Nome, m.Metadado
FROM Eventos e
JOIN Metadados m ON e.ID = m.ID_evento;
'''

cursor.execute(query_5)
resultado5 = cursor.fetchall()  
print(resultado5)
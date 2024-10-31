import psycopg2

conexao = psycopg2.connect(
    dbname = "db_teste",
    user = "ptgs",
    password = "admin"
    host = "localhost",
    port = "5432"
)

cursor = conexao.cursor()

cursor.execute("Select * from clientes")
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)

cursor.close()
conexao.close()
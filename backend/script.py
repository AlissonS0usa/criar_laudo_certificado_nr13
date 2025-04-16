import psycopg2

# Altere com suas credenciais
conn = psycopg2.connect(
    host="sistema-nr13-db.cjia2cqyygb1.us-east-2.rds.amazonaws.com",
    port="5432",
    user="postgres",
    password="segredo123",
    dbname="postgres"  # pode ser qualquer um existente
)

conn.autocommit = True
cur = conn.cursor()
cur.execute("CREATE DATABASE nr13;")
print("Banco de dados 'nr13' criado com sucesso.")
cur.close()
conn.close()


import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="*******",
    database="crudpython",
)

cursor = conexao.cursor()

# CRUD
nome_produto = "toddynho"
valor = 6
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)  # EXECUTA o comando SQL
conexao.commit()



cursor.close()
conexao.close()


#CREATE
# nome_produto = "toddynho"
# valor = 10
# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
# cursor.execute(comando)  # EXECUTA o comando SQL
# conexao.commit()

#READ
# nome_produto = "toddynho"
# valor = 10
# comando = f'SELECT * FROM vendas'
# cursor.execute(comando)  # EXECUTA o comando SQL
# resultado = cursor.fetchall()  # LÊ os dados
# print(resultado)

#UPDATE
# nome_produto = "toddynho"
# valor = 6
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)  # EXECUTA o comando SQL
# conexao.commit()

# DELETE
# nome_produto = "toddynho"
# valor = 6
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)  # EXECUTA o comando SQL

# conexao.commit()

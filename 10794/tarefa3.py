import mysql.connector

def ligacao_bd():
    try:
        ligacao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="JsSribeiro14",
            database="works"
        )
        print("Ligação estabelecida com sucesso!")
        return ligacao
    except mysql.connector.Error as erro:
        print(f"Erro ao ligar à BD: {erro}")
        return None

def verificar_tabela(cursor, nome_tabela):
    cursor.execute(f"SHOW TABLES LIKE '{nome_tabela}'")
    return cursor.fetchone()

def criar_tabela(cursor, ligacao):
    nome_tabela = input("Nome da tabela: ")

    if verificar_tabela(cursor, nome_tabela):
        print("Tabela já existe!")
        return

    num_campos = int(input("Número de campos: "))
    campos = []

    for i in range(num_campos):
        nome = input(f"Nome do campo {i+1}: ")
        tipo = input(f"Tipo do campo {i+1} (INT, VARCHAR(255), ...): ")
        campos.append(f"{nome} {tipo}")

    sql = f"CREATE TABLE {nome_tabela} (id INT AUTO_INCREMENT PRIMARY KEY, {', '.join(campos)})"
    cursor.execute(sql)

    ligacao.commit()
    print("Tabela criada com sucesso!")

def adicionar_dados(cursor, ligacao):
    nome_tabela = input("Tabela onde inserir dados: ")

    if not verificar_tabela(cursor, nome_tabela):
        print("Tabela não existe!")
        return

    cursor.execute(f"DESCRIBE {nome_tabela}")
    colunas = cursor.fetchall()[1:]  # ignora o id

    valores = []
    for coluna in colunas:
        valor = input(f"{coluna[0]} ({coluna[1]}): ")
        valores.append(valor)

    placeholders = ", ".join(["%s"] * len(colunas))
    nomes_colunas = ", ".join([col[0] for col in colunas])

    sql = f"INSERT INTO {nome_tabela} ({nomes_colunas}) VALUES ({placeholders})"
    cursor.execute(sql, tuple(valores))

    ligacao.commit()
    print("Dados inseridos!")

def consultar_dados(cursor):
    nome_tabela = input("Tabela a consultar: ")

    if not verificar_tabela(cursor, nome_tabela):
        print("Tabela não existe!")
        return

    cursor.execute(f"SELECT * FROM {nome_tabela}")
    resultados = cursor.fetchall()

    print("\n--- DADOS ---")
    for r in resultados:
        print(r)

def eliminar_dados(cursor, ligacao):
    nome_tabela = input("Tabela: ")

    if not verificar_tabela(cursor, nome_tabela):
        print("Tabela não existe!")
        return

    cursor.execute(f"SELECT * FROM {nome_tabela}")
    for r in cursor.fetchall():
        print(r)

    try:
        id = int(input("ID a eliminar: "))
    except ValueError:
        print("ID inválido!")
        return

    cursor.execute(f"DELETE FROM {nome_tabela} WHERE id = %s", (id,))
    ligacao.commit()
    print("Registo eliminado!")

def menu():
    ligacao = ligacao_bd()

    if ligacao:
        cursor = ligacao.cursor()

        while True:
            print("\n--- MENU ---")
            print("1 - Criar tabela")
            print("2 - Inserir dados")
            print("3 - Consultar dados")
            print("4 - Eliminar dados")
            print("5 - Sair")

            op = input("Opção: ")

            if op == "1":
                criar_tabela(cursor, ligacao)
            elif op == "2":
                adicionar_dados(cursor, ligacao)
            elif op == "3":
                consultar_dados(cursor)
            elif op == "4":
                eliminar_dados(cursor, ligacao)
            elif op == "5":
                print("Fim do programa.")
                break
            else:
                print("Opção inválida!")

        cursor.close()
        ligacao.close()
    else:
        print("Erro na ligação!")


menu()
import mysql.connector
import csv

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
        tipo = input(f"Tipo do campo {i+1}: ")
        campos.append(f"{nome} {tipo}")

    cursor.execute(f"CREATE TABLE {nome_tabela} (id INT AUTO_INCREMENT PRIMARY KEY, {', '.join(campos)})")
    ligacao.commit()
    print("Tabela criada!")


def adicionar_dados(cursor, ligacao):
    nome_tabela = input("Tabela: ")

    if not verificar_tabela(cursor, nome_tabela):
        print("Tabela não existe!")
        return

    cursor.execute(f"DESCRIBE {nome_tabela}")
    colunas = cursor.fetchall()[1:]

    valores = []
    for col in colunas:
        valores.append(input(f"{col[0]} ({col[1]}): "))

    placeholders = ", ".join(["%s"] * len(colunas))
    nomes = ", ".join([c[0] for c in colunas])

    cursor.execute(f"INSERT INTO {nome_tabela} ({nomes}) VALUES ({placeholders})", tuple(valores))
    ligacao.commit()
    print("Dados inseridos!")


def consultar_dados(cursor):
    nome_tabela = input("Tabela: ")

    if not verificar_tabela(cursor, nome_tabela):
        print("Tabela não existe!")
        return

    cursor.execute(f"SELECT * FROM {nome_tabela}")
    for r in cursor.fetchall():
        print(r)


def eliminar_dados(cursor, ligacao):
    nome_tabela = input("Tabela: ")

    if not verificar_tabela(cursor, nome_tabela):
        print("Tabela não existe!")
        return

    consultar_dados(cursor)

    try:
        id = int(input("ID a eliminar: "))
    except ValueError:
        print("ID inválido!")
        return

    cursor.execute(f"DELETE FROM {nome_tabela} WHERE id = %s", (id,))
    ligacao.commit()
    print("Eliminado!")

def alterar_dados(cursor, ligacao):
    nome_tabela = input("Tabela: ")

    if not verificar_tabela(cursor, nome_tabela):
        print("Tabela não existe!")
        return

    consultar_dados(cursor)

    cursor.execute(f"DESCRIBE {nome_tabela}")
    colunas = [c[0] for c in cursor.fetchall()]

    try:
        id = int(input("ID a alterar: "))
    except ValueError:
        print("ID inválido!")
        return

    print("Colunas:")
    for i, col in enumerate(colunas):
        print(f"{i+1} - {col}")

    try:
        idx = int(input("Escolha coluna: ")) - 1
    except ValueError:
        print("Inválido!")
        return

    if 0 <= idx < len(colunas):
        novo = input("Novo valor: ")
        cursor.execute(f"UPDATE {nome_tabela} SET {colunas[idx]} = %s WHERE id = %s", (novo, id))
        ligacao.commit()
        print("Atualizado!")
    else:
        print("Coluna inválida!")

def listar_tabelas(cursor):
    cursor.execute("SHOW TABLES")
    tabelas = cursor.fetchall()

    if tabelas:
        print("\nTabelas:")
        for t in tabelas:
            print(t[0])
    else:
        print("Sem tabelas!")

def filtrar_dados(cursor):
    nome_tabela = input("Tabela: ")

    if not verificar_tabela(cursor, nome_tabela):
        print("Tabela não existe!")
        return

    cursor.execute(f"DESCRIBE {nome_tabela}")
    colunas = [c[0] for c in cursor.fetchall()]

    print("Colunas:")
    for i, col in enumerate(colunas):
        print(f"{i+1} - {col}")

    criterio = input("Critério (ex: idade = 20): ")

    cursor.execute(f"SELECT * FROM {nome_tabela} WHERE {criterio}")
    resultados = cursor.fetchall()

    if resultados:
        for r in resultados:
            print(r)
    else:
        print("Sem resultados!")

def exportar_csv(cursor):
    nome_tabela = input("Tabela a exportar: ")

    if not verificar_tabela(cursor, nome_tabela):
        print("Tabela não existe!")
        return

    cursor.execute(f"SELECT * FROM {nome_tabela}")
    dados = cursor.fetchall()
    colunas = [desc[0] for desc in cursor.description]

    with open(f"{nome_tabela}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(colunas)
        writer.writerows(dados)

    print("Exportado com sucesso!")

def importar_csv(cursor, ligacao):
    nome_tabela = input("Tabela: ")

    if not verificar_tabela(cursor, nome_tabela):
        print("Tabela não existe!")
        return

    ficheiro = input("Nome do ficheiro CSV: ")

    try:
        with open(ficheiro, "r") as f:
            reader = csv.reader(f)
            colunas = next(reader)

            placeholders = ", ".join(["%s"] * len(colunas))
            sql = f"INSERT INTO {nome_tabela} ({', '.join(colunas)}) VALUES ({placeholders})"

            for linha in reader:
                cursor.execute(sql, tuple(linha))

        ligacao.commit()
        print("Importado com sucesso!")

    except FileNotFoundError:
        print("Ficheiro não encontrado!")

def menu():
    ligacao = ligacao_bd()

    if ligacao:
        cursor = ligacao.cursor()

        while True:
            print("\n--- MENU ---")
            print("1 Criar tabela")
            print("2 Inserir dados")
            print("3 Consultar dados")
            print("4 Eliminar dados")
            print("5 Alterar dados")
            print("6 Listar tabelas")
            print("7 Filtrar dados")
            print("8 Exportar CSV")
            print("9 Importar CSV")
            print("0 Sair")

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
                alterar_dados(cursor, ligacao)
            elif op == "6":
                listar_tabelas(cursor)
            elif op == "7":
                filtrar_dados(cursor)
            elif op == "8":
                exportar_csv(cursor)
            elif op == "9":
                importar_csv(cursor, ligacao)
            elif op == "0":
                print("Fim.")
                break
            else:
                print("Opção inválida!")

        cursor.close()
        ligacao.close()


menu()
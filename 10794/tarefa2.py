import mysql.connector

def ligacao_bd():
    try:
        ligacao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="JsSribeiro14",
            database="works"
        )
        return ligacao
    except mysql.connector.Error as erro:
        print(f"Erro ao ligar à BD: {erro}")
        return None

def criar_tabela(cursor):
    instrucao = """
    CREATE TABLE IF NOT EXISTS utilizadores(
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255),
        idade INT
    )
    """
    cursor.execute(instrucao)
    print("Tabela criada/verificada com sucesso!")

def inserir_dados_iniciais(cursor):
    cursor.execute("SELECT COUNT(*) FROM utilizadores")
    total = cursor.fetchone()[0]

    if total == 0:
        dados = [
            ("Nome1", 24),
            ("Nome2", 15),
            ("Nome3", 36),
            ("Nome4", 18)
        ]

        instrucao = "INSERT INTO utilizadores (nome, idade) VALUES (%s, %s)"
        cursor.executemany(instrucao, dados)

        print("Dados iniciais inseridos!")
    else:
        print("A tabela já contém dados!")

def adicionar_utilizador(cursor, ligacao):
    try:
        nome = input("Nome: ")
        idade = int(input("Idade: "))

        instrucao = "INSERT INTO utilizadores (nome, idade) VALUES (%s, %s)"
        cursor.execute(instrucao, (nome, idade))

        ligacao.commit()
        print("Utilizador adicionado!")
    except ValueError:
        print("Erro! Idade inválida.")

def consultar_utilizadores(cursor):
    cursor.execute("SELECT * FROM utilizadores")
    resultados = cursor.fetchall()

    print("\n--- UTILIZADORES ---")
    for r in resultados:
        print(r)

def eliminar_utilizador(cursor, ligacao):
    consultar_utilizadores(cursor)
    try:
        id = int(input("ID a eliminar: "))

        cursor.execute("SELECT * FROM utilizadores WHERE id = %s", (id,))
        if cursor.fetchone():
            cursor.execute("DELETE FROM utilizadores WHERE id = %s", (id,))
            ligacao.commit()
            print("Utilizador eliminado!")
        else:
            print("ID não encontrado!")
    except ValueError:
        print("ID inválido!")

def menu():
    ligacao = ligacao_bd()
    print("Teste")
    if ligacao:
        cursor = ligacao.cursor()

        criar_tabela(cursor)
        inserir_dados_iniciais(cursor)
        ligacao.commit()

        while True:
            print("\n--- MENU ---")
            print("1 - Adicionar utilizador")
            print("2 - Consultar utilizadores")
            print("3 - Eliminar utilizador")
            print("4 - Sair")

            opcao = input("Escolha: ")

            if opcao == "1":
                adicionar_utilizador(cursor, ligacao)
            elif opcao == "2":
                consultar_utilizadores(cursor)
            elif opcao == "3":
                eliminar_utilizador(cursor, ligacao)
            elif opcao == "4":
                print("Programa terminado.")
                break
            else:
                print("Opção inválida!")

        cursor.close()
        ligacao.close()
    else:
        print("Não foi possível ligar à BD.")


menu()
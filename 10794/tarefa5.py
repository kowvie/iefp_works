import asyncio
import aiomysql
import csv
import os
from datetime import datetime

BD = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "JsSribeiro14",
    "db": "works",
    "minsize": 1,
    "maxsize": 5,
    "autocommit": True
}

pool = None

async def verificar_tabela(conn, nome_tabela):
    async with conn.cursor() as cursor:
        await cursor.execute("SHOW TABLES LIKE %s", (nome_tabela,))
        return await cursor.fetchone()

async def criar_tabela():
    async with pool.acquire() as conn:
        nome_tabela = input("Nome da tabela: ")

        if await verificar_tabela(conn, nome_tabela):
            print("Tabela já existe!")
            return

        num = int(input("Número de campos: "))
        campos = []

        for i in range(num):
            nome = input(f"Campo {i+1}: ")
            tipo = input("Tipo: ")
            campos.append(f"{nome} {tipo}")

        async with conn.cursor() as cursor:
            await cursor.execute(
                f"CREATE TABLE {nome_tabela} (id INT AUTO_INCREMENT PRIMARY KEY, {', '.join(campos)})"
            )

        print("Tabela criada!")

async def adicionar_dados():
    async with pool.acquire() as conn:
        nome_tabela = input("Tabela: ")

        if not await verificar_tabela(conn, nome_tabela):
            print("Tabela não existe!")
            return

        async with conn.cursor() as cursor:
            await cursor.execute(f"DESCRIBE {nome_tabela}")
            colunas = (await cursor.fetchall())[1:]

            valores = []
            for col in colunas:
                valores.append(input(f"{col[0]} ({col[1]}): "))

            placeholders = ", ".join(["%s"] * len(colunas))
            nomes = ", ".join([c[0] for c in colunas])

            await cursor.execute(
                f"INSERT INTO {nome_tabela} ({nomes}) VALUES ({placeholders})",
                tuple(valores)
            )

        print("Dados inseridos!")

async def consultar_dados():
    async with pool.acquire() as conn:
        nome_tabela = input("Tabela: ")

        if not await verificar_tabela(conn, nome_tabela):
            print("Tabela não existe!")
            return

        async with conn.cursor() as cursor:
            await cursor.execute(f"SELECT * FROM {nome_tabela}")
            resultados = await cursor.fetchall()

            for r in resultados:
                print(r)

async def eliminar_dados():
    async with pool.acquire() as conn:
        nome_tabela = input("Tabela: ")

        if not await verificar_tabela(conn, nome_tabela):
            print("Tabela não existe!")
            return

        async with conn.cursor() as cursor:
            await cursor.execute(f"SELECT id FROM {nome_tabela}")
            ids = [r[0] for r in await cursor.fetchall()]

            if not ids:
                print("Tabela vazia!")
                return

            try:
                id = int(input("ID: "))
            except:
                print("Inválido!")
                return

            if id not in ids:
                print("ID não existe!")
                return

            await cursor.execute(f"DELETE FROM {nome_tabela} WHERE id = %s", (id,))

        print("Eliminado!")

async def alterar_dados():
    async with pool.acquire() as conn:
        nome_tabela = input("Tabela: ")

        if not await verificar_tabela(conn, nome_tabela):
            print("Tabela não existe!")
            return

        async with conn.cursor() as cursor:
            await cursor.execute(f"DESCRIBE {nome_tabela}")
            colunas = [c[0] for c in await cursor.fetchall()]

            await cursor.execute(f"SELECT id FROM {nome_tabela}")
            ids = [r[0] for r in await cursor.fetchall()]

            try:
                id = int(input("ID: "))
            except:
                return

            print("Colunas:")
            for i, c in enumerate(colunas):
                print(f"{i+1} - {c}")

            idx = int(input("Escolha: ")) - 1
            novo = input("Novo valor: ")

            await cursor.execute(
                f"UPDATE {nome_tabela} SET {colunas[idx]} = %s WHERE id = %s",
                (novo, id)
            )

        print("Atualizado!")

async def listar_tabelas():
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SHOW TABLES")
            for t in await cursor.fetchall():
                print(t[0])

async def filtrar_dados():
    async with pool.acquire() as conn:
        nome_tabela = input("Tabela: ")

        if not await verificar_tabela(conn, nome_tabela):
            return

        async with conn.cursor() as cursor:
            criterio = input("Critério (ex: idade = 20): ")
            await cursor.execute(f"SELECT * FROM {nome_tabela} WHERE {criterio}")

            for r in await cursor.fetchall():
                print(r)

async def exportar_csv():
    async with pool.acquire() as conn:
        nome_tabela = input("Tabela: ")

        if not await verificar_tabela(conn, nome_tabela):
            return

        async with conn.cursor() as cursor:
            await cursor.execute(f"SELECT * FROM {nome_tabela}")
            dados = await cursor.fetchall()
            colunas = [d[0] for d in cursor.description]

            nome = f"{nome_tabela}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

            with open(nome, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(colunas)
                writer.writerows(dados)

        print("Exportado!")

async def importar_csv():
    async with pool.acquire() as conn:
        nome_tabela = input("Tabela: ")
        ficheiro = input("Ficheiro: ")

        if not os.path.isfile(ficheiro):
            print("Ficheiro não existe!")
            return

        async with conn.cursor() as cursor:
            with open(ficheiro, "r") as f:
                reader = csv.reader(f)
                colunas = next(reader)

                placeholders = ", ".join(["%s"] * len(colunas))
                sql = f"INSERT INTO {nome_tabela} ({', '.join(colunas)}) VALUES ({placeholders})"

                for linha in reader:
                    await cursor.execute(sql, tuple(linha))

        print("Importado!")

async def menu():
    while True:
        print("\n--- MENU ---")
        print("1 Criar tabela")
        print("2 Inserir dados")
        print("3 Consultar dados")
        print("4 Eliminar dados")
        print("5 Alterar dados")
        print("6 Listar tabelas")
        print("7 Filtrar")
        print("8 Exportar CSV")
        print("9 Importar CSV")
        print("0 Sair")

        op = input("Opção: ")

        if op == "1":
            await criar_tabela()
        elif op == "2":
            await adicionar_dados()
        elif op == "3":
            await consultar_dados()
        elif op == "4":
            await eliminar_dados()
        elif op == "5":
            await alterar_dados()
        elif op == "6":
            await listar_tabelas()
        elif op == "7":
            await filtrar_dados()
        elif op == "8":
            await exportar_csv()
        elif op == "9":
            await importar_csv()
        elif op == "0":
            break

async def main():
    global pool
    pool = await aiomysql.create_pool(**BD)

    await menu()

    pool.close()
    await pool.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
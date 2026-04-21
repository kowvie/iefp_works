import asyncio
import aiomysql
import csv
import os
import logging
from datetime import datetime
from dotenv import load_dotenv
from getpass import getpass

load_dotenv()

logging.basicConfig(
    filename="bd.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

pool = None


# 🔐 Config segura
def obter_config_bd():
    password = os.getenv("DB_PASSWORD")

    if not password:
        password = getpass("Password da BD: ")

    return {
        "host": os.getenv("DB_HOST", "localhost"),
        "port": int(os.getenv("DB_PORT", 3306)),
        "user": os.getenv("DB_USER", "root"),
        "password": password,
        "db": os.getenv("DB_NAME", "works"),
        "minsize": 1,
        "maxsize": 5,
        "autocommit": True
    }


# 🔒 Validação
def nome_valido(nome):
    return nome.isidentifier()


async def verificar_tabela(conn, nome):
    if not nome_valido(nome):
        return None

    async with conn.cursor() as cursor:
        await cursor.execute("SHOW TABLES LIKE %s", (nome,))
        return await cursor.fetchone()


# 🧱 Criar tabela
async def criar_tabela():
    async with pool.acquire() as conn:
        nome = input("Tabela: ")

        if not nome_valido(nome):
            print("Nome inválido!")
            return

        if await verificar_tabela(conn, nome):
            print("Já existe!")
            return

        n = int(input("Nº campos: "))
        campos = []

        for i in range(n):
            campo = input("Campo: ")
            tipo = input("Tipo: ")

            if not nome_valido(campo):
                print("Campo inválido!")
                return

            campos.append(f"{campo} {tipo}")

        async with conn.cursor() as cursor:
            await cursor.execute(
                f"CREATE TABLE {nome} (id INT AUTO_INCREMENT PRIMARY KEY, {', '.join(campos)})"
            )

        print("Tabela criada!")


# ➕ Inserir
async def adicionar_dados():
    async with pool.acquire() as conn:
        tabela = input("Tabela: ")

        if not await verificar_tabela(conn, tabela):
            print("Tabela não existe!")
            return

        async with conn.cursor() as cursor:
            await cursor.execute(f"DESCRIBE {tabela}")
            colunas = (await cursor.fetchall())[1:]

            valores = [input(f"{c[0]}: ") for c in colunas]

            placeholders = ", ".join(["%s"] * len(colunas))
            nomes = ", ".join([c[0] for c in colunas])

            await cursor.execute(
                f"INSERT INTO {tabela} ({nomes}) VALUES ({placeholders})",
                tuple(valores)
            )

        print("Inserido!")


# 📄 Consultar
async def consultar_dados():
    async with pool.acquire() as conn:
        tabela = input("Tabela: ")

        if not await verificar_tabela(conn, tabela):
            return

        async with conn.cursor() as cursor:
            await cursor.execute(f"SELECT * FROM {tabela}")
            for r in await cursor.fetchall():
                print(r)


# ❌ Eliminar
async def eliminar_dados():
    async with pool.acquire() as conn:
        tabela = input("Tabela: ")

        if not await verificar_tabela(conn, tabela):
            return

        async with conn.cursor() as cursor:
            await cursor.execute(f"SELECT id FROM {tabela}")
            ids = [r[0] for r in await cursor.fetchall()]

            if not ids:
                print("Vazia!")
                return

            id = int(input("ID: "))

            if id not in ids:
                print("Não existe!")
                return

            await cursor.execute(f"DELETE FROM {tabela} WHERE id=%s", (id,))

        print("Eliminado!")


# ✏️ Alterar
async def alterar_dados():
    async with pool.acquire() as conn:
        tabela = input("Tabela: ")

        if not await verificar_tabela(conn, tabela):
            return

        async with conn.cursor() as cursor:
            await cursor.execute(f"DESCRIBE {tabela}")
            colunas = [c[0] for c in await cursor.fetchall()]

            id = int(input("ID: "))

            for i, c in enumerate(colunas):
                print(i+1, c)

            idx = int(input("Coluna: ")) - 1
            novo = input("Novo valor: ")

            await cursor.execute(
                f"UPDATE {tabela} SET {colunas[idx]}=%s WHERE id=%s",
                (novo, id)
            )

        print("Atualizado!")


# 📤 Exportar
async def exportar_csv():
    async with pool.acquire() as conn:
        tabela = input("Tabela: ")

        if not await verificar_tabela(conn, tabela):
            return

        async with conn.cursor() as cursor:
            await cursor.execute(f"SELECT * FROM {tabela}")
            dados = await cursor.fetchall()
            colunas = [c[0] for c in cursor.description]

            nome = f"{tabela}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

            with open(nome, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(colunas)
                writer.writerows(dados)

        print("Exportado!")


# 📥 Importar
async def importar_csv():
    async with pool.acquire() as conn:
        tabela = input("Tabela: ")
        ficheiro = input("Ficheiro: ")

        if not os.path.isfile(ficheiro):
            print("Não existe!")
            return

        async with conn.cursor() as cursor:
            with open(ficheiro, "r") as f:
                reader = csv.reader(f)
                colunas = next(reader)

                sql = f"INSERT INTO {tabela} ({', '.join(colunas)}) VALUES ({', '.join(['%s']*len(colunas))})"

                for linha in reader:
                    await cursor.execute(sql, tuple(linha))

        print("Importado!")


# MENU
async def menu():
    while True:
        print("\n1 Criar | 2 Inserir | 3 Ver | 4 Eliminar | 5 Alterar | 6 Exportar | 7 Importar | 0 Sair")

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
            await exportar_csv()
        elif op == "7":
            await importar_csv()
        elif op == "0":
            break


async def main():
    global pool
    pool = await aiomysql.create_pool(**obter_config_bd())

    await menu()

    pool.close()
    await pool.wait_closed()


asyncio.run(main())
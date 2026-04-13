import pandas as pd

df = pd.DataFrame()
tipos_colunas = {}

def criar_dataframe():
    global df, tipos_colunas
    
    try:
        nrcolunas = int(input("Nº de colunas: "))
        data = {}
        tipos_colunas = {}
        num_linhas = None

        for i in range(nrcolunas):
            nome = input(f"Nome da coluna {i+1}: ")

            if nome in data:
                print("Coluna já existe!\n")
                return

            print("Tipo de dados:")
            print("1-Texto | 2-Inteiro | 3-Decimal | 4-Data")
            escolha = input("Opção: ")

            tipo = str
            if escolha == "2":
                tipo = int
            elif escolha == "3":
                tipo = float
            elif escolha == "4":
                tipo = "date"

            dados = input(f"Dados de {nome} separados por vírgula: ").split(',')
            dados = [d.strip() for d in dados]

            if num_linhas is None:
                num_linhas = len(dados)
            elif len(dados) != num_linhas:
                print("Erro no nº de dados!\n")
                return

            try:
                if tipo == "date":
                    dados = [pd.to_datetime(d, format="%d/%m/%Y") for d in dados]
                else:
                    dados = [tipo(d) for d in dados]
            except:
                print("Erro na conversão!\n")
                return

            data[nome] = dados
            tipos_colunas[nome] = tipo

        df = pd.DataFrame(data)
        print("DataFrame criado!\n")

    except:
        print("Erro!\n")

def consultar():
    if df.empty:
        print("DataFrame vazio!\n")
    else:
        print(df, "\n")

def adicionar_coluna():
    global df, tipos_colunas

    if df.empty:
        print("DataFrame vazio!\n")
        return

    nome = input("Nova coluna: ")

    if nome in df.columns:
        print("Já existe!\n")
        return

    print("Tipo: 1-Texto | 2-Int | 3-Float | 4-Data")
    escolha = input("Opção: ")

    tipo = str
    if escolha == "2":
        tipo = int
    elif escolha == "3":
        tipo = float
    elif escolha == "4":
        tipo = "date"

    dados = input("Dados: ").split(',')
    dados = [d.strip() for d in dados]

    if len(dados) != len(df):
        print("Erro no nº de dados!\n")
        return

    try:
        if tipo == "date":
            df[nome] = [pd.to_datetime(d, format="%d/%m/%Y") for d in dados]
        else:
            df[nome] = [tipo(d) for d in dados]

        tipos_colunas[nome] = tipo
        print("Coluna adicionada!\n")

    except:
        print("Erro!\n")

def remover_coluna():
    global df, tipos_colunas

    nome = input("Coluna a remover: ")

    if nome not in df.columns:
        print("Não existe!\n")
        return

    df.drop(columns=[nome], inplace=True)
    tipos_colunas.pop(nome, None)
    print("Removida!\n")

def adicionar_linha():
    global df, tipos_colunas

    if df.empty:
        print("DataFrame vazio!\n")
        return

    nova = []

    for col in df.columns:
        tipo = tipos_colunas[col]

        while True:
            valor = input(f"{col}: ")
            try:
                if tipo == "date":
                    valor = pd.to_datetime(valor, format="%d/%m/%Y")
                else:
                    valor = tipo(valor)
                nova.append(valor)
                break
            except:
                print("Valor inválido!")

    df.loc[len(df)] = nova
    print("Linha adicionada!\n")

def editar():
    global df, tipos_colunas

    consultar()

    try:
        linha = int(input("Linha: "))
        coluna = input("Coluna: ")

        if linha not in df.index or coluna not in df.columns:
            print("Erro!\n")
            return

        tipo = tipos_colunas[coluna]

        while True:
            valor = input("Novo valor: ")
            try:
                if tipo == "date":
                    valor = pd.to_datetime(valor, format="%d/%m/%Y")
                else:
                    valor = tipo(valor)
                break
            except:
                print("Tipo inválido!")

        df.at[linha, coluna] = valor
        print("Atualizado!\n")

    except:
        print("Erro!\n")

def filtrar():
    consultar()
    col = input("Coluna: ")

    if col not in df.columns:
        print("Inválido!\n")
        return

    valor = input("Valor: ")
    print(df[df[col].astype(str) == valor], "\n")

def ordenar():
    consultar()
    col = input("Coluna: ")

    if col not in df.columns:
        print("Inválido!\n")
        return

    ordem = input("A/D: ")
    asc = True if ordem.upper() == "A" else False

    print(df.sort_values(by=col, ascending=asc), "\n")

while True:
    print("SISTEMA DATAFRAME")
    print("1 Criar")
    print("2 Consultar")
    print("3 Adicionar Coluna")
    print("4 Remover Coluna")
    print("5 Adicionar Linha")
    print("6 Editar")
    print("7 Filtrar")
    print("8 Ordenar")
    print("0 Sair")

    op = input("Opção: ")

    if op == "1":
        criar_dataframe()
    elif op == "2":
        consultar()
    elif op == "3":
        adicionar_coluna()
    elif op == "4":
        remover_coluna()
    elif op == "5":
        adicionar_linha()
    elif op == "6":
        editar()
    elif op == "7":
        filtrar()
    elif op == "8":
        ordenar()
    elif op == "0":
        break
    else:
        print("Inválido!\n")
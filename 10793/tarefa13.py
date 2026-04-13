import pandas as pd

df = pd.DataFrame()
tipos_colunas = {} 

def criar_dataframe():
    global df, tipos_colunas
    
    try:
        nrcolunas = int(input("Indique o nº de colunas para criar o Data Frame: "))
        
        data = {}
        tipos_colunas = {}
        num_linhas = None
        
        for i in range(nrcolunas):
            nome_coluna = input(f"Introduza o nome da coluna {i + 1}: ")
            
            if nome_coluna in data:
                print("Coluna já existe!\n")
                return
            
            print("Escolha o tipo de dados:")
            print("1 - Texto")
            print("2 - Inteiro")
            print("3 - Decimal")
            print("4 - Data (DD/MM/AAAA)")
            
            escolha = input("Opção: ")
            
            if escolha == "1":
                tipo = str
            elif escolha == "2":
                tipo = int
            elif escolha == "3":
                tipo = float
            elif escolha == "4":
                tipo = "date"
            else:
                print("Opção inválida! Será considerado Texto.")
                tipo = str
            
            dados = input(f"Introduza os dados da coluna '{nome_coluna}' separados por vírgula: ").split(',')
            dados = [d.strip() for d in dados]
            
            if num_linhas is None:
                num_linhas = len(dados)
            elif len(dados) != num_linhas:
                print("Número de valores inválido!\n")
                return
            
            try:
                if tipo == "date":
                    dados_convertidos = [pd.to_datetime(d, format="%d/%m/%Y") for d in dados]
                else:
                    dados_convertidos = [tipo(d) for d in dados]
            except ValueError:
                print("Erro na conversão dos dados!\n")
                return
            
            data[nome_coluna] = dados_convertidos
            tipos_colunas[nome_coluna] = tipo
        
        df = pd.DataFrame(data)
        print("Data Frame criado com sucesso!\n")
    
    except ValueError:
        print("Erro! Número inválido.\n")

def consultar_dataframe():
    global df
    
    if df.empty:
        print("Data Frame vazio!\n")
        return
    
    print("Dados atuais do Data Frame:")
    print(df)
    print()

def adicionar_coluna():
    global df, tipos_colunas
    
    if df.empty:
        print("Data Frame vazio!\n")
        return
    
    nome_coluna = input("Nome da nova coluna: ")
    
    if nome_coluna in df.columns:
        print("Coluna já existe!\n")
        return
    
    print("Escolha o tipo de dados:")
    print("1 - Texto")
    print("2 - Inteiro")
    print("3 - Decimal")
    print("4 - Data (DD/MM/AAAA)")
    
    escolha = input("Opção: ")
    
    if escolha == "1":
        tipo = str
    elif escolha == "2":
        tipo = int
    elif escolha == "3":
        tipo = float
    elif escolha == "4":
        tipo = "date"
    else:
        print("Opção inválida! Será considerado Texto.")
        tipo = str
    
    dados = input("Introduza os dados separados por vírgula: ").split(',')
    dados = [d.strip() for d in dados]
    
    if len(dados) != len(df.index):
        print("Número de valores inválido!\n")
        return
    
    try:
        if tipo == "date":
            df[nome_coluna] = [pd.to_datetime(d, format="%d/%m/%Y") for d in dados]
        else:
            df[nome_coluna] = [tipo(d) for d in dados]
        
        tipos_colunas[nome_coluna] = tipo
        print("Coluna adicionada com sucesso!\n")
    
    except ValueError:
        print("Erro na conversão dos dados!\n")

def eliminar_coluna():
    global df, tipos_colunas
    
    if df.empty:
        print("Data Frame vazio!\n")
        return
    
    consultar_dataframe()
    
    nome_coluna = input("Indique o nome da coluna a remover: ")
    
    if nome_coluna not in df.columns:
        print("Coluna não encontrada!\n")
        return
    
    df.drop(columns=[nome_coluna], inplace=True)
    tipos_colunas.pop(nome_coluna, None)
    print("Coluna removida com sucesso!\n")

def adicionar_linha():
    global df, tipos_colunas
    
    if df.empty:
        print("Data Frame vazio!\n")
        return
    
    nova_linha = []
    
    for coluna in df.columns:
        tipo = tipos_colunas[coluna]
        
        while True:
            valor = input(f"Valor para '{coluna}': ")
            try:
                if tipo == "date":
                    valor_convertido = pd.to_datetime(valor, format="%d/%m/%Y")
                else:
                    valor_convertido = tipo(valor)
                
                nova_linha.append(valor_convertido)
                break
            except ValueError:
                print("Tipo inválido! Tente novamente.")
    
    df.loc[len(df)] = nova_linha
    print("Linha adicionada com sucesso!\n")


def editar_valor():
    global df, tipos_colunas
    
    if df.empty:
        print("Data Frame vazio!\n")
        return
    
    consultar_dataframe()
    
    try:
        linha = int(input("Indique o índice da linha: "))
        coluna = input("Indique o nome da coluna: ")
        
        if linha not in df.index or coluna not in df.columns:
            print("Linha ou coluna inválida!\n")
            return
        
        tipo = tipos_colunas[coluna]
        
        while True:
            novo_valor = input("Novo valor: ")
            try:
                if tipo == "date":
                    novo_valor = pd.to_datetime(novo_valor, format="%d/%m/%Y")
                else:
                    novo_valor = tipo(novo_valor)
                break
            except ValueError:
                print("Tipo de dado inválido! Tente novamente.")
        
        df.at[linha, coluna] = novo_valor
        print("Valor atualizado com sucesso!\n")
    
    except ValueError:
        print("Índice inválido!\n")

while True:
    print("Sistema DataFrame")
    print("A - Criar Data Frame")
    print("B - Consultar Data Frame")
    print("C - Adicionar Coluna")
    print("D - Eliminar Coluna")
    print("E - Adicionar Linha")
    print("F - Editar Valor")
    print("Z - Terminar")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha.upper() == "A":
        criar_dataframe()
    elif escolha.upper() == "B":
        consultar_dataframe()
    elif escolha.upper() == "C":
        adicionar_coluna()
    elif escolha.upper() == "D":
        eliminar_coluna()
    elif escolha.upper() == "E":
        adicionar_linha()
    elif escolha.upper() == "F":
        editar_valor()
    elif escolha.upper() == "Z":
        print("Programa terminado. Obrigado!")
        break
    else:
        print("Opção inválida!\n")
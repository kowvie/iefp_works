import pandas as pd

df = pd.DataFrame()

def criar_dataframe():
    global df
    
    try:
        nrcolunas = int(input("Indique o nº de colunas para criar o Data Frame: "))
        
        data = {}
        num_linhas = None
        
        for i in range(nrcolunas):
            nome_coluna = input(f"Introduza o nome da coluna {i + 1}: ")
            
            if nome_coluna in data:
                print(f"A coluna '{nome_coluna}' já foi registada!")
                return
            
            dados = input(f"Introduza os dados da coluna '{nome_coluna}' separados por vírgula: ").split(',')
            dados = [d.strip() for d in dados]
            
            if num_linhas is None:
                num_linhas = len(dados)
            elif len(dados) != num_linhas:
                print(f"Erro! Devem ser registados {num_linhas} valores.")
                return
            
            data[nome_coluna] = dados
        
        df = pd.DataFrame(data)
        print("Data Frame criado com sucesso!\n")
        
    except ValueError:
        print("Erro! O nº de colunas deve ser um número inteiro!\n")

def consultar_dataframe():
    global df
    
    if df.empty:
        print("O Data Frame está vazio!\n")
        return
    
    print("Dados atuais do Data Frame:")
    print(df)
    print()

def adicionar_coluna():
    global df
    
    if df.empty:
        print("O Data Frame está vazio!\n")
        return
    
    consultar_dataframe()
    
    nome_coluna = input("Indique o nome da nova coluna: ")
    
    if nome_coluna in df.columns:
        print("Essa coluna já existe!\n")
        return
    
    dados = input(f"Introduza os dados para '{nome_coluna}' separados por vírgula: ").split(',')
    dados = [d.strip() for d in dados]
    
    if len(dados) != len(df.index):
        print(f"Erro! Deve introduzir exatamente {len(df.index)} valores.\n")
        return
    
    df[nome_coluna] = dados
    print("Coluna adicionada com sucesso!\n")

def eliminar_coluna():
    global df
    
    if df.empty:
        print("O Data Frame está vazio!\n")
        return
    
    consultar_dataframe()
    
    nome_coluna = input("Indique o nome da coluna a remover: ")
    
    if nome_coluna not in df.columns:
        print("Erro! Coluna não encontrada.\n")
        return
    
    df.drop(columns=[nome_coluna], inplace=True)
    print("Coluna removida com sucesso!\n")

def ordenar_dataframe():
    global df
    
    if df.empty:
        print("O Data Frame está vazio!\n")
        return
    
    consultar_dataframe()
    
    coluna = input("Indique o nome da coluna para ordenar: ")
    
    if coluna not in df.columns:
        print("Coluna inválida!\n")
        return
    
    ordem = input("Ordenar Ascendente (A) ou Descendente (D)? ")
    
    if ordem.upper() == "A":
        df_ordenado = df.sort_values(by=coluna, ascending=True)
    elif ordem.upper() == "D":
        df_ordenado = df.sort_values(by=coluna, ascending=False)
    else:
        print("Opção inválida!\n")
        return
    
    print("Data Frame ordenado:")
    print(df_ordenado)
    print()

while True:
    print("Sistema de Registo Académico")
    print("A - Criar Data Frame")
    print("B - Consultar Data Frame")
    print("C - Adicionar Coluna")
    print("D - Eliminar Coluna")
    print("E - Ordenar Dados")
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
        ordenar_dataframe()
    elif escolha.upper() == "Z":
        print("Programa terminado. Obrigado!")
        break
    else:
        print("Opção inválida!\n")
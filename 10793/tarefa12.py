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
                print(f"A coluna '{nome_coluna}' já foi registada!\n")
                return
            
            dados = input(f"Introduza os dados da coluna '{nome_coluna}' separados por vírgula: ").split(',')
            dados = [d.strip() for d in dados]
            
            if num_linhas is None:
                num_linhas = len(dados)
            elif len(dados) != num_linhas:
                print(f"Erro! Devem ser registados {num_linhas} valores.\n")
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

def renomear_coluna():
    global df
    
    if df.empty:
        print("Data Frame vazio!\n")
        return
    
    consultar_dataframe()
    
    nome_coluna = input("Indique o nome da coluna a renomear: ")
    
    if nome_coluna not in df.columns:
        print("Coluna não encontrada!\n")
        return
    
    novo_nome = input("Indique o novo nome da coluna: ")
    
    if not novo_nome:
        print("Nome inválido!\n")
        return
    
    if novo_nome in df.columns:
        print("Já existe uma coluna com esse nome!\n")
        return
    
    df.rename(columns={nome_coluna: novo_nome}, inplace=True)
    print("Coluna renomeada com sucesso!\n")

def filtrar_dataframe():
    global df
    
    if df.empty:
        print("Data Frame vazio!\n")
        return
    
    consultar_dataframe()
    
    coluna = input("Indique a coluna para filtrar: ")
    
    if coluna not in df.columns:
        print("Coluna inválida!\n")
        return
    
    criterio = input("Indique o valor a procurar: ")
    
    filtro = df[df[coluna] == criterio]
    
    print("Resultado do filtro:")
    print(filtro)
    print()

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

def adicionar_linha():
    global df
    
    if df.empty:
        print("Data Frame vazio!\n")
        return
    
    nova_linha = []
    
    for coluna in df.columns:
        valor = input(f"Introduza o valor para '{coluna}': ")
        nova_linha.append(valor)
    
    df.loc[len(df)] = nova_linha
    print("Linha adicionada com sucesso!\n")

def remover_linha():
    global df
    
    if df.empty:
        print("Data Frame vazio!\n")
        return
    
    consultar_dataframe()
    
    try:
        indice = int(input("Indique o índice da linha a remover: "))
        
        if indice not in df.index:
            print("Índice inválido!\n")
            return
        
        df.drop(index=indice, inplace=True)
        print("Linha removida com sucesso!\n")
        
    except ValueError:
        print("O índice deve ser um número inteiro!\n")

def editar_valor():
    global df
    
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
        
        novo_valor = input("Indique o novo valor: ")
        df.at[linha, coluna] = novo_valor
        
        print("Valor atualizado com sucesso!\n")
        
    except ValueError:
        print("O índice deve ser um número inteiro!\n")

def exportar_excel():
    global df
    
    if df.empty:
        print("Data Frame vazio!\n")
        return
    
    nome = input("Nome do ficheiro: ")
    
    if not nome.endswith(".xlsx"):
        nome += ".xlsx"
    
    df.to_excel(nome, index=False)
    print("Ficheiro exportado com sucesso!\n")

def importar_excel():
    global df
    
    nome = input("Nome do ficheiro a importar: ")
    
    if not nome.endswith(".xlsx"):
        nome += ".xlsx"
    
    try:
        df = pd.read_excel(nome)
        print("Ficheiro importado com sucesso!\n")
    except FileNotFoundError:
        print("Ficheiro não encontrado!\n")

while True:
    print("Sistema de Registo Académico")
    print("A - Criar Data Frame")
    print("B - Consultar Data Frame")
    print("C - Adicionar Coluna")
    print("D - Eliminar Coluna")
    print("E - Ordenar Dados")
    print("F - Renomear Coluna")
    print("G - Filtrar Dados")
    print("H - Adicionar Linha")
    print("I - Remover Linha")
    print("J - Editar Valor")
    print("K - Exportar Excel")
    print("L - Importar Excel")
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
    elif escolha.upper() == "F":
        renomear_coluna()
    elif escolha.upper() == "G":
        filtrar_dataframe()
    elif escolha.upper() == "H":
        adicionar_linha()
    elif escolha.upper() == "I":
        remover_linha()
    elif escolha.upper() == "J":
        editar_valor()
    elif escolha.upper() == "K":
        exportar_excel()
    elif escolha.upper() == "L":
        importar_excel()
    elif escolha.upper() == "Z":
        print("Programa terminado. Obrigado!")
        break
    else:
        print("Opção inválida!\n")
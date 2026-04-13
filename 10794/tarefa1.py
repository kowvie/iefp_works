import mysql.connector

try:
    ligação = mysql.connector.connect(
        host = "localhost",      #Servidor da BD (neste caso, local - localhost)
        user = "root",           #Nome do utilizador da BD
        password = "JsSribeiro14",     #Palavra-passe do utilizador
        database = "works"     #Nome da base de dados a utilizar
    )
    
    print("Ligação estabelecida com sucesso! ")
    
    cursor = ligação.cursor()
    
    instrução1 = """
    CREATE TABLE IF NOT EXISTS utilizadores(
        id INT AUTO_INCREMENT PRIMARY KEY,  
        nome VARCHAR(255),                 
        Idade INT                          
    )
    """
    cursor.execute(instrução1)
    
    print("Tabela Utilizadores Criada com sucesso!")

    instrução2 = "INSERT INTO utilizadores (nome, idade) VALUES (%s, %s)"
    
    cursor.execute("SELECT COUNT(*) FROM utilizadores")
    
    total = cursor.fetchone()[0]

    if total == 0:
        dados = [
            ("Nome1", 24),
            ("Nome2", 15),
            ("Nome3", 36),
            ("Nome4", 18)
        ]
        
        cursor.executemany(instrução2, dados)

        print("Dados adicionados com sucesso!")
    else:
        print("A tabela já tem dados! ")  
    
    instrução3 = "SELECT * FROM utilizadores"
    
    cursor.execute(instrução3) 
    
    resultados = cursor.fetchall()     
    
    for resultado in resultados:
        print(resultado)
        
    ligação.commit()
    
    cursor.close()
    
    ligação.close()

except mysql.connector.Error as erro:
    print(f"Erro ao estabelecer ligação à BD: {erro}")
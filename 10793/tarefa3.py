numeros = [2, 7, 15, 2.5, 9, 1, 18, -2]
numeros2 = [14, 22, 7, 3, -15, 25]

def somatorio():
    soma = sum(numeros)
    print(f"O valor do somatório dos dados do array é: {soma}")

def media():
    soma = sum(numeros)
    comprimento = len(numeros)
    med = round(soma / comprimento, 3)

    print(f"O valor da média dos valores do array é: {med}")

def max_val():
    maior_valor = max(numeros)
    print(f"O maior valor presente no array  é: {maior_valor}")

def min_val():
    menor_valor = min(numeros)
    print(f"O menor valor presente no array é: {menor_valor}")

def somatorio_2():
    somatório2 = sum(numeros2)
    print(f"O valor do somatório dos dados do segundo array é: {somatório2}")

def media_2():
    soma2 = sum(numeros2)
    comprimento2 = len(numeros2)
    media2 = round(soma2 / comprimento2, 3)

    print(f"O valor da média dos valores do array é: {media2}")

def max_val_2():
    maior_valor2 = max(numeros2)
    print(f"O maior valor presente no array  é: {maior_valor2}")

def min_val_2():
    menor_valor2 = min(numeros2)
    print(f"O menor valor presente no array é: {menor_valor2}")


print("Bem-Vindo(a) \n")
print("a - Valor somatorio do primeiro array\n")
print("b - Media do primeiro array \n") 
print("c - Maior valor do primeiro array \n") 
print("d - Menor valor do primeiro array \n") 
print("e - Valor somatorio do segundo array\n")
print("f - Media do segundo array \n") 
print("g - Maior valor do segundo array \n") 
print("h - Menor valor do segundo array \n")   
print("z - Terminar Programa \n")

while True:
    escolha = input("Indique a opção a executar: \n")
    
    if escolha.lower() == "a":
        somatorio()
    elif escolha.lower() == "b":
        media()
    elif escolha.lower() == "c":
        max_val()
    elif escolha.lower() == "d":
        min_val()
    elif escolha.lower() == "e":
        somatorio_2()
    elif escolha.lower() == "f":
        media_2()
    elif escolha.lower() == "g":
        max_val_2()
    elif escolha.lower() == "h":
        min_val_2()
    elif escolha.lower() == "z":
        print("Obrigado! \n")
        break
    else:
        print("Erro! Introduziu uma opção inválida! ")        
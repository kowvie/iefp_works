def soma():
    try:    
        a = float(input("Introduza o primeiro número a somar: "))
        b = float(input("Introduza o segundo número a somar: "))
        
        soma = a + b
        
        print(f"Resutaldo : {soma}")
    except ValueError:
        print("Erro! Por favor certifique-se de que introduz um nº real!")

def subtracao():
    try:    
        a = float(input("Introduza o primeiro número a subtrair: "))
        b = float(input("Introduza o segundo número a subtrair: "))
        
        sub = a - b
        
        print(f"Resutaldo : {sub}")
    except ValueError:
        print("Erro! Por favor certifique-se de que introduz um nº real!")  

def multi():
    try:    
        a = float(input("Introduza o primeiro número a multiplicar: "))
        b = float(input("Introduza o segundo número a multiplicar: "))
        
        mult = a * b
        
        print(f"Resutaldo : {mult}")
    except ValueError:
        print("Erro! Por favor certifique-se de que introduz um nº real!") 
        
def divisão():
    try:
        num1 = float(input("Introduza o primeiro número: "))
        num2 = float(input("Introduza o segundo número: "))
        
        
        div = num1/num2
        print(f"O resultado da divisão é: {div}")
            
    except ZeroDivisionError:
        print("Erro! É impossível dividir por 0!") 
    except ValueError:
        print("Erro! Por favor certifique-se de que introduz um nº real!")               
    
print("Bem-Vindo(a) \n")
print("a - Somar 2 números \n")
print("b - Dividir 2 números \n") 
print("c - Multiplicar 2 números \n") 
print("d - Subtrair 2 números \n")    
print("z - Terminar Programa \n")

while True:
    escolha = input("Indique a opção a executar: \n")
    
    if escolha.lower() == "a":
        soma()
    elif escolha.lower() == "b":
        divisão()
    elif escolha.lower() == "c":
        multi()
    elif escolha.lower() == "d":
        subtracao()
    elif escolha.lower() == "z":
        print("Obrigado! \n")
        break
    else:
        print("Erro! Introduziu uma opção inválida! ")        
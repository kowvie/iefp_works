"""Teste"""
import os
from datetime import date

def calcular_idade (ano_nascimento: int)-> int:
   """funcao de calculo"""
   ano_atual = date.today().year
   return ano_atual - ano_nascimento

def definir_categoria(idade: int)-> str:
    """categorias de idade"""
    if idade < 10:
        return "Child"
    elif idade < 18:
        return "Teenager"
    elif idade < 65:
        return "Adult"
    elif idade < 100:
        return "Senior"
    else:
        return "Elderly"


if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        try:
            ano_nascimento_input = int(input("Insert your birth year"))
            idade_aux = calcular_idade(ano_nascimento_input)

            if idade_aux < 0:
                print("Invalid birth year!")
                print("press any key to continue...")
                continue

            print(f"The age of {ano_nascimento_input} birth years is {idade_aux} years")
            print(f"Is{definir_categoria(idade_aux)}")

            continuar: str = input("Wish to continue? (s/n)").lower()
            if continuar == 'n':
                break

        except ValueError as e:
            print('Errors', e)
            print("Insert a valid value")
            print()
            print("Press any key to continue...")

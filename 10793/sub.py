try:
    num1 = int(input("introduz o primeiro numero: "))
    num2 = int(input("introduz o segundo numero: "))

    sub = num1 - num2 

    print(f"o resultado da subtracao entre {num1} e {num2} sera: {sub}")
except ValueError:
    print("os numeros introduzidos devem de ser inteiros!")
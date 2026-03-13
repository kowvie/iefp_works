print ("sim senhora \n")
try:
    num1 = int(input("introduz o primeiro numero: "))
    num2 = int(input("introduz o segundo numero: "))

    soma = num1 + num2 

    print(f"o resultado da soma entre {num1} e {num2} sera: {soma}")
except ValueError:
    print("os numeros introduzidos devem de ser inteiros!")

 #if else exemplo

    try:
        numero = int(input("introduza um numero: "))

        if numero > 0:
            print("o numero e positivo!")
        elif numero == 0:
            print("o numero e 0!")
        else:
            print("o numero e negativo")
    except  ValueError:
        print("erro, o numero a verificar deve de ser inteiro")

#exemplo if esle 2

tempo = input("gostas de rosa? (S/N/?)")

if tempo.lower() == "S":
    print("On thursdays we wear pink!")
elif tempo.lower() == "N":
    print("You can't sit with us")
else:
    print("Decide then u indecisive bloat")
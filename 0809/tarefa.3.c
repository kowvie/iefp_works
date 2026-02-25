#include <iostream>
using namespace std;

float subtrair(float num1, float num2){
    return num1 - num2;
}

float multiplicar(float valor, float taxa){
    return valor * taxa;
}

int main()
{
    float num1, num2, resultado;
    int opcao;

    cout << "Bem-Vindo(a)" << endl;
    cout << "1 - Subtrair 2 numeros reais" << endl;
    cout << "2 - Subtrair e multiplicar por 10 se positivo" << endl;
    cout << "Escolha a opcao a executar: ";

    if (!(cin >> opcao)){
        cout << "Erro! Deve introduzir um valor numerico!" << endl;
        return 1;
    }

    cout << "Introduza o primeiro numero: ";
    if (!(cin >> num1)){
        cout << "Erro! Deve introduzir um valor numerico!" << endl;
        return 1;
    }

    cout << "Introduza o segundo numero: ";
    if (!(cin >> num2)){
        cout << "Erro! Deve introduzir um valor numerico!" << endl;
        return 1;
    }

    if (opcao == 1){
        resultado = subtrair(num1, num2);
        cout << "Resultado da subtracao: " << resultado << endl;
    }
    else if (opcao == 2){
        resultado = subtrair(num1, num2);
        cout << "Resultado da subtracao: " << resultado << endl;

        if (resultado > 0){
            cout << "Valor positivo." << endl;
            float mult = multiplicar(resultado, 10);
            cout << "Multiplicado por 10: " << mult << endl;
        }
        else{
            cout << "Valor negativo." << endl;
        }
    }
    else{
        cout << "Erro! Opcao invalida!" << endl;
        return 1;
    }

    return 0;
}

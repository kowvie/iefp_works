#include <iostream>
#include <iomanip>
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

    do {
        cout << "\n===== CALCULADORA =====" << endl;
        cout << "1 - Subtrair 2 numeros reais" << endl;
        cout << "2 - Subtrair e multiplicar por 10 se positivo" << endl;
        cout << "0 - Sair" << endl;
        cout << "Escolha a opcao: ";

        if (!(cin >> opcao)){
            cout << "Erro! Deve introduzir um valor numerico!" << endl;
            cin.clear();
            cin.ignore(1000, '\n');
            continue;
        }

        if (opcao == 0){
            cout << "Programa Terminado!" << endl;
            break;
        }

        cout << "Introduza o primeiro numero: ";
        if (!(cin >> num1)){
            cout << "Erro! Deve introduzir um valor numerico!" << endl;
            cin.clear();
            cin.ignore(1000, '\n');
            continue;
        }

        cout << "Introduza o segundo numero: ";
        if (!(cin >> num2)){
            cout << "Erro! Deve introduzir um valor numerico!" << endl;
            cin.clear();
            cin.ignore(1000, '\n');
            continue;
        }

        cout << fixed << setprecision(2);

        switch(opcao){

            case 1:
                resultado = subtrair(num1, num2);
                cout << "Resultado da subtracao: " << resultado << endl;
                break;

            case 2:
                resultado = subtrair(num1, num2);
                cout << "Resultado da subtracao: " << resultado << endl;

                if (resultado > 0){
                    cout << "Valor positivo." << endl;
                    cout << "Multiplicado por 10: " 
                         << multiplicar(resultado, 10) << endl;
                }
                else{
                    cout << "Valor negativo." << endl;
                }
                break;

            default:
                cout << "Erro! Opcao invalida!" << endl;
        }

    } while (opcao != 0);

    return 0;
}

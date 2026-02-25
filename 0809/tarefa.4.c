///parte 1

#include <iostream>
#include <iomanip>

int main()
{
    int opcao;
    float saldo, preco;

    do {
        cout << "\nMENU COMPRA" << endl;
        cout << "1 - Efetuar compra" << endl;
        cout << "0 - Sair" << endl;
        cout << "Escolha uma opcao: ";
        cin >> opcao;

        switch(opcao){

            case 1:
                cout << "Introduza o saldo disponivel: ";
                cin >> saldo;

                cout << "Introduza o preco do produto: ";
                cin >> preco;

                if (saldo >= preco){
                    cout << "Compra realizada com sucesso!" << endl;
                    cout << "Troco: " << fixed << setprecision(2)
                         << saldo - preco << " euros" << endl;
                }
                else{
                    cout << "Saldo insuficiente!" << endl;
                }
                break;

            case 0:
                cout << "Programa terminado!" << endl;
                break;

            default:
                cout << "Opcao invalida!" << endl;
        }

    } while (opcao != 0);

    return 0;
}

//parte2 - alteracao do exemplo 8
#include <iostream>

int main() {

    int i = 15;

    do {
        cout << "Contagem: " << i << endl;
        i--;
    } while (i >= 5);

    return 0;
}

// parte 3
#include <iostream>

int main() {

    int numeros[5];
    int soma = 0;
    int maior;

    for (int i = 0; i < 5; i++){
        cout << "Introduza um numero: ";
        cin >> numeros[i];

        soma += numeros[i];

        if (i == 0 || numeros[i] > maior){
            maior = numeros[i];
        }
    }

    float media = soma / 5.0;

    cout << "\nNumeros registados:\n";

    for (int i = 0; i < 5; i++){
        cout << numeros[i] << endl;
    }

    cout << "Media: " << media << endl;
    cout << "Maior numero: " << maior << endl;

    return 0;
}

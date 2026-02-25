#include <iostream>
#include <iomanip>

int main()
{
    float produtos[5];
    float saldo, total = 0;

    cout << "SIMULADOR DE COMPRA" << endl;

    cout << "Introduza o saldo disponivel: ";
    cin >> saldo;

    for(int i = 0; i < 5; i++)
    {
        cout << "Preco do produto " << i + 1 << ": ";
        cin >> produtos[i];
        total += produtos[i];
    }

    float restante = saldo - total;

    cout << fixed << setprecision(2);
    cout << "\nTotal da compra: " << total << " euros" << endl;
    cout << "Saldo restante: " << restante << " euros" << endl;

    if (restante >= 0)
        cout << "Compra efetuada com sucesso!" << endl;
    else
        cout << "Saldo insuficiente!" << endl;

    return 0;
}

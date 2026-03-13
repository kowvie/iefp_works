#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>

using namespace std;

struct Produto{
    string nome;
    float preco;
    int quantidade;
}

bool login(){

    string utilizador;
    string password;

    cout << "Utilizador: ";
    getline(cin, utilizador);

    cout << "Password: ";
    getline(cin, password);

    transform(utilizador.begin(), utilizador.end(),
              utilizador.begin(), ::tolower);

    if(utilizador=="admin" && password=="1234")
        return true;

    return false;
}

void atualizar_estatisticas(vector<Produto> &produtos,
                            float &valor_total,
                            float &precomaior,
                            float &precomenor){

    valor_total = 0;

    if(produtos.empty()){
        precomaior = precomenor = 0;
        return;
    }

    precomaior = precomenor = produtos[0].preco;

    for(auto &p : produtos){

        valor_total += p.preco * p.quantidade;

        if(p.preco > precomaior)
            precomaior = p.preco;

        if(p.preco < precomenor)
            precomenor = p.preco;
    }
}

void adicionar_produto(vector<Produto> &produtos){

    Produto p;

    cout << "Nome do produto: ";
    getline(cin, p.nome);

    cout << "Preco: ";
    cin >> p.preco;

    cout << "Quantidade: ";
    cin >> p.quantidade;
    cin.ignore();

    produtos.push_back(p);
}

void listar_produtos(vector<Produto> &produtos){

    if(produtos.empty()){
        cout << "Nao existem produtos.\n";
        return;
    }

    cout << "\nLista de Produtos:\n";

    for(int i=0;i<produtos.size();i++){
        cout << i << " - "
             << produtos[i].nome << " | "
             << produtos[i].preco << " | "
             << produtos[i].quantidade << endl;
    }
}

void eliminar_produto(vector<Produto> &produtos){

    if(produtos.empty()){
        cout<<"Nao existem produtos.\n";
        return;
    }

    listar_produtos(produtos);

    int indice;
    cout<<"Indice a eliminar: ";
    cin>>indice;
    cin.ignore();

    if(indice>=0 && indice<produtos.size()){
        produtos.erase(produtos.begin()+indice);
        cout<<"Produto removido com sucesso.\n";
    }
}

void atualizar_produto(vector<Produto> &produtos){

    if(produtos.empty()){
        cout<<"Nao existem produtos.\n";
        return;
    }

    listar_produtos(produtos);

    int indice;
    cout<<"Indice a atualizar: ";
    cin>>indice;
    cin.ignore();

    if(indice>=0 && indice<produtos.size()){

        cout<<"Novo nome: ";
        getline(cin, produtos[indice].nome);

        cout<<"Novo preco: ";
        cin>>produtos[indice].preco;

        cout<<"Nova quantidade: ";
        cin>>produtos[indice].quantidade;
        cin.ignore();

        cout<<"Produto atualizado com sucesso.\n";
    }
}

void filtrar_produtos(vector<Produto> &produtos){

    if(produtos.empty()){
        cout<<"Nao existem produtos.\n";
        return;
    }

    float preco_min;

    cout<<"Preco minimo: ";
    cin>>preco_min;
    cin.ignore();

    bool encontrado=false;

    for(auto &p : produtos){
        if(p.preco >= preco_min){
            cout<<p.nome<<" | "
                <<p.preco<<" | "
                <<p.quantidade<<endl;
            encontrado=true;
        }
    }

    if(!encontrado)
        cout<<"Nenhum produto encontrado.\n";
}

void exportar_dados(vector<Produto> &produtos){

    ofstream f("produtos_backup.txt");

    for(auto &p : produtos){
        f<<p.nome<<" "
         <<p.preco<<" "
         <<p.quantidade<<endl;
    }

    cout<<"Backup exportado com sucesso.\n";
}

void importar_dados(vector<Produto> &produtos){

    ifstream f("produtos_backup.txt");

    if(!f){
        cout<<"Ficheiro nao encontrado.\n";
        return;
    }

    produtos.clear();

    Produto p;

    while(f>>p.nome>>p.preco>>p.quantidade){
        produtos.push_back(p);
    }

    cout<<"Dados importados com sucesso.\n";
}

void produto_mais_caro(vector<Produto> &produtos){

    if(produtos.empty()){
        cout<<"Nao existem produtos.\n";
        return;
    }

    float maior = produtos[0].preco;

    for(auto &p : produtos){
        if(p.preco > maior)
            maior = p.preco;
    }

    cout<<"Produto(s) mais caro(s):\n";

    for(auto &p : produtos){
        if(p.preco == maior)
            cout<<p.nome<<" | "
                <<p.preco<<" | "
                <<p.quantidade<<endl;
    }
}

int contar_stock_baixo(vector<Produto> &produtos){

    int contador = 0;

    for(auto &p : produtos){
        if(p.quantidade < 5)
            contador++;
    }

    if(contador==0)
        cout<<"Nao existem produtos com stock baixo.\n";

    return contador;
}

int main(){

    if(!login()){
        cout<<"Acesso negado!\n";
        return 0;
    }

    cout<<"Bem-vindo(a)!\n";

    vector<Produto> produtos;

    float valor_total, precomaior, precomenor;
    int opcao;

    do{

        cout<<"\n1 - Listar Produtos\n";
        cout<<"2 - Adicionar Produto\n";
        cout<<"3 - Eliminar Produto\n";
        cout<<"4 - Atualizar Produto\n";
        cout<<"5 - Estatisticas\n";
        cout<<"6 - Filtrar Produtos\n";
        cout<<"7 - Exportar Backup\n";
        cout<<"8 - Importar Backup\n";
        cout<<"9 - Produto(s) Mais Caro(s)\n";
        cout<<"10 - Contar Stock Baixo\n";
        cout<<"0 - Sair\n";

        cout<<"Opcao: ";
        cin>>opcao;
        cin.ignore();

        switch(opcao){

            case 1:
                listar_produtos(produtos);
                break;

            case 2:
                adicionar_produto(produtos);
                break;

            case 3:
                eliminar_produto(produtos);
                break;

            case 4:
                atualizar_produto(produtos);
                break;

            case 5:
                atualizar_estatisticas(produtos,
                                       valor_total,
                                       precomaior,
                                       precomenor);

                if(!produtos.empty()){
                    cout<<"Valor total: "<<valor_total<<endl;
                    cout<<"Preco maior: "<<precomaior<<endl;
                    cout<<"Preco menor: "<<precomenor<<endl;
                }
                break;

            case 6:
                filtrar_produtos(produtos);
                break;

            case 7:
                exportar_dados(produtos);
                break;

            case 8:
                importar_dados(produtos);
                break;

            case 9:
                produto_mais_caro(produtos);
                break;

            case 10:
                cout<<"Produtos com stock baixo: "
                    <<contar_stock_baixo(produtos)
                    <<endl;
                break;
        }

    }while(opcao!=0);

    return 0;
}
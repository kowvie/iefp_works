#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct{
    char nome[50];
    float preco;
    int quantidade;
} Produto;

int login(){
    char utilizador[50];
    char password[50];

    printf("Utilizador: ");
    fgets(utilizador, 50, stdin);
    utilizador[strcspn(utilizador, "\n")] = 0;

    printf("Password: ");
    fgets(password, 50, stdin);
    password[strcspn(password, "\n")] = 0;

    for(int i=0; utilizador[i]!='\0'; i++)
        utilizador[i] = tolower(utilizador[i]);

    if(strcmp(utilizador,"admin")==0 && strcmp(password,"1234")==0)
        return 1;

    return 0;
}

void atualizar_estatisticas(Produto *produtos, int tamanho,
                            float *valor_total,
                            float *precomaior,
                            float *precomenor){

    *valor_total = 0;

    if(tamanho == 0){
        *precomaior = 0;
        *precomenor = 0;
        return;
    }

    *precomaior = *precomenor = produtos[0].preco;

    for(int i=0;i<tamanho;i++){

        *valor_total += produtos[i].preco * produtos[i].quantidade;

        if(produtos[i].preco > *precomaior)
            *precomaior = produtos[i].preco;

        if(produtos[i].preco < *precomenor)
            *precomenor = produtos[i].preco;
    }
}

void registar_produtos(Produto *produtos, int tamanho){

    for(int i=0;i<tamanho;i++){

        printf("\nProduto %d\n", i+1);

        printf("Nome do produto: ");
        fgets(produtos[i].nome,50,stdin);
        produtos[i].nome[strcspn(produtos[i].nome,"\n")] = 0;

        printf("Preco: ");
        while(scanf("%f",&produtos[i].preco)!=1 || produtos[i].preco<=0){
            printf("Erro! Introduza um preco valido: ");
            while(getchar()!='\n');
        }

        printf("Quantidade: ");
        while(scanf("%d",&produtos[i].quantidade)!=1 || produtos[i].quantidade<0){
            printf("Erro! Introduza quantidade valida: ");
            while(getchar()!='\n');
        }

        while(getchar()!='\n');
    }
}

void listar_produtos(Produto *produtos, int tamanho){

    if(tamanho==0){
        printf("Nao existem produtos!\n");
        return;
    }

    printf("\nLISTA DE PRODUTOS\n");

    for(int i=0;i<tamanho;i++){
        printf("[%d] %s | Preco: %.2f | Quantidade: %d\n",
        i,
        produtos[i].nome,
        produtos[i].preco,
        produtos[i].quantidade);
    }
}

void eliminar_produto(Produto *produtos, int *tamanho){

    if(*tamanho==0){
        printf("Nao existem produtos!\n");
        return;
    }

    listar_produtos(produtos,*tamanho);

    int indice;

    printf("Indice do produto a eliminar: ");

    while(scanf("%d",&indice)!=1 || indice<0 || indice>=*tamanho){
        printf("Indice invalido: ");
        while(getchar()!='\n');
    }

    while(getchar()!='\n');

    for(int i=indice;i<*tamanho-1;i++)
        produtos[i]=produtos[i+1];

    (*tamanho)--;

    printf("Produto removido!\n");
}

void atualizar_produto(Produto *produtos, int tamanho){

    if(tamanho==0){
        printf("Nao existem produtos!\n");
        return;
    }

    listar_produtos(produtos,tamanho);

    int indice;

    printf("Indice do produto a atualizar: ");

    while(scanf("%d",&indice)!=1 || indice<0 || indice>=tamanho){
        printf("Indice invalido: ");
        while(getchar()!='\n');
    }

    while(getchar()!='\n');

    printf("Novo nome: ");
    fgets(produtos[indice].nome,50,stdin);
    produtos[indice].nome[strcspn(produtos[indice].nome,"\n")] = 0;

    printf("Novo preco: ");
    while(scanf("%f",&produtos[indice].preco)!=1){
        printf("Preco invalido: ");
        while(getchar()!='\n');
    }

    printf("Nova quantidade: ");
    while(scanf("%d",&produtos[indice].quantidade)!=1){
        printf("Quantidade invalida: ");
        while(getchar()!='\n');
    }

    while(getchar()!='\n');

    printf("Produto atualizado com sucesso!\n");
}

int main(){

    if(!login()){
        printf("Acesso negado!\n");
        return 1;
    }

    printf("Bem-vindo ao sistema!\n");

    int tamanho;

    printf("Quantos produtos deseja registar? ");

    while(scanf("%d",&tamanho)!=1 || tamanho<=0){
        printf("Valor invalido: ");
        while(getchar()!='\n');
    }

    while(getchar()!='\n');

    Produto *produtos = malloc(tamanho*sizeof(Produto));

    if(produtos==NULL){
        printf("Erro de memoria!\n");
        return 1;
    }

    registar_produtos(produtos,tamanho);

    float valor_total=0, precomaior=0, precomenor=0;

    atualizar_estatisticas(produtos,tamanho,&valor_total,&precomaior,&precomenor);

    int opcao;

    do{

        printf("\n--- MENU ---\n");
        printf("1 - Listar produtos\n");
        printf("2 - Adicionar produto\n");
        printf("3 - Eliminar produto\n");
        printf("4 - Atualizar produto\n");
        printf("5 - Estatisticas\n");
        printf("0 - Sair\n");
        printf("Opcao: ");

        while(scanf("%d",&opcao)!=1){
            printf("Opcao invalida: ");
            while(getchar()!='\n');
        }

        while(getchar()!='\n');

        switch(opcao){

            case 1:
                listar_produtos(produtos,tamanho);
                break;

            case 2:{
                tamanho++;

                Produto *temp = realloc(produtos, tamanho*sizeof(Produto));

                if(temp==NULL){
                    printf("Erro de memoria!\n");
                    tamanho--;
                    break;
                }

                produtos=temp;

                printf("Novo produto:\n");
                registar_produtos(&produtos[tamanho-1],1);

                atualizar_estatisticas(produtos,tamanho,&valor_total,&precomaior,&precomenor);

                break;
            }

            case 3:
                eliminar_produto(produtos,&tamanho);
                atualizar_estatisticas(produtos,tamanho,&valor_total,&precomaior,&precomenor);
                break;

            case 4:
                atualizar_produto(produtos,tamanho);
                atualizar_estatisticas(produtos,tamanho,&valor_total,&precomaior,&precomenor);
                break;

            case 5:
                if(tamanho>0){
                    printf("Valor total do stock: %.2f\n",valor_total);
                    printf("Preco mais alto: %.2f\n",precomaior);
                    printf("Preco mais baixo: %.2f\n",precomenor);
                }
                else{
                    printf("Nao existem produtos registados!\n");
                }
                break;

            case 0:
                printf("A terminar programa...\n");
                break;

            default:
                printf("Opcao invalida!\n");
        }

    }while(opcao!=0);

    free(produtos);

    return 0;
}
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

    for(int i = 0; utilizador[i] != '\0'; i++)
        utilizador[i] = tolower(utilizador[i]);

    if(strcmp(utilizador, "admin") == 0 &&
       strcmp(password, "1234") == 0)
        return 1;

    return 0;
}

int pedir_numero_produtos(){
    int tamanho;

    printf("Indique quantos produtos pretende registar:\n");

    while(scanf("%d", &tamanho) != 1 || tamanho <= 0){
        printf("Erro! Introduza um numero inteiro positivo:\n");
        while(getchar() != '\n');
    }

    while(getchar() != '\n');
    return tamanho;
}

void registar_produtos(Produto *produtos, int tamanho,
                       float *valor_total,
                       float *precomaior,
                       float *precomenor){

    for(int i = 0; i < tamanho; i++){

        printf("\nProduto %d\n", i + 1);

        printf("Nome do produto:\n");
        fgets(produtos[i].nome, 50, stdin);
        produtos[i].nome[strcspn(produtos[i].nome, "\n")] = 0;

        printf("Preco do produto:\n");
        while(scanf("%f", &produtos[i].preco) != 1 || produtos[i].preco <= 0){
            printf("Erro! Introduza um preco valido (>0):\n");
            while(getchar() != '\n');
        }

        printf("Quantidade em stock:\n");
        while(scanf("%d", &produtos[i].quantidade) != 1 || produtos[i].quantidade < 0){
            printf("Erro! Introduza uma quantidade valida (>=0):\n");
            while(getchar() != '\n');
        }

        while(getchar() != '\n');

        *valor_total += produtos[i].preco * produtos[i].quantidade;

        if(i == 0){
            *precomaior = produtos[i].preco;
            *precomenor = produtos[i].preco;
        } else {
            if(produtos[i].preco > *precomaior)
                *precomaior = produtos[i].preco;

            if(produtos[i].preco < *precomenor)
                *precomenor = produtos[i].preco;
        }
    }
}

void listar_produtos(Produto *produtos, int tamanho){
    printf("\nLISTA DE PRODUTOS\n");
    for(int i = 0; i < tamanho; i++){
        printf("[%d] Produto: %s | Preco: %.2f | Quantidade: %d\n",
               i,
               produtos[i].nome,
               produtos[i].preco,
               produtos[i].quantidade);
    }
}

void eliminar_produto(Produto *produtos, int *tamanho,
                      float *valor_total,
                      float *precomaior,
                      float *precomenor){

    if(*tamanho == 0){
        printf("Nao existem produtos registados!\n");
        return;
    }

    listar_produtos(produtos, *tamanho);

    int indice;

    printf("Indique o indice do produto a eliminar (0 a %d): ",
           *tamanho - 1);

    while(scanf("%d", &indice) != 1 ||
          indice < 0 || indice >= *tamanho){
        printf("Indice invalido! Introduza um valor entre 0 e %d: ",
               *tamanho - 1);
        while(getchar() != '\n');
    }

    while(getchar() != '\n');

    for(int i = indice; i < *tamanho - 1; i++){
        produtos[i] = produtos[i + 1];
    }

    (*tamanho)--;

    printf("Produto removido com sucesso!\n");

    if(*tamanho == 0){
        *valor_total = 0;
        *precomaior = 0;
        *precomenor = 0;
        return;
    }

    *valor_total = 0;

    for(int i = 0; i < *tamanho; i++){
        *valor_total += produtos[i].preco * produtos[i].quantidade;

        if(i == 0){
            *precomaior = produtos[i].preco;
            *precomenor = produtos[i].preco;
        } else {
            if(produtos[i].preco > *precomaior)
                *precomaior = produtos[i].preco;

            if(produtos[i].preco < *precomenor)
                *precomenor = produtos[i].preco;
        }
    }
}

int main(){

    if(!login()){
        printf("Acesso negado!\n");
        return 1;
    }

    printf("Bem-vindo(a) ao sistema!\n");

    int tamanho;
    float valor_total = 0.0;
    float precomaior = 0.0;
    float precomenor = 0.0;

    tamanho = pedir_numero_produtos();

    Produto *produtos = malloc(tamanho * sizeof(Produto));

    if(produtos == NULL){
        printf("Erro na alocacao de memoria!\n");
        return 1;
    }

    registar_produtos(produtos, tamanho,
                      &valor_total,
                      &precomaior,
                      &precomenor);

    int opcao;

    printf("\nDeseja remover algum produto? (1-Sim | 0-Nao): ");
    scanf("%d", &opcao);
    while(getchar()!='\n');

    if(opcao == 1){
        eliminar_produto(produtos, &tamanho,
                         &valor_total,
                         &precomaior,
                         &precomenor);
    }

    listar_produtos(produtos, tamanho);

    printf("\nValor total do stock: %.2f euros\n", valor_total);
    printf("Preco mais alto: %.2f euros\n", precomaior);
    printf("Preco mais baixo: %.2f euros\n", precomenor);

    free(produtos);

    return 0;
}
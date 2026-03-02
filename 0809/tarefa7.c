#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct{
    char nome[50];
    float preco;
    int quantidade;
} Produto;

int pedir_numero_produtos(){
    int tamanho;
    printf("Indique quantos produtos pretende registar:\n");

    while(scanf("%d", &tamanho) != 1 || tamanho <= 0){
        printf("Erro! Introduza um numero inteiro positivo:\n");
        while(getchar() != '\n');
    }

    while(getchar() != '\n'); // limpar buffer
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
            printf("Erro! Introduza um preco valido (maior que 0):\n");
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
        printf("Produto: %s | Preco: %.2f | Quantidade: %d\n",
               produtos[i].nome,
               produtos[i].preco,
               produtos[i].quantidade);
    }
}

int main(){

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

    listar_produtos(produtos, tamanho);

    printf("\nValor total do stock: %.2f euros\n", valor_total);
    printf("Preco mais alto: %.2f euros\n", precomaior);
    printf("Preco mais baixo: %.2f euros\n", precomenor);

    free(produtos);

    return 0;
}
#include <stdio.h>
#include <stdlib.h>

typedef struct{
    char nome[50];
    float preco;
    int quantidade;
} Produto;

int     pedir_numero_produtos(){
    int tamanho;
    printf("Indique quantos produtos pretende registar: ");
    scanf("%d", &tamanho);
    return tamanho;
}

void    registar_produtos(Produto *produtos, int tamanho, float *valor_total){
    for(int i = 0; i < tamanho; i++){
        
        printf("\nProduto %d\n", i + 1);

        printf("Nome do produto: ");
        scanf("%49s", produtos[i].nome);

        printf("Preco do produto: ");
        while(scanf("%f", &produtos[i].preco) != 1){
            printf("Erro! O preco deve ser um numero real: ");
            while(getchar() != '\n');
        }

        printf("Quantidade em stock: ");
        while(scanf("%d", &produtos[i].quantidade) != 1){
            printf("Erro! A quantidade deve ser um numero inteiro: ");
            while(getchar() != '\n');
        }

        *valor_total += produtos[i].preco * produtos[i].quantidade;
    }
}

void    listar_produtos(Produto *produtos, int tamanho){
    printf("\n LISTA DE PRODUTOS \n");
    
    for(int i = 0; i < tamanho; i++){
        printf("Produto: %s | Preco: %.2f | Quantidade: %d\n",
               produtos[i].nome,
               produtos[i].preco,
               produtos[i].quantidade);
    }
}


int     main()
{
    int tamanho;
    float valor_total = 0.0;

    tamanho = pedir_numero_produtos();

    Produto *produtos = malloc(tamanho * sizeof(Produto));

    if(produtos == NULL){
        printf("Erro\n");
        return 1;
    }

    registar_produtos(produtos, tamanho, &valor_total);

    listar_produtos(produtos, tamanho);

    printf("\nValor total do stock: %.2f euros\n", valor_total);

    free(produtos);

    return 0;
}

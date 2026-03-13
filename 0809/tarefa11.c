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

int pedir_numero_produtos(){
    int tamanho;

    printf("Indique quantos produtos pretende registar:\n");

    while(scanf("%d",&tamanho)!=1 || tamanho<=0){
        printf("Erro! Introduza um numero inteiro positivo: ");
        while(getchar()!='\n');
    }

    while(getchar()!='\n');
    return tamanho;
}

void atualizar_estatisticas(Produto *produtos, int tamanho,
                            float *valor_total,
                            float *precomaior,
                            float *precomenor){

    *valor_total = 0;

    if(tamanho==0){
        *precomaior = *precomenor = 0;
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

        printf("Nome do produto %d:\n", i+1);
        fgets(produtos[i].nome,50,stdin);
        produtos[i].nome[strcspn(produtos[i].nome,"\n")] = 0;

        printf("Preco:\n");
        while(scanf("%f",&produtos[i].preco)!=1 || produtos[i].preco<=0){
            printf("Erro! Introduza um preco valido: ");
            while(getchar()!='\n');
        }

        printf("Quantidade:\n");
        while(scanf("%d",&produtos[i].quantidade)!=1 || produtos[i].quantidade<0){
            printf("Erro! Introduza quantidade valida: ");
            while(getchar()!='\n');
        }

        while(getchar()!='\n');
    }
}

void listar_produtos(Produto *produtos, int tamanho){

    if(tamanho==0){
        printf("Nao existem produtos registados!\n");
        return;
    }

    printf("\nLISTA DE PRODUTOS:\n");

    for(int i=0;i<tamanho;i++){
        printf("[%d] %s | Preco: %.2f | Quantidade: %d\n",
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

    if(*tamanho==0){
        printf("Nao existem produtos!\n");
        return;
    }

    listar_produtos(produtos,*tamanho);

    int indice;

    printf("Indice do produto a eliminar (0 a %d): ", *tamanho-1);

    while(scanf("%d",&indice)!=1 || indice<0 || indice>=*tamanho){
        printf("Indice invalido: ");
        while(getchar()!='\n');
    }

    while(getchar()!='\n');

    for(int i=indice;i<*tamanho-1;i++)
        produtos[i]=produtos[i+1];

    (*tamanho)--;

    atualizar_estatisticas(produtos,*tamanho,
                           valor_total,precomaior,precomenor);

    printf("Produto removido com sucesso!\n");
}

void atualizar_produto(Produto *produtos, int tamanho,
                       float *valor_total,
                       float *precomaior,
                       float *precomenor){

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

    printf("Novo nome:\n");
    fgets(produtos[indice].nome,50,stdin);
    produtos[indice].nome[strcspn(produtos[indice].nome,"\n")] = 0;

    printf("Novo preco:\n");
    while(scanf("%f",&produtos[indice].preco)!=1){
        printf("Erro! Introduza preco valido: ");
        while(getchar()!='\n');
    }

    printf("Nova quantidade:\n");
    while(scanf("%d",&produtos[indice].quantidade)!=1){
        printf("Erro! Introduza quantidade valida: ");
        while(getchar()!='\n');
    }

    while(getchar()!='\n');

    atualizar_estatisticas(produtos,tamanho,
                           valor_total,precomaior,precomenor);

    printf("Produto atualizado com sucesso!\n");
}

void filtrar_produtos(Produto *produtos, int tamanho){

    if(tamanho==0){
        printf("Nao existem produtos!\n");
        return;
    }

    float preco_min;

    printf("Preco minimo para filtrar: ");

    while(scanf("%f",&preco_min)!=1){
        printf("Valor invalido: ");
        while(getchar()!='\n');
    }

    while(getchar()!='\n');

    int encontrado = 0;

    for(int i=0;i<tamanho;i++){
        if(produtos[i].preco >= preco_min){
            printf("%s | %.2f | %d\n",
                   produtos[i].nome,
                   produtos[i].preco,
                   produtos[i].quantidade);
            encontrado = 1;
        }
    }

    if(!encontrado)
        printf("Nenhum produto encontrado.\n");
}

void exportar_dados(Produto *produtos, int tamanho){

    FILE *f = fopen("produtos_backup.txt","w");

    if(f==NULL){
        printf("Erro ao criar ficheiro!\n");
        return;
    }

    for(int i=0;i<tamanho;i++){
        fprintf(f,"%s %.2f %d\n",
                produtos[i].nome,
                produtos[i].preco,
                produtos[i].quantidade);
    }

    fclose(f);

    printf("Backup exportado com sucesso!\n");
}

int importar_dados(Produto *produtos){

    FILE *f = fopen("produtos_backup.txt","r");

    if(f==NULL){
        printf("Ficheiro nao encontrado!\n");
        return 0;
    }

    int i=0;

    while(fscanf(f,"%s %f %d",
          produtos[i].nome,
          &produtos[i].preco,
          &produtos[i].quantidade)==3)
        i++;

    fclose(f);

    printf("Dados importados com sucesso!\n");

    return i;
}

int main(){

    if(!login()){
        printf("Acesso negado!\n");
        return 1;
    }

    printf("Bem-vindo(a)!\n");

    float valor_total=0, precomaior=0, precomenor=0;

    int tamanho = pedir_numero_produtos();

    Produto *produtos = malloc(tamanho*sizeof(Produto));

    if(produtos==NULL){
        printf("Erro na alocacao de memoria!\n");
        return 1;
    }

    registar_produtos(produtos,tamanho);

    atualizar_estatisticas(produtos,tamanho,
                           &valor_total,&precomaior,&precomenor);

    int opcao;

    do{

        printf("\n1 - Listar Produtos\n");
        printf("2 - Adicionar Produto\n");
        printf("3 - Eliminar Produto\n");
        printf("4 - Atualizar Produto\n");
        printf("5 - Estatisticas\n");
        printf("6 - Filtrar Produtos\n");
        printf("7 - Exportar Backup\n");
        printf("8 - Importar Backup\n");
        printf("0 - Terminar Programa\n");
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

        case 2:
            tamanho++;
            registar_produtos(&produtos[tamanho-1],1);
            atualizar_estatisticas(produtos,tamanho,
                                   &valor_total,&precomaior,&precomenor);
            break;

        case 3:
            eliminar_produto(produtos,&tamanho,
                             &valor_total,&precomaior,&precomenor);
            break;

        case 4:
            atualizar_produto(produtos,tamanho,
                              &valor_total,&precomaior,&precomenor);
            break;

        case 5:
            if(tamanho>0){
                printf("Valor total: %.2f\n",valor_total);
                printf("Preco maior: %.2f\n",precomaior);
                printf("Preco menor: %.2f\n",precomenor);
            } else {
                printf("Nao existem produtos!\n");
            }
            break;

        case 6:
            filtrar_produtos(produtos,tamanho);
            break;

        case 7:
            exportar_dados(produtos,tamanho);
            break;

        case 8:
            tamanho = importar_dados(produtos);
            atualizar_estatisticas(produtos,tamanho,
                                   &valor_total,&precomaior,&precomenor);
            break;

        case 0:
            printf("A terminar o programa...\n");
            break;

        default:
            printf("Opcao invalida!\n");
        }

    }while(opcao!=0);

    free(produtos);

    return 0;
}
//parte1 (&&)
#include <stdio.h>

int main()
{
    float temperatura;

    printf("Introduza a temperatura: ");
    scanf("%f", &temperatura);

    if (temperatura >= 0 && temperatura <= 40) {
        printf("Temperatura dentro do intervalo permitido!\n");
    } else {
        printf("Temperatura fora do intervalo!\n");
    }

    return 0;
}

//parte2 (||)
#include <stdio.h>

int main()
{
    int numero;

    printf("Introduza um numero: ");
    scanf("%d", &numero);

    if (numero < 1 || numero > 50) {
        printf("Numero invalido!\n");
    } else {
        printf("Numero valido!\n");
    }

    return 0;
}

//parte3 (login)
#include <stdio.h>
#include <string.h>

int login() {

    char utilizador[50];
    char password[50];

    printf("Utilizador: ");
    fgets(utilizador, 50, stdin);
    utilizador[strcspn(utilizador, "\n")] = 0;

    printf("Password: ");
    fgets(password, 50, stdin);
    password[strcspn(password, "\n")] = 0;

    if (strcmp(utilizador, "admin") == 0 &&
        strcmp(password, "1234") == 0) {
        return 1;
    }

    return 0;
}

int main()
{
    if (!login()) {
        printf("Acesso negado! Programa terminado.\n");
        return 1;
    }

    printf("Acesso validado!\n");
    printf("Bem-vindo(a) ao sistema!\n");

    int numero;

    printf("Introduza um numero positivo: ");
    scanf("%d", &numero);

    if (numero > 0) {
        printf("Numero valido!\n");
    } else {
        printf("Numero invalido!\n");
    }

    return 0;
}
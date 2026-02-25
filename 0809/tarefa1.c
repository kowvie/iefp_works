#include <stdio.h>

int main()
{
    float saldo;
    float valor1;
    float valor2;
    float valor3;
    float res;

    printf("Introduza o saldo total: ");
    scanf("%f", &saldo);

    printf("Introduza o primeiro valor: ");
    scanf("%f", &valor1);

    printf("Introduza o segundo valor: ");
    scanf("%f", &valor2);

    printf("Introduza o terceiro valor: ");
    scanf("%f", &valor3);

    res = saldo - valor1 - valor2 - valor3;

    printf("Resultado: %.2f\n", res);

    if (res > 0)
    {
        printf("Positivo! \n");
    }
    else
    {
        printf("Negativo! \n");
    }
    return 0;
}
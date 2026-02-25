#include <stdio.h>

float subtrair(float num1, float num2)
{
    return (num1 - num2);
}


float multiplicar(float valor, float taxa)
{
    return (valor * taxa);
}

int main()
 {

    float num1, num2;
    float res_sub, res_mult;

    
    printf("Introduza o primeiro valor: ");
    scanf("%f", &num1);

    printf("Introduza o segundo valor: ");
    scanf("%f", &num2);

    res_sub = subtrair(num1, num2);

    printf("\nresultado da subtracao: %.2f\n", res_sub);


    if (res_sub > 0) 
    {
        printf("Valor positivo.\n");

        res_mult = multiplicar(res_sub, 10);
        printf("Multiplicado por 10, o valor sera: %.2f\n", res_mult);
    }
    else {
        printf("Valor negativo.\n");
    }

    return 0;
}
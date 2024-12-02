#include <stdio.h>
#include <math.h>

double f(double x) {
    if (x >= 0 && x <= 0.25) {
        return exp(sin(x));
    } else if (x > 0.25 && x <= 0.5) {
        return exp(x) - 1/sqrt(3.0);
    } else {
        return -1;
    }
}

int main() {
    double x;
    printf("Введите значение x: ");
    scanf("%lf", &x);

    double result = f(x);
    if (result != 1) {
        printf("f(%.2f) = %.5f\n", x, result);
    } else {
        printf("x вне допустимого диапазона\n");
    }
    return 0;
}
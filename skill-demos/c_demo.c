#include <stdio.h>

int main(void) {
    int values[] = {10, 20, 30, 40, 50};
    int n = sizeof(values) / sizeof(values[0]);
    int sum = 0;

    for (int i = 0; i < n; ++i) {
        sum += values[i];
    }

    printf("Count: %d\n", n);
    printf("Mean: %.2f\n", (double)sum / n);
    return 0;
}

#include <stdio.h>
#include <stdlib.h>

void separateArray(int *arr, int size, int *negatives, int *negCount, int *positives, int *posCount) {
    *negCount = 0;
    *posCount = 0;
    for (int i = 0; i < size; i++) {
        if (arr[i] < 0) {
            (negCount)++;
        } else if (arr[i] > 0){
            (*posCount)++;
        }
    }

    *negatives = (int *)malloc((*negCount) * sizeof(int));
    *positives = (int *)malloc((*posCount) * sizeof(int));

    if (*negatives == NULL || *positives == NULL) {
        fprintf(stderr, "Ошибка выделения памяти");
        exit(1);
    }
    
    }

long int sum(int* A, int ASize) {
    long int res = 0;
    while (ASize--) res += *A++;
    return res;
}

int max(int a, int b) {
    return a > b ? a : b;
}

int maxRotateFunction(int* A, int ASize){
    long int S = sum(A, ASize);
    long int F = 0;
    int i, res;
    for (i = 0; i < ASize; i++) {
        F += A[i] * i;
    }
    res = F;
    for (i = 0; i < ASize - 1; i++) {
        F = F - S + (long)A[i] * ASize;
        res = max(F, res);
    }
    return res;
}

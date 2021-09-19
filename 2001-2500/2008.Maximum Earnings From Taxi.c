#define MAX(x, y) ((x) > (y)) ? (x) : (y)

int compare(const void* a, const void* b) {
    int n1, n2;
    for (int i = 0; i < 3; i++) {
        n1 = (*(int**)a)[i];
        n2 = (*(int**)b)[i];
        if (n1 != n2) break;
    }
    return n1 - n2;
}

long long maxTaxiEarnings(int n, int** rides, int ridesSize, int* ridesColSize){
    qsort(rides, ridesSize, sizeof(int*), compare);
    long long res = 0, cur = 0;
    long long* tips = (long long*)calloc(n + 1, sizeof(long long));
    for (int i = 0; i < ridesSize; i++) {
        if (i != 0) {
            for (int j = rides[i - 1][0] + 1; j <= rides[i][0]; j++) {
                cur = MAX(cur, tips[j]);
            }
        }
        int* ride = rides[i];
        tips[ride[1]] = MAX(tips[ride[1]], ride[1] - ride[0] + ride[2] + cur);
        res = MAX(res, tips[ride[1]]);
    }
    return res;
}


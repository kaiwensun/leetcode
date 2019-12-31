int* data;

int find(int x) {
    return data[x] == x ? x : (data[x] = find(data[x]));
}

void merge(int x, int y) {
    if (find(x) != find(y)) data[find(x)] = find(y);
}

int count(int N) {
    int cnt = 0;
    for (int i = 0; i < N; i++)
        cnt += data[i] == i;
    return cnt;
}

int findCircleNum(int** M, int N, int* MColSize){
    data = malloc(N * sizeof(int));
    for (int i = 0; i < N; i++)
        data[i] = i;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            if (M[i][j])
                merge(i, j);
    int res = count(N);
    free(data);
    return res;
}

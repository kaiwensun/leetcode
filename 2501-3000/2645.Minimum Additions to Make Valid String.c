int addMinimum(char * word){
    int res = 0;
    int wanted = 0;
    char* c = word;
    bool ended = false;
    while (true) {
        int diff = (*c - 'a' + 3 - wanted) % 3;
        printf("%d\n", diff);
        res += diff;
        wanted += diff + 1;
        wanted %= 3;
        if (ended) {
            break;
        }
        if (!*(++c)) {
            ended = true;
            *c = 'a';
        };
    }
    *c = '\0';
    return res;
}


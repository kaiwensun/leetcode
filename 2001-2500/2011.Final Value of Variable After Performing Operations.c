int finalValueAfterOperations(char ** operations, int operationsSize){
    int x = 0;
    for (int i = 0; i < operationsSize; i++) {
        x += operations[i][1] == '+' ? 1 : -1;
    }
    return x;
}


bool isUgly(int num){
    if (num < 1) return false;
    int factors[] = {2, 3, 5};
    for (int i = 0; i < 3; i++) {
        while (!(num % factors[i])) num /= factors[i];
    }
    return num == 1;
}

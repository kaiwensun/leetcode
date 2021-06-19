int leastMinutes(int n){
    n--;
    int res = 1;
    while (n != 0) {
        n >>= 1;
        res++;
    }
    return res;
}


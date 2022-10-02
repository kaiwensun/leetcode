int calc_gcd(int a, int b) {
    if (a > b) {
        int tmp = a; a = b; b = tmp;
    }
    while (a != 0) {
        b %= a;
        int tmp = a; a = b; b = tmp;
    }
    return b;
}

int commonFactors(int a, int b){
    int res = 0, gcd = calc_gcd(a, b);
    for (int i = 1; i <= gcd; i++) {
        if (gcd % i == 0) {
            res++;
        }
    }
    return res;
}


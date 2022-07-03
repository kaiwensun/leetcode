const int MOD = 1000000007;
const int MAX = 1000;
long plan[1000] = {1};

int peopleAwareOfSecret(int n, int delay, int forget){
    long spreaders = 0;
    long res = 1;
    for (int i = 0; i < n; i++) {
        if (i - delay >= 0) {
            spreaders += plan[i - delay];
            spreaders %= MOD;
        }
        if (i - forget >= 0) {
            spreaders -= plan[i - forget];
            spreaders %= MOD;
            res -= plan[i - forget];
        }
        plan[i] = i == 0 ? 1 : spreaders;
        res += spreaders;
        res %= MOD;
    }
    return (res + MOD) % MOD;
    
}


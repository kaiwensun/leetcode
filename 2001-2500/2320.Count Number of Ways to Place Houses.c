unsigned long long MOD = 1000000007;
int countHousePlacements(int n){
    unsigned long long taken = 0, not_taken = 1;
    for (int i = 0; i <= n; i++) {
        unsigned long long tmp = (taken + not_taken) % MOD;
        taken = not_taken;
        not_taken = tmp;
    }
    return (not_taken * not_taken) % MOD;
}


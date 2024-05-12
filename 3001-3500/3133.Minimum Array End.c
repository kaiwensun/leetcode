long long minEnd(int n, int x) {
    long long insert_bit_posi = 1;
    long long res = x;
    n -= 1;
    while (n) {
        long long inserted_bit = n & 1;
        n >>= 1;
        while (insert_bit_posi & res) {
            insert_bit_posi <<= 1;
        }
        res |= inserted_bit ? insert_bit_posi : 0;
        insert_bit_posi <<= 1;
    }
    return res;
}


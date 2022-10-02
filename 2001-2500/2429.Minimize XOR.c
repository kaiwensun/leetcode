int minimizeXor(int num1, int num2){
    int bitCnt = 0;
    while (num2 != 0) {
        bitCnt++;
        num2 &= (num2 - 1);
    }
    int res = 0;
    while (num1 != 0 && bitCnt != 0) {
        unsigned int mask = num1 >> 1;
        for (int shift = 1; shift < 32; shift<<=1) {
            mask |= mask >> shift;
        }
        mask += 1;
        res |= mask;
        num1 ^= mask;
        bitCnt--;
    }
    unsigned int mask = 1;
    while (bitCnt != 0) {
        if ((mask & res) == 0) {
            bitCnt--;
            res |= mask;
        }
        mask <<= 1;
    }
    return res;
}


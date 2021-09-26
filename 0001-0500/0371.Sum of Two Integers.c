int getSum(int a, int b){
    int and = a & b;
    int or = a | b;
    int res = 0;
    unsigned mask = 1;
    unsigned carry = 0;
    while (true) {
        res |= (a & mask) ^ (b & mask) ^ carry;
        carry = ((and | (or & carry)) & mask) << 1;
        if (mask == ~((unsigned)(-1) >> 1)) {
            break;
        }
        mask <<= 1;
    }
    return res | carry;
}


int add(int a, int b){
    unsigned ua = (unsigned) a;
    unsigned ub = (unsigned) b;
    while (ua != 0) {
        unsigned carry = (ua & ub) << 1;
        unsigned sum = ua ^ ub;
        ua = carry;
        ub = sum;
    }
    return (int)ub;
}


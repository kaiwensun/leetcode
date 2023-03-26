#define MIN(a,b) ((a) < (b) ? (a) : (b))

int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k){
    int res = 0;
    res += MIN(numOnes, k);
    k -= MIN(numOnes, k);
    k -= MIN(numZeros, k);
    res -= MIN(numNegOnes, k);
    return res;
}


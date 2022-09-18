class Solution {
public:
    int smallestEvenMultiple(int n) {
        return n << (n & 1);
    }
};


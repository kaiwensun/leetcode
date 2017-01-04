class Solution {
public:
    int hammingDistance(int x, int y) {
        int exc = x^y;
        int dist = 0;
        while(exc){
            dist++;
            exc &= (exc-1);
        }
        return dist;
    }
};

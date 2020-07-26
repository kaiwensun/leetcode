class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int total = 0;
        for(int shift=0;shift<31;shift++){
            int mask = 1<<shift;
            int bitSet = 0;
            for(auto num : nums){
                bitSet+=(num&mask)?1:0;
            }
            total+=bitSet*(nums.size()-bitSet);
        }
        return total;
    }
};

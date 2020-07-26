/**
 *Result:
 * 16 / 16 test cases passed.
 * Status: Accepted
 * Runtime: 26 ms
 * Your runtime beats 48.33% of cpp submissions.
 *Date:
 * 10/2/2016
 */
class NumArray {
private:
    int* left = NULL;
public:
    NumArray(vector<int> &nums) {
        left = new int[nums.size()+1];
        left[0] = 0;
        for(int i=0;i<nums.size();i++){
            left[i+1] = left[i]+nums[i];
        }
    }

    int sumRange(int i, int j) {
        return left[j+1]-left[i];
    }
};


// Your NumArray object will be instantiated and called as such:
// NumArray numArray(nums);
// numArray.sumRange(0, 1);
// numArray.sumRange(1, 2);

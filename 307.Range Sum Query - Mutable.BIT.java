/**
 *Basic idea:
 * Binary Index Tree (BIT).
 * For tutorial about BIT, see https://www.youtube.com/watch?v=CWDQJGaN1gY
 *Result:
 * 10 / 10 test cases passed.
 * Status: Accepted
 * Runtime: 8 ms
 * Your runtime beats 58.28% of java submissions.
 *Date:
 * 10/30/2016
 */ 

public class NumArray {
    private int[] bit;
    private int[] nums;
    public NumArray(int[] nums) {
        this.nums = new int[nums.length];
        bit = new int[nums.length+1];
        for(int i=0;i<nums.length;i++){
            update(i,nums[i]);
        }
    }

    void update(int i, int val) {
        if(i<0 || i>=nums.length)
            return;
        int add = val - nums[i];
        nums[i] = val;
        i = i+1;
        while(i<bit.length){
            bit[i]+=add;
            i = getNext(i);
        }
    }

    public int sumRange(int i, int j) {
        return getPrefix(j)-getPrefix(i-1);
    }
    
    private int getPrefix(int i){
        //i is inclusive.
        if(i>=nums.length){
            i = nums.length-1;
        }
        if(i<0){
            return 0;
        }
        int sum = 0;
        i = i+1;
        while(i!=0){
            sum+=bit[i];
            i = getParent(i);
        }
        return sum;
    }
    
    private int getParent(int x){
        return x-getLow(x);
    }
    private int getNext(int x){
        return x+getLow(x);
    }
    
    private int getLow(int x){
        return x & (-x);
    }
}


// Your NumArray object will be instantiated and called as such:
// NumArray numArray = new NumArray(nums);
// numArray.sumRange(0, 1);
// numArray.update(1, 10);
// numArray.sumRange(1, 2);

/**
 *Basic idea:
 * Reservoir Sampling and hashmap.
 *Result:
 * 13 / 13 test cases passed.
 * Status: Accepted
 * Runtime: 321 ms
 * Your runtime beats 75.37% of java submissions.
 *Date:
 * 10/27/2016
 */

public class Solution {
    private final Map<Integer,LinkedList<Integer>> map = new HashMap<>();
    private final Random rand = new Random();
    private final int[] nums;
    private final int SIZEBAR = 10000;
    public Solution(int[] nums) {
        this.nums = nums;
        if(this.nums.length<SIZEBAR){
            for(int i=0;i<nums.length;i++){
                if(!map.containsKey(nums[i])){
                    map.put(nums[i],new LinkedList<Integer>());
                }
                map.get(nums[i]).add(i);
            }
        }
    }
    
    public int pick(int target) {
        if(nums.length<SIZEBAR){
            List lst = map.get(target);
            if(lst==null)
                return -1;
            int id = rand.nextInt(lst.size());
            return (int)lst.get(id);
        }else{
            int cnt = 0;
            int index = -1;
            for(int i=0;i<nums.length;i++){
                if(nums[i]==target){
                    if(rand.nextInt(++cnt)==0){
                        index = i;
                    }
                }
            }
            return index;
        }
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */

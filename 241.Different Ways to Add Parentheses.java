/**
 * Basic Idea:
 *  Dynamic programming. dp[i][sz-j-1] is a linkedlist containing possible results for numbers ranging from index i to j (inclusive).
 * Result:
 *  25 / 25 test cases passed.
 *  Status: Accepted
 *  Runtime: 12 ms
 *  Your runtime beats 7.64% of javasubmissions.
 *Date:
 *  8/18/2016
 */
 
import java.util.Arrays;
public class Solution {
	private int[] nums;
	private String[] opts;
	private ArrayList<ArrayList<LinkedList<Integer>>> dp;
	int sz;
	public List<Integer> diffWaysToCompute(String input) {
        String[] strings = input.split("((?<=[\\+\\-\\*])|(?=[\\+\\-\\*]))");
        sz = strings.length/2+1;
        nums = new int[sz];
        opts = new String[sz-1];
        
        str2comp(strings);
        initDP();
        return result(0, sz-1);
    }
	private void initDP(){
		/* dp[i][sz-j-1] is a linkedlist containing possible results for numbers ranging from index i to j (inclusive). */
        dp = new ArrayList<ArrayList<LinkedList<Integer>>>(sz);
		for(int i=0;i<sz;i++){
			ArrayList<LinkedList<Integer>>row = new ArrayList<LinkedList<Integer>>(sz-i);
			for(int j=0;j<sz-i;j++)
				row.add(null);
			dp.add(row);
		}
		for(int i=0;i<sz;i++){
			LinkedList<Integer> oneEle = new LinkedList<>();
			oneEle.add(nums[i]);
			dp.get(i).set(sz-i-1, oneEle);
		}
			
	}
	private void str2comp(String[] strings){
		for(int i=0;i<strings.length/2;i++){
			nums[i]=Integer.parseInt(strings[i<<1]);
			opts[i]=strings[(i<<1)+1];
		}
		nums[nums.length-1] = Integer.parseInt(strings[strings.length-1]);
	}
	private LinkedList<Integer>result(int begin, int end){
		if(dp.get(begin).get(sz-end-1)!=null){
			return dp.get(begin).get(sz-end-1);
		}
		LinkedList<Integer>answer = new LinkedList<>();
		for(int split = begin;split<end;split++){
			LinkedList<Integer>left = result(begin, split);
			LinkedList<Integer>right = result(split+1, end);
			if(opts[split].equals("+"))
				for(Integer l:left)for(Integer r:right)answer.add(l+r);
			else if(opts[split].equals("-"))
				for(Integer l:left)for(Integer r:right)answer.add(l-r);
			else if(opts[split].equals("*"))
				for(Integer l:left)for(Integer r:right)answer.add(l*r);
		}
		dp.get(begin).set(sz-end-1, answer);
		return  answer;
	}
}

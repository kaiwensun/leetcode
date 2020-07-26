/**
 *Basic idea:
 * back tracking
 *Result:
 * 27 / 27 test cases passed.
 * Status: Accepted
 * Runtime: 5 ms
 * We are in the progress of updating the graph distribution. Please check the distribution again within weeks.
 *Date:
 * 9/9/2016
 */

public class Solution {
    private List<List<Integer>>res;
    public List<List<Integer>> combine(int n, int k) {
        res = new LinkedList<List<Integer>>();
        combine(n,1,k,new LinkedList<Integer>());
        return res;
    }
    private void combine(int n, int start, int k, LinkedList<Integer> path){
        if(k>n-start+1)
            return;
        if(k==0){
            res.add(new ArrayList(path));
            return;
        }
        for(int s = start;s<=n-k+1;s++){
            path.add(s);
            combine(n,s+1,k-1,path);
            path.removeLast();
        }
    }
}

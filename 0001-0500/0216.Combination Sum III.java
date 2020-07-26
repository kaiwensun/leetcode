/**
 *Result:
 * 18 / 18 test cases passed.
 * Status: Accepted
 * Runtime: 2 ms
 * Your runtime beats 13.56% of javasubmissions.
 *Date:
 * 9/3/2016
 */
public class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> res = combinationSum3(k,n,0);
        if(res==null)
            res = new LinkedList<List<Integer>>();
        return res;
    }
    public List<List<Integer>> combinationSum3(int k, int n, int starter){
        List<List<Integer>> res = new LinkedList<List<Integer>>();
        if(k==0){
            if(n==0){
                List<Integer> lst = new LinkedList<>();
                res.add(lst);
                return res;
            }
            else if(n>0)
                return res;     //return [] means n is too big
            else
                return null;    //return null means n is too small
        }
        
        for(int next = Math.min(9,n-(starter+starter+k)*(k-1)/2);next>starter;next--){
            List<List<Integer>>rtn = combinationSum3(k-1,n-next,next);
            if(rtn==null){
                continue;
            }
            if(rtn.size()==0){
                return res;
            }
            for(List<Integer> lst : rtn){
                lst.add(next);
            }
            res.addAll(rtn);
        }
        if(res.size()==0)
            return null;
        return res;
    }
}

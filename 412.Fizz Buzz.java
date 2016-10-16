/**
 *Result:
 * 8 / 8 test cases passed.
 * Status: Accepted
 * Runtime: 4 ms
 * Sorry. We do not have enough accepted submissions.
 *Date:
 * 10/15/2016
 */
public class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> res = new ArrayList<String>(n);
        for(int i=1;i<=n;i++){
            if(i%3==0){
                if(i%5==0)
                    res.add("FizzBuzz");
                else
                    res.add("Fizz");
            }
            else if(i%5==0){
                res.add("Buzz");
            }else{
                res.add(""+i);
            }
        }
        return res;
    }
}

/**
 *Result:
 * 18 / 18 test cases passed.
 * Status: Accepted
 * Runtime: 4 ms
 * Your runtime beats 83.80% of java submissions.
 *Date:
 * 12/11/2016
 */
class Solution {
    public String countAndSay(int n) {
    	StringBuilder res = new StringBuilder("1");
    	for(int i=1;i<n;i++){
    		res = read(res);
    	}
        return res.toString();
    }
    StringBuilder read(StringBuilder sb){
        StringBuilder res = new StringBuilder();
        int cnt = 0;
        for(int i=0;i<sb.length();i++){
        	cnt++;
            if(i+1==sb.length() || sb.charAt(i)!=sb.charAt(i+1)){
            	res.append(cnt).append(sb.charAt(i));
            	cnt = 0;
            }
        }
        return res;
    }
}

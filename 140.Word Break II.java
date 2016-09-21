/**
 *Basic idea:
 * DFS and Dynamic Programming.
 *Result:
 * 37 / 37 test cases passed.
 * Status: Accepted
 * Runtime: 8 ms
 * Your runtime beats 93.44% of java submissions.
 *Date:
 * 9/20/2016
 */
public class Solution {
    private ArrayList<LinkedList<String>> dp;
    private String s;
    private Set<String> wordDict;
    public List<String> wordBreak(String s, Set<String> wordDict) {
        dp = new ArrayList<LinkedList<String>>(s.length()+1);
        for(int i=0;i<=s.length();i++)
            dp.add(null);
        LinkedList<String> empty = new LinkedList<>();
        empty.add("");
        dp.set(0,empty);
        this.s = s;
        this.wordDict = wordDict;
        return getListEndedAt(s.length());
    }
    private LinkedList<String> getListEndedAt(int i){
        LinkedList rtn = dp.get(i);
        if(rtn!=null)
            return rtn;
        rtn = new LinkedList<String>();
        for(String word : wordDict){
            if(i-word.length()<0 || !s.substring(i-word.length(),i).equals(word))
                continue;
            for(String prev : getListEndedAt(i-word.length())){
                if(i==word.length()){
                    rtn.add(word);
                }
                else{
                    rtn.add(prev+" "+word);
                }
            }
        }
        dp.set(i,rtn);
        return rtn;
    }
}

/**
 *Basic idea:
 * DFS, check by sizes of words, and Dynamic Programming.
 *Result:
 * 37 / 37 test cases passed.
 * Status: Accepted
 * Runtime: 10 ms
 * Your runtime beats 87.74% of java submissions.
 *Date:
 * 9/21/2016
 */
public class Solution {
    private ArrayList<LinkedList<String>> dp;
    private String s;
    private Set<String> wordDict;
    private Set<Integer> wordSizes;
    public List<String> wordBreak(String s, Set<String> wordDict) {
        dp = new ArrayList<LinkedList<String>>(s.length()+1);
        for(int i=0;i<=s.length();i++)
            dp.add(null);
        LinkedList<String> empty = new LinkedList<>();
        empty.add("");
        dp.set(0,empty);
        
        wordSizes = new TreeSet<Integer>();
        for(String word : wordDict)
            wordSizes.add(word.length());
        
        this.s = s;
        this.wordDict = wordDict;
        return getListEndedAt(s.length());
    }
    private LinkedList<String> getListEndedAt(int i){
        LinkedList rtn = dp.get(i);
        if(rtn!=null)
            return rtn;
        rtn = new LinkedList<String>();
        for(int wordSize : wordSizes){
            if(i-wordSize<0)
                break;
            String substr = s.substring(i-wordSize,i);
            if(!wordDict.contains(substr))
                continue;
            for(String prev : getListEndedAt(i-wordSize)){
                if(i==wordSize)
                    rtn.add(substr);
                else
                    rtn.add(prev+" "+substr);
            }
        }
        dp.set(i,rtn);
        return rtn;
    }
}

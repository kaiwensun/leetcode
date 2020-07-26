/**
 *Result:
 * 14 / 14 test cases passed.
 * Status: Accepted
 * Runtime: 6 ms
 * Your runtime beats 10.14% of java submissions.
 *Date:
 * 11/7/2016
 */
public class Solution {
    
    public int minMutation(String start, String end, String[] bank) {
        //corner case
        if(start==null || end==null || start.length()!=end.length()){
            return -1;
        }
        if(bank==null || bank.length==0){
            if(start.equals(end)){
                return 0;
            }else{
                return -1;
            }
        }
        
        //make bank a hashmap
        Map<String,ArrayList<Integer>> s2dMap = new HashMap<String,ArrayList<Integer>>(bank.length);
        Map<ArrayList<Integer>,Set<String>> d2sMap = new HashMap<>();
        for(String str : bank){
            if(str.length()==start.length() && !str.equals(start)){
                ArrayList<Integer> digest = getDigest(str);
                s2dMap.put(str,digest);
                if(!d2sMap.containsKey(digest)){
                    d2sMap.put(digest,new HashSet<String>());
                }
                d2sMap.get(digest).add(str);
            }
        }
        if(!s2dMap.containsKey(end)){
            return -1;
        }
        if(s2dMap.containsKey(start)){
            return 0;
        }
        
        //current level of BFS
        Map<String,ArrayList<Integer>>curr = new HashMap<String,ArrayList<Integer>>();
        curr.put(start,getDigest(start));
        Map<String,ArrayList<Integer>>next = new HashMap<String,ArrayList<Integer>>();
        int step = 0;
        
        //BFS
        while(!curr.isEmpty() && !s2dMap.isEmpty()){
            for(Map.Entry<String,ArrayList<Integer>> entry : curr.entrySet()){
                String currstr = entry.getKey();
                ArrayList<Integer> digest = entry.getValue();
                for(int i=0;i<3;i++){
                	for(int j=i+1;j<4;j++){
	                    for(int delta : new int[]{-1,1}){
	                        digest.set(i,digest.get(i)+delta);
	                        digest.set(j,digest.get(j)-delta);
	                        Set<String> strs = d2sMap.get(digest);
	                        if(strs!=null){
	                            for(String str : strs){
	                                if(isAdjacent(str,currstr)){
	                                    if(str.equals(end)){
	                                        return step+1;
	                                    }
	                                    next.put(str,s2dMap.remove(str));
	                                    strs.remove(str);
	                                    if(strs.isEmpty()){
	                                        d2sMap.remove(digest);
	                                    }
	                                    break;
	                                }
	                            }
	                        }
	                        digest.set(i,digest.get(i)-delta);
	                        digest.set(j,digest.get(j)+delta);
	                    }
                        
                    }
                }
            }
            Map<String,ArrayList<Integer>>tmp = curr;curr = next;next = tmp;
            step++;
            next.clear();
        }
        return -1;
    }
    
    private boolean isAdjacent(String str1, String str2){
        //assume str1.length()==str2.length()
        int diff = 0;
        for(int i=0;i<str1.length() && diff<=1;i++){
            if(str1.charAt(i)!=str2.charAt(i)){
                diff++;
            }
        }
        return diff==1;
    }
    private ArrayList<Integer> getDigest(String str){
        int[] res = new int[4];
        for(int i=0;i<str.length();i++){
            switch(str.charAt(i)){
                case 'A':res[0]++;break;
                case 'C':res[1]++;break;
                case 'G':res[2]++;break;
                case 'T':res[3]++;break;
            }
        }
        ArrayList<Integer> reslst = new ArrayList<>(4);
        for(int i=0;i<4;i++){
            reslst.add(res[i]);
        }
        return reslst;
    }
}

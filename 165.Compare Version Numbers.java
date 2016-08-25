/**
 *Result:
 * 71 / 71 test cases passed.
 * Status: Accepted
 * Runtime: 3 ms
 * Your runtime beats 45.33% of javasubmissions.
 *Date:
 * 8/25/2016
 */

public class Solution {
    public int compareVersion(String version1, String version2) {
        String[] vlst1 = version1.split("\\.");
        String[] vlst2 = version2.split("\\.");
        int minlen = vlst1.length<vlst2.length?vlst1.length:vlst2.length;
        int i=0;
        for(i=0;i<minlen;i++){
            int v1 = Integer.parseInt(vlst1[i]);
            int v2 = Integer.parseInt(vlst2[i]);
            if(v1<v2)
                return -1;
            if(v1>v2)
                return 1;
        }
        if(vlst1.length>vlst2.length){
            for(;i<vlst1.length;i++){
                if(Integer.parseInt(vlst1[i])!=0)
                    return 1;
            }
            return 0;
        }
        if(vlst1.length<vlst2.length){
            for(;i<vlst2.length;i++){
                if(Integer.parseInt(vlst2[i])!=0)
                    return -1;
            }
            return 0;
        }
        return 0;
    }
}

public class Solution {
    public int myAtoi(String str) {
        str = str.trim();
        if(str.length()==0){
            return 0;
        }
        int res = 0;
        boolean neg = false;
        int i = 0;
        if(str.charAt(0)=='-' || str.charAt(0)=='+'){
            i++;
            neg = str.charAt(0)=='-';
        }
        while(i<str.length() && str.charAt(i)>='0' && str.charAt(i)<='9'){
            int n = str.charAt(i)-'0';
            System.out.println(n+","+res);
            if((n>7 && Integer.MAX_VALUE/10==res) || Integer.MAX_VALUE/10<res){
                return neg?Integer.MIN_VALUE:Integer.MAX_VALUE;
            }
            res = res*10+n;
            i++;
        }
        return neg?-res:res;
    }
}

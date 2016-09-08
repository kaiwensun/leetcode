/**
 *Result:
 * 601 / 601 test cases passed.
 * Status: Accepted
 * Runtime: 8 ms
 * Your runtime beats 17.15% of javasubmissions.
 *Date:
 * 9/8/2016
 */
public class Solution {
    public String numberToWords(int num) {
        if(num==0)
            return "Zero";
        List<Integer> ints = splitedString(num);
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<ints.size();i++){
            String d3 = translate3Digits(ints.get(i));
            if(d3.equals(""))
                continue;
            if(sb.length()!=0)
                sb.insert(0," ");
            sb.insert(0,THOUS[i]);
            if(i!=0)
                sb.insert(0," ");
            sb.insert(0,d3);
        }
        return sb.toString();
    }
    private final static String[] DIGIT = {"","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"};
    private final static String[] TEENS = {"Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"};
    private final static String[] TENS = {"","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"};
    private final static String[] THOUS = {"","Thousand","Million","Billion"};
    private String translate3Digits(int digits){
        String str = ""+digits;
        StringBuilder sb = new StringBuilder();
        int c = digits%10;
        int b = (digits%100)/10;
        int a = digits/100;
        if(digits==0)
            return "";
        if(c==0){
            sb.append(TENS[b]);
        }
        else{
            if(b==1){
                sb.append(TEENS[c]);
            }
            else{
                sb.append(TENS[b]);
                if(sb.length()!=0)
                    sb.append(" ");
                sb.append(DIGIT[c]);
            }
        }
        if(a!=0){
            if(sb.length()!=0)
                sb.insert(0," ");
            sb.insert(0," Hundred");
            sb.insert(0,DIGIT[a]);
        }
        return sb.toString();
    }
    private List<Integer> splitedString(int num){
        List<Integer> ints = new LinkedList<>();
        while(num!=0){
            ints.add(num%1000);
            num /= 1000;
        }
        return ints;
    }
    
}

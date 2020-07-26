public class Solution {
    String getDigit(int num, int unit){
        char one,five,ten;
        switch(unit){
            case 0:one = 'I';five = 'V';ten='X';break;
            case 1:one = 'X';five = 'L';ten='C';break;
            case 2:one = 'C';five = 'D';ten='M';break;
            case 3:one = 'M';five = ' ';ten=' ';break;
            default:one = ' ';five = ' ';ten=' ';break;
        }
        switch(num){
            case 0:return "";
            case 1:return ""+one;
            case 2:return ""+one+one;
            case 3:return ""+one+one+one;
            case 4:return ""+one+five;
            case 5:return ""+five;
            case 6:return ""+five+one;
            case 7:return ""+five+one+one;
            case 8:return ""+five+one+one+one;
            case 9:return ""+one+ten;
            default:return "";
        }
    }
    public String intToRoman(int num) {
        String res = "";
        for(int unit = 0;num!=0;unit++){
            
            res = getDigit(num%10,unit)+res;
            num /=10;
        }
        return res;
    }
}

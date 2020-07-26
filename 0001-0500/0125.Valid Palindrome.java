/**
 * Basic ideea:
 * 	Two pointers.
 * Result:
 * 	476 / 476 test cases passed.
 * 	Status: Accepted
 * 	Runtime: 10 ms
 * 	Your runtime beats 56.42% of java submissions.
 * Date:
 * 	2/6/2016
 */

public class Solution {
    public boolean isPalindrome(String s) {
        int l=0, r=s.length()-1;
        char cl=' ', cr=' ';
        int len = s.length();
        while(l<=r){
            do{
                try{cl=Character.toLowerCase(s.charAt(l++));}
                catch(IndexOutOfBoundsException e){cl='\u0001';break;}
            }while(!(Character.isLetter(cl)||Character.isDigit(cl)));
            do{
                try{cr=Character.toLowerCase(s.charAt(r--));}
                catch(IndexOutOfBoundsException e){cr='\u0001';break;}
            }while(!(Character.isLetter(cr)||Character.isDigit(cr)));
            if(cl!=cr)
                return false;
        }
        return true;
    }
}


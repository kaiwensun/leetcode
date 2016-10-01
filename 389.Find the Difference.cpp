/**
 *Result:
 * 52 / 52 test cases passed.
 * Status: Accepted
 * Runtime: 3 ms
 * Your runtime beats 56.79% of cpp submissions.
 *Date:
 * 10/1/2016
 */
class Solution {
public:
    char findTheDifference(string s, string t) {
       int table[26] = {0}; 
       for(int i=0;i<t.length();i++){
           table[t.at(i)-'a']++;
       }
       for(int i=0;i<s.length();i++){
           table[s.at(i)-'a']--;
       }
       for(int i=0;i<26;i++){
           if(table[i]==1){
               return 'a'+i;
           }
       }
       return -1;
    }
};

class Solution {
public:
    int romanToInt(string s) {
        int res = 0;
        for(size_t i=0;i<s.length()-1;i++){
            if(getValue(s[i])<getValue(s[i+1])){
                res-=getValue(s[i]);
            }
            else{
                res+=getValue(s[i]);
            }
        }
        return res+getValue(s[s.length()-1]);
    }
private:
    int getValue(char c){
        switch(c){
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
        }
        return 0;
    }
};

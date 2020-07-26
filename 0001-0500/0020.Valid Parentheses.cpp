#include<stack>
class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        const char* str = s.c_str();
        while(*str!='\0')
        {
            char c = *str;
            if(c=='('||c=='['||c=='{')
                stk.push(c);
            else if (c==')'||c==']'||c=='}')
            {
                if(stk.empty())
                    return false;
                switch(c)
                {
                    case ')':c='(';break;
                    case ']':c='[';break;
                    case '}':c='{';break;
                }
                if(c != stk.top())
                    return false;
                stk.pop();
            }
            else
                return false;
            str++;
        }
        if(stk.empty())
            return true;
        return false;
    }
};


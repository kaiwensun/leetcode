/**
 *Result:
 * 315 / 315 test cases passed.
 * Status: Accepted
 * Runtime: 9 ms
 * Your runtime beats 29.69% of cpp submissions.
 */
class Solution {
public:
	string addStrings(string num1, string num2) {
		if (num1.size() == 0 && num2.size() == 0){
			return "0";
		}
		string result;
		string::reverse_iterator i1 = num1.rbegin();
		string::reverse_iterator i2 = num2.rbegin();
		int carry = 0;
		while (i1 != num1.rend() && i2 != num2.rend()){
			int n1 = *i1 - '0';
			int n2 = *i2 - '0';
			int r = n1 + n2 + carry;
			if (r >= 10){
				carry = 1;
				r -= 10;
			}
			else{
				carry = 0;
			}
			result.push_back(r + '0');
			i1++;
			i2++;
		}
		string::reverse_iterator* i = &i1;
		string* num = &num1;
		if (i1 == num1.rend()){
			i = &i2;
			num = &num2;
		}
		while (*i != num->rend()){
			int n = **i - '0';
			int r = n + carry;
			if (r >= 10){
				carry = 1;
				r -= 10;
			}
			else{
				carry = 0;
			}
			result.push_back(r + '0');
			(*i)++;
		}
		if (carry){
			result.push_back('1');
		}
		reverse(result.begin(), result.end());
		return result;
	}
};

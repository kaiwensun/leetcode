/*
 * ˼·��ֻ����output������ռ䣬�������顣��һ�����������дnums[i]����������ֵĳ˻����ڶ�������������nums[i]�Ҳ��������ֵĳ˻�����output[i]��ˡ�
 * Leetcode�������������ҵ�˼������
 * Leetcode������������һ�����õĽ⣬�õݹ���õķ�����дoutput[] https://leetcode.com/discuss/47226/my-recursive-solution-o-n-time-o-1-space
 */
#pragma warning (disable:4996)
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;
class Solution {
public:
	vector<int> productExceptSelf(vector<int>& nums) {
		vector<int> output;
		vector<int>::const_iterator it;
		vector<int>::const_reverse_iterator rit;
		vector<int>::reverse_iterator routputit;
		int left = 1;
		for (it = nums.begin(); it != nums.end(); it++)
		{
			output.push_back(left);
			left *= *it;
		}
		int right = 1;
		for (rit = nums.rbegin(), routputit = output.rbegin(); rit != nums.rend(); rit++,routputit++)
		{
			*routputit = *routputit * right;
			right = right*(*rit);
		}
		return output;
	}
};
int main()
{
	int n = 4;
	Solution sol;
	vector<int> input;
	int tmp;
	for (int i = 0; i < n; i++)
	{
		cin >> tmp;
		input.push_back(tmp);
	}
	vector<int> arr = sol.productExceptSelf(input);
	for (vector<int>::const_iterator it = arr.begin(); it != arr.end(); it++)
	{
		cout << *it << ' ';
	}
	cout << endl;
}
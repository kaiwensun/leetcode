/*
 * 思路：只利用output的数组空间，遍历两遍。第一遍从左往右填写nums[i]左侧所有数字的乘积，第二遍从右往左计算nums[i]右侧所有数字的乘积并与output[i]相乘。
 * Leetcode的讨论区中有我的思考过程
 * Leetcode的讨论区中有一个更好的解，用递归调用的方法填写output[] https://leetcode.com/discuss/47226/my-recursive-solution-o-n-time-o-1-space
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
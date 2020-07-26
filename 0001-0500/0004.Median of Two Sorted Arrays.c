#pragma warning (disable:4996)
#include<stdlib.h>
#include<stdio.h>
/* Reference http://articles.leetcode.com/2011/01/find-k-th-smallest-element-in-union-of.html */
#define MAX (int)0x7FFFFFFF
#define MIN (int)0x80000000
int findKthElement(int* nums1, int nums1Size, int* nums2, int nums2Size, int k)
{
	if (nums1Size == 0)
		return nums2[k - 1];
	if (nums2Size == 0)
		return nums1[k - 1];
	int totalSize = nums1Size + nums2Size;
	int i = k*nums1Size / totalSize;
	int j = k - i - 1;
	int nums1_i = i<nums1Size ? nums1[i] : MAX;
	int nums2_j = j<nums2Size ? nums2[j] : MAX;
	int nums1_i_1 = i > 0 ? nums1[i - 1] : MIN;
	int nums2_j_1 = j > 0 ? nums2[j - 1] : MIN;
	if (nums1_i >= nums2_j_1 && nums1_i <= nums2_j)
		return nums1_i;
	if (nums2_j >= nums1_i_1 && nums2_j <= nums1_i)
		return nums2_j;
	if (nums1_i < nums2_j_1)
		return findKthElement(nums1 + i + 1, nums1Size - i - 1, nums2, nums2Size, k - i - 1);
	else
		return findKthElement(nums1, nums1Size, nums2 + j + 1, nums2Size - j - 1, k - j - 1);
}
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
	int totalSize = nums1Size + nums2Size;
	if (totalSize % 2 == 0)
	{
		int a = findKthElement(nums1, nums1Size, nums2, nums2Size, totalSize / 2);
		int b = findKthElement(nums1, nums1Size, nums2, nums2Size, totalSize / 2 + 1);
		return (double)(a + b) / 2;
	}
	else
	{
		return findKthElement(nums1, nums1Size, nums2, nums2Size, totalSize / 2 + 1);
	}
}
int main()
{
	int nums1[] = { 1 };
	int nums2[] = { 0 };
	printf("%f", findMedianSortedArrays(nums1, 1, nums2, 1));
	return 0;
}
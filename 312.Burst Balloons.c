#pragma warning(disable:4996)
#include<stdlib.h>
#include<string.h>
#include<stdio.h>
int maxCoins(int* nums, int numsSize) {
	if (numsSize == 0)
		return 0;
	int size = numsSize + 2;
	int* mynums = (int*)malloc(sizeof(int)*(size));
	mynums[0] = 1;
	mynums[numsSize + 1] = 1;
	int* p = nums, *q = mynums + 1;
	while (p != nums + numsSize)
		*q++ = *p++;
	int** m = (int**)malloc(sizeof(int*)*size);	//m[i][j] indicates the range of length i starting with j
	for (int i = 0; i < size; i++)
	{
		m[i] = (int*)malloc(sizeof(int)*size);
		memset(m[i], 0, sizeof(int)*size);
	}
	for (int i = 1; i < size - 1; i++)
		m[1][i] = mynums[i - 1] * mynums[i] * mynums[i + 1];
	for (int length = 2; length < size - 1; length++)
	{
		for (int start = 1; start < size - length; start++)
		{
			int tmpmax = -1;
			for (int mid = start; mid < start + length; mid++)
			{
				int result = m[mid - start][start] +
					mynums[start - 1] * mynums[mid] * mynums[start + length] +
					m[start + length - mid - 1][mid + 1];
				if (result>tmpmax)
					tmpmax = result;
			}
			m[length][start] = tmpmax;
		}
	}
	return m[size - 2][1];
}

int main()
{
	int nums[] = { 3, 1 };
	int rtn = maxCoins(nums, 2);
	printf("%d\n", rtn);
	return 0;
}
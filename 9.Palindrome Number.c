#pragma warning (disable:4996)
#include<stdlib.h>
#include<string.h>
#include<stdio.h>
#define bool int
#define true 1
#define false 0
int getNthDigit(int x, int n)
{
	int base = 1;
	for (int i = 1; i < n; i++)
		base *= 10;
	return (x / base) % 10;
}
int countDigit(int x)
{
	int digit = 0;
	while (x != 0)
	{
		x /= 10;
		digit++;
	}
	return digit;
}
bool isPalindrome(int x) {
	if (x < 0)
		return false;
	if (x == 0)
		return true;
	if (x % 10 == 0)
		return false;
	for (int right = 1, left = countDigit(x); right < left; right++, left--)
	{
		if (getNthDigit(x, left) != getNthDigit(x, right))
			return false;
	}
	return true;
}

int main()
{
	isPalindrome(12321);
	char buff[20] = "";
	for (int x = 0; x < 110; x++)
		printf("%d,%s\n", x,isPalindrome(x)==true?"true":"false");
	return 0;
}
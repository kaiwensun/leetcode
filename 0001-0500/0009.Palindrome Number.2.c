#pragma warning (disable:4996)
#include<stdlib.h>
#include<string.h>
#include<stdio.h>
#include<math.h>
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
	if (x == 0)
		return true; 
	if (x < 0 || x % 10 == 0)
		return false;
	int digit = (int)log10(x);	//digit-1
	for (int lbase = pow(10, digit), rbase = 1; lbase>rbase; lbase /= 10, rbase *= 10)
	{
		int ldigit = x / lbase % 10;
		int rdigit = x / rbase % 10;
		if (ldigit != rdigit)
			return false;
	}
	return true;
}

int main()
{
	isPalindrome(12321);
	char buff[20] = "";
	for (int x = 0; x < 110; x++)
		printf("%d,%s\n",x,isPalindrome(x)?"true":"false");
	return 0;
}
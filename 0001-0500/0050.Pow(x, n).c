#pragma warning (disable:4996)
#include<stdlib.h>
#include<stdio.h>
#include<math.h>
/* discuss中的其他想法：用泰勒展开实现exp()，然后exp()/exp() */
/*
double myPow(double x, long long int n) {
	if (n == 0)
		return 1;
	if (n == 1)
		return x;
	if (n < 0)
		return 1 / myPow(x, -n);
	if (n % 2 == 1)
		return x*myPow(x, n - 1);
	else
	{
		double factor = myPow(x, n / 2);
		return factor*factor;
	}
}
*/
double myPow(double x, long long int n) {
	/*trick version*/
	if (x == 0)
		return 0;
	if (n == 0)
		return 1;
	if (x<0)
	{
		int sign = (n + 1) % 2;
		x = -x;
		if ((n + 1) % 2)
			return exp(n*log(x));
		else
			return -exp(n*log(x));
	}
	return exp(n*log(x));
}
int main()
{

//	double x = 1.00000;
//	long long int n = -(signed long long int)(2147483648L);
	double x = 2;
	long long int n = 3;
	printf("%f", myPow(x,n));
	return 0;
}
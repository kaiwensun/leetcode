#pragma warning (disable:4996)
#include<stdlib.h>
#include<string.h>
#include<stdio.h>
int reverse(int x) {
	int is_neg = x < 0 ? 1 : 0;
	char s[13] = "";
	//itoa(x, s, 10);	//itoa is not a standard function
	sprintf(s,"%d", x);
	char* str = s[0] == '-' ? s + 1 : s;
	char rtn[14] = "";
	char* src = str;
	int src_len = strlen(src);
	if (src_len>10)
		return 0;
	char* dst = rtn+strlen(src);
	*(dst--) = '\0';
	while (*src != '\0')
		*dst-- = *src++;
	if (is_neg)
	{
		if ((src_len ==10) && strcmp("2147483646", rtn) < 0)
			return 0;
	}
	else
	{
		if ((src_len == 10) && strcmp("2147483647", rtn) < 0)
			return 0;
	}
	int y = atoi(rtn);
	if (is_neg)
		y = -y;
	return y;
}
int main()
{
	printf("%d\n", reverse(-123));
	printf("%d\n", reverse(123));
	printf("%d\n", reverse(2147483647));
	printf("%d\n", reverse(-2147483646));
	return 0;
}
#pragma warning (disable:4996)
#include<stdlib.h>
#include<string.h>
#include<stdio.h>
char* convert(char* s, int numRows) {
	if (*s == '\0')
		return s;
	int len = strlen(s);
	if (numRows == 1)
		return s;
	char* rtn = (char*)malloc(sizeof(char)*(len + 1));
	int block_size = numRows * 2 - 2;
	int rtn_id = 0;
	for (int start = 0; start < numRows; start++)
	{
		unsigned short couple = start == 0 || start == numRows - 1 ? 0 : 1;
		for (int s_id = start; s_id < len; s_id += block_size)
		{
			rtn[rtn_id++] = s[s_id];
			if (couple)
			{
				int step = block_size - start - start;
				if (s_id+step<len)
					rtn[rtn_id++] = s[s_id + step];
			}
		}
	}
	rtn[len] = '\0';
	return rtn;
}
int main()
{
	printf("%s\n", convert("PAYPALISHIRING", 3));
	printf("%s\n", convert("01", 2));
	printf("%s\n", convert("012", 2));
	printf("%s\n", convert("0123", 2));
	printf("%s\n", convert("01234", 2));
	return 0;
}

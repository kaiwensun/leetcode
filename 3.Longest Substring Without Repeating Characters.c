#pragma warning (disable:4996)
#include<stdlib.h>
#include<string.h>
#include<stdio.h>
int lengthOfLongestSubstring(char* s) {
	int hash[128];
	memset(hash, -1, 128 * sizeof(int));
	int max = 0;
	int counter = 0;
	int head = 0;
	int tail = 0;
	for (tail = 0; s[tail] != '\0'; tail++)
	{
		if (hash[s[tail]] == -1)
		{
			hash[s[tail]] = tail;
		}
		else
		{
			counter = tail - head;
			if (counter > max)
				max = counter;
			int newhead = hash[s[tail]]+1;
			for (int i = head; i<newhead; i++)
				hash[s[i]] = -1;
			head = newhead;
			hash[s[tail]] = tail;
		}
	}
	counter = tail - head;
	if (counter > max)
		max = counter;
	return max;
}
int main()
{
	char str[] = "abcd";
	printf("%d\n", lengthOfLongestSubstring(str));
	return 0;
}
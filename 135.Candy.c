#pragma warning (disable:4996)
#include<stdlib.h>
#include<stdio.h>
int goUpward(int* ratings, int startFrom, int ratingsSize, int supposed_candy);
int goDownward(int* ratings, int startFrom, int ratingsSize, int* right_candy/*return my candy*/);

int goDownward(int* ratings, int startFrom, int ratingsSize, int* right_candy/*return my candy*/) {
	if (startFrom == ratingsSize - 1)
		return *right_candy = 1;
	if (ratings[startFrom] < ratings[startFrom + 1])
		return (*right_candy = 1) + goUpward(ratings, startFrom + 1, ratingsSize, 2);
	if (ratings[startFrom] == ratings[startFrom + 1])
	{
		int right_total = goDownward(ratings, startFrom + 1, ratingsSize, right_candy);
		return (*right_candy=1) + right_total;
	}
	else //ratings[startFrom] > ratings[startFrom + 1]
	{
		int right_total = goDownward(ratings, startFrom + 1, ratingsSize, right_candy);
		return (*right_candy = *right_candy + 1) + right_total;
	}
}
int goUpward(int* ratings, int startFrom, int ratingsSize, int supposed_candy) {
	/*goUpward被调用的前提：之前是非降*/
	int total_candy_cnt = 0;
	for (int i = startFrom; i < ratingsSize; i++)
	{
		if (i == ratingsSize - 1)
		{
			total_candy_cnt += supposed_candy;
			return total_candy_cnt;
		}
		if (ratings[i] < ratings[i + 1])
		{
			total_candy_cnt += supposed_candy;
			supposed_candy++;
		}
		else if (ratings[i] == ratings[i + 1])
		{
			total_candy_cnt += supposed_candy;
			supposed_candy = 1;
		}
		else
		{
			int right_candy = 0;
			int here_and_right_total_candy = goDownward(ratings, i, ratingsSize,&right_candy);
			if (right_candy < supposed_candy)
				total_candy_cnt += (supposed_candy - right_candy);
			return total_candy_cnt + here_and_right_total_candy;
		}
	}
}
int candy(int* ratings, int ratingsSize) {
		return goUpward(ratings, 0, ratingsSize, 1);
}
int main()
{
	int arr[] = { 1,2,2 };
	int size = 3;
	printf("%d\n",candy(arr, size));
	return 0;
}
#pragma warning (disable:4996)

#include<stdio.h>
int work(int num)
{
	if (num < 0)
		return 0;
	int digit = num % 10;
	num = num / 10;
	int right = 0;	//不包括当前位
	int total_cnt = digit == 0 ? 0 : 1;
	int zeros = 1;
	int heading = 1;
	while(num != 0)
	{	
		right += digit*zeros;
		digit = num % 10;
		num /= 10;
		if (digit == 1)
		{
			total_cnt += (right+1) + zeros*heading;	//在百位上出现1的个数  +  在百位右侧几位中，达到该百的过程中所出现的1的个数
		}
		else if (digit!=0)
		{
			total_cnt += zeros*10 + zeros*heading*digit;
		}
		
		/*  处理百位，digit=3, zeros = 10, heading = 2, 0~100之间有20个1 */
		/*  处理十位，digit=3, zeros = 1, heading = 1, 0~10之间有1个1 */
		heading++;
		zeros *= 10;

	}
	return total_cnt;
}

int main()
{
	for (int i = 890; i < 1002; i++)
	{
		printf("%4d has #1 = %d\n",i,work(i));
	}
}

/*
digit = 3
round 2，百位。	1个本单位含1的个数 base = 20		base_10 = 100		total_cnt += 3*base + base_10
							base_10	* (当前位是否为1/0)				当前位*base
由三部分组成：一、原来的；	二、当前位为1时的的；	三、当前位右侧的


*/

/*

		base_0			+	base_10					round	分析的digit位
0-9		0				+	10^0					1		十位
0-99	(1)*10			+	10^1					2		百位
0-999	((1)*10+10)*10	+	10^2					3		千位


*/

#pragma warning (disable:4996)

#include<stdio.h>
int work(int num)
{
	if (num < 0)
		return 0;
	int digit = num % 10;
	num = num / 10;
	int right = 0;	//��������ǰλ
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
			total_cnt += (right+1) + zeros*heading;	//�ڰ�λ�ϳ���1�ĸ���  +  �ڰ�λ�Ҳ༸λ�У��ﵽ�ðٵĹ����������ֵ�1�ĸ���
		}
		else if (digit!=0)
		{
			total_cnt += zeros*10 + zeros*heading*digit;
		}
		
		/*  �����λ��digit=3, zeros = 10, heading = 2, 0~100֮����20��1 */
		/*  ����ʮλ��digit=3, zeros = 1, heading = 1, 0~10֮����1��1 */
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
round 2����λ��	1������λ��1�ĸ��� base = 20		base_10 = 100		total_cnt += 3*base + base_10
							base_10	* (��ǰλ�Ƿ�Ϊ1/0)				��ǰλ*base
����������ɣ�һ��ԭ���ģ�	������ǰλΪ1ʱ�ĵģ�	������ǰλ�Ҳ��


*/

/*

		base_0			+	base_10					round	������digitλ
0-9		0				+	10^0					1		ʮλ
0-99	(1)*10			+	10^1					2		��λ
0-999	((1)*10+10)*10	+	10^2					3		ǧλ


*/

/*
 * 思路：把每一个数字想象成高维直角空间中的一个坐标轴。各个数字出每出现一次，都在往自己的那个坐标轴的无穷大点“拉一下”（count++）。count==0表示被拉到了原点上。对于数量超过n/2的众数，一定会把它“拉”到自己这个坐标轴上。
 * 上面是别人的想法。我原来的想法是，qsort()然后去中位数。
 */
int majorityElement(int* nums, int numsSize) {
int i,j,k,count=0;
	j=nums[0];
	for(i=0;i<numsSize;i++)
	{
		if(count==0)
			j=nums[i];
		if(nums[i]==j)
			count++;
		else
		count--;
		if(count>numsSize-i-1)
			return j;
	}
	return j;
}

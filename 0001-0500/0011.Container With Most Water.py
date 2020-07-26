class Solution(object):
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		left = 0
		right = len(height)-1
		result = 0
		while(left<right):
			if height[left]<height[right]:
				result = max(result,height[left]*(right-left))
				pivot = height[left]
				left +=1
				while left<right and height[left]<=pivot:
					left+=1
			else:
				result = max(result,height[right]*(right-left))
				pivot = height[right]
				right-=1
				while left<right and height[right]<=pivot:
					right-=1
		return result

so = Solution()
print so.maxArea([1,2])

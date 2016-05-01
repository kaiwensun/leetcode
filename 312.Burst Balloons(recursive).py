class Solution(object):
	def maxCoins(self, nums):

		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums)==0:
			return 0
		nums.insert(0,1)
		nums.append(1)
		size = len(nums)
		maxcoinsbtwn = [[-1 for j in range(size)] for i in range(size)]
		return self.maxCoinsBetween(nums,maxcoinsbtwn,1,size-2)

	def maxCoinsBetween(self,nums,maxcoinsbtwn,left,right):
		if right<left:
			return 0
		if maxcoinsbtwn[left][right]!=-1:
			return maxcoinsbtwn[left][right]
		if left==right:	#not necessary
			maxcoinsbtwn[left][right] = nums[left-1]*nums[left]*nums[left+1]
			return maxcoinsbtwn[left][right]
		tmpmax = -1
		for mid in range(left,right+1):
			#print 'left=%d,mid=%d,right=%d'%(left,mid,right)
			result = self.maxCoinsBetween(nums,maxcoinsbtwn,left,mid-1) + \
					nums[left-1]*nums[mid]*nums[right+1] + \
					self.maxCoinsBetween(nums,maxcoinsbtwn,mid+1,right)
			if result > tmpmax:
				tmpmax = result
		maxcoinsbtwn[left][right] = tmpmax
		return tmpmax


nums = [3,1,5,8]
s = Solution()
print s.maxCoins(nums)

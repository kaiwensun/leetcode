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
		maxcoinsbtwn = [[0 for j in range(size)] for i in range(size)]	#maxcoinsbtwn[i][j] indicates the range of length i starting with j
		for i in range(1,size-1):
			maxcoinsbtwn[1][i] = nums[i-1]*nums[i]*nums[i+1]
			#maxcoinsbtwn[0][i] = 0

		for length in range(2,size-1):
			for start in range(1,size-length):
				tmpmax = -1
				for mid in range(start,start+length):
					result = maxcoinsbtwn[mid-start][start] + \
							nums[start-1]*nums[mid]*nums[start+length] + \
							maxcoinsbtwn[start+length-mid-1][mid+1]

					if result > tmpmax:
						tmpmax = result
				maxcoinsbtwn[length][start] = tmpmax

		#debut
		for i in range(size):
			for j in range(size):
				print maxcoinsbtwn[i][j],'\t',
			print ''
		return maxcoinsbtwn[size-2][1]

nums = [95,63,82,5,20,63,55,9,81,21,58,7,94,50,43,49,8,0,16,85,89,74,5,81,62,55,60,31,57,67,7,84,55,16,78,88,8,36,60,26,2,1,50,31,49,70,43,60,88,60,24,81,1,49,39,48,39,60,28,40,97,83,68,8,20,75,54,59,58,78,32,49,81,31,23,96,30,95,15,54,43,35,13,28,33,47,64,20,64,66,90,27,77,71,44,41,89,60,46,83,64,5,73,95,69,45,92,15,34,34,81,12,92,91,44,21,75,91,74,57,40,28,0,58,45,2,40,40,67,27,61,22,75,12,31,8,11,21,6,18,15,70,20,9,87,78,21,32,13,50,67,59,68,32,0,23,21,76,67,69,69,47,93,26,16,71,60,47,18,25,73,91,82,88,44,2,30,33,68,93,73,47,75,57,92,80,47,84,77,38,30,67,60,86,52,73,6,71,86,41,22,99,65,81,72,19,26,11,38,80,60,80,97,63,12,47,19,13,40,60,57,31,20,83,68,31,51,21,8,59,88,6,61,28,33,16,59,83,24,15,62,71,91,62,44,96,16,63,73,7,44]
s = Solution()
print s.maxCoins(nums)

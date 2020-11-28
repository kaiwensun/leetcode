class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def dfs(l, r):
            while l <= r:
                mid = (l + r) // 2
                if target in [nums[i] for i in [l, mid, r]]:
                    return True
                if nums[l] < nums[mid]:
                    if nums[l] < target < nums[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[l] > nums[mid]:
                    if nums[mid] < target < nums[l]:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    if nums[mid] < nums[r]:
                        if target < nums[mid]:
                            r = mid - 1
                        elif target < nums[r]:
                            l = mid + 1
                        else:
                            return False
                    elif nums[mid] > nums[r]:
                        if nums[r] < target < nums[mid]:
                            return False
                        else:
                            l = mid + 1
                    else:
                        return dfs(l + 1, mid - 1) or dfs(mid + 1, r - 1)
            return False
        return dfs(0, len(nums) - 1)


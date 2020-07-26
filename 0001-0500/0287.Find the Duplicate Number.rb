# @param {Integer[]} nums
# @return {Integer}
def find_duplicate(nums)
    slow = fast = nums.size - 1
    while slow != fast || slow == nums.size - 1
        slow = nums[slow] - 1
        fast = nums[nums[fast] - 1] - 1
    end
    slow = nums.size - 1
    while slow != fast
        slow = nums[slow] - 1
        fast = nums[fast] - 1
    end
    slow + 1
end

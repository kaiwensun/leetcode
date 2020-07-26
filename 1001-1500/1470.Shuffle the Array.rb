# O(1) space, O(n) time

# @param {Integer[]} nums
# @param {Integer} n
# @return {Integer[]}
def shuffle(nums, n)
    for i in (0...nums.size)
        j = i
        while nums[i] >= 0
            j = j < n ? j * 2 : (j - n) * 2 + 1
            nums[i], nums[j] = nums[j], -nums[i]
        end
    end
    for i in (0...nums.size)
        nums[i] = -nums[i]
    end
    nums
end

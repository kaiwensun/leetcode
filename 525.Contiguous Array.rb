# @param {Integer[]} nums
# @return {Integer}
def find_max_length(nums, head=0, tail=nums.size)
    res = 0
    if head + 1 != tail
        left = Hash.new (-1.0/0.0)
        right = Hash.new (-1.0/0.0)
        mid = (head + tail) / 2
        cnt = 0
        (mid - 1).downto(head).each do |index|
            cnt += (nums[index].zero? ? 1 : -1)
            left[cnt] = mid - index
        end
        cnt = 0
        (mid...tail).each do |index|
            cnt += (nums[index].zero? ? 1 : -1)
            right[cnt] = index - mid + 1
        end
        if left.size > right.size
            left, right = right, left
        end
        left.each do |key, value|
            res = [res, value + right[-key]].max
        end
        if res < mid - head
            res = [res, find_max_length(nums, head, mid)].max
        end
        if res < tail - mid
            res = [res, find_max_length(nums, mid, tail)].max
        end
    end
    res
end

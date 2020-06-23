# @param {Integer[]} nums
# @return {Integer}
def single_number(nums)
    # x and y together represents a bit counter in binary format, counting from 0 to 2. If counter becomes 3, enforce it to become 0.
    # x represents the bit b01 of the counter.
    # y represents the bit b10 of the counter.
    y = x = 0
    for num in nums
        carry = ~(x ^ num) & (x | num)
        x1 = x ^ num
        y1 = y ^ carry
        x = ~(x1 & y1) & x1
        y = ~(x1 & y1) & y1
    end
    x
end

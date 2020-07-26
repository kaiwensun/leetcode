# @param {Integer[]} digits
# @return {Integer[]}
def plus_one(digits)
    carry = 1
    for i in (digits.size - 1).downto(0)
        digits[i] += carry
        carry = digits[i] / 10
        digits[i] %= 10
    end
    digits.insert(0, 1) if carry == 1
    return digits
end

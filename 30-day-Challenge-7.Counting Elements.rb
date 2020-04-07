# @param {Integer[]} arr
# @return {Integer}
def count_elements(arr)
    s = arr.to_set
    arr.reduce(0) { |cnt, a| (s.include? a + 1) ? cnt + 1 : cnt }
end

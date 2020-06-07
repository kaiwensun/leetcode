# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer[]}
def get_strongest(arr, k)
    m = (arr.size - 1) / 2
    median = arr.sort[m]
    arr.sort { |a, b| (a - median).abs == (b - median).abs ? (b - a) : ((b - median).abs - (a - median).abs) } [0...k]
end

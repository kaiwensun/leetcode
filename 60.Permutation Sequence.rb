# @param {Integer} n
# @param {Integer} k
# @return {String}
def get_permutation(n, k, options=(1..n).to_a.map(&:to_s))
    return "" if options.size == 0
    batch_size=(1..(options.size - 1)).inject(1) { |acc, x| acc * x }
    selection_index = (k - 1) / batch_size
    selection = options.delete_at(selection_index)
    return selection + get_permutation(n, k % batch_size, options)
end

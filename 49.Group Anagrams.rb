# @param {String[]} strs
# @return {String[][]}
def group_anagrams(strs)
    hash = Hash.new { |h, k| h[k] = [] }
    strs.each { |str| hash[str.chars.sort.join] << str }
    hash.values
end

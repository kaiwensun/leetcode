# @param {String} pattern
# @param {String} str
# @return {Boolean}
def word_pattern(pattern, str)
    str = str.split(" ")
    if str.size == pattern.size
        p2s = Hash.new
        s2p = Hash.new
        for i in (0...pattern.size) do
            return false if !checkOrSet(pattern[i], str[i], p2s) or !checkOrSet(str[i], pattern[i], s2p)
        end
        true
    else
        false
    end
end
    
def checkOrSet(from, to, hash)
    if hash.include? from
        return false if hash[from] != to
    else
        hash[from] = to
    end
    return true
end


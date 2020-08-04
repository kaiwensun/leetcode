# @param {String} s
# @return {Boolean}
def is_palindrome(s)
    s = s.gsub(/[^0-9a-zA-Z]/, '')
    s.size < 2 || s[0 ... s.size / 2].downcase == s[-(s.size / 2)..s.size].downcase.reverse
end

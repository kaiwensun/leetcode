# @param {Integer} n
# @return {Boolean}
def is_happy(n)
    seen = [n].to_set
    while n != 1 do
        m = 0
        s = n.to_s
        (0...s.size).each { |x| m += s[x].to_i ** 2 }
        if seen.include? m
            return false
        end
        seen << m
        n = m
    end 
    true
end

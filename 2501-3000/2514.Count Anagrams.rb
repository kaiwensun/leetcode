MOD = 10 ** 9 + 7
FACTORIAL = [1]
def get_factorial(n)
    while n > FACTORIAL.size - 1
        FACTORIAL << FACTORIAL[FACTORIAL.size - 1] * FACTORIAL.size % MOD
    end
    FACTORIAL[n]
end

# @param {String} s
# @return {Integer}
def count_anagrams(s)
    def multinv(n)
        m, y, x = MOD, 0, 1
        while n > 1
            y, x = x - n / m * y, y
            m, n = n % m, m
        end
        return (x + MOD) % MOD
    end
    def choose(n, total)
        get_factorial(total) * multinv(get_factorial(total - n) * get_factorial(n) % MOD)
    end
    def count_word_permutations(s)
        cnt = Hash.new 0
        s.each_char { |c| cnt[c] += 1 }
        cnt.each_value.reduce([1, s.size]) { |acc, v| [acc[0] * choose(v, acc[1]) % MOD, acc[1] - v] }[0]
    end
    s.split(' ').each.reduce(1) { |acc, word| acc * count_word_permutations(word) % MOD }
end


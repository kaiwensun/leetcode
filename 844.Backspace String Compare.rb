# @param {String} s
# @param {String} t
# @return {Boolean}
def backspace_compare(s, t)
    def getNextIndex(str, i)
        cnt, p = 0, i
        while cnt <= 0 and p >= -1
            cnt += str[p] == "#" ? -1 : 1
            p -= 1
        end
        p + 1
    end
    ps, pt = s.size, t.size
    while (ps >= 0 and pt >= 0 and s[ps] == t[pt])
        ps = getNextIndex(s, ps - 1)
        pt = getNextIndex(t, pt - 1)
    end
    ps == -1 and pt == -1
end

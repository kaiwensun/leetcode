# @param {String} s
# @return {Boolean}
def check_valid_string(s)
    @cache = Array.new(s.size) { {} }
    @s = s
    def dp(i, unmatched)
        if unmatched < 0 || i < 0
            return unmatched >= 0
        end
        if !@cache[i].has_key? unmatched
            if i == 0
                res = (0 <= unmatched && unmatched <= 1 && @s[0] == "*") || (unmatched == 1 && @s[0] == "(")
            else
                case @s[i]
                    when "("
                        res = dp(i - 1, unmatched - 1)
                    when ")"
                        res = dp(i - 1, unmatched + 1)
                    when "*"
                        res = (-1..1).reduce(false) { |acc, change| acc or dp(i - 1, unmatched + change) }
                end
            end
            
            @cache[i][unmatched] = res
        end
        @cache[i][unmatched]
    end
    dp(s.size - 1, 0)
end

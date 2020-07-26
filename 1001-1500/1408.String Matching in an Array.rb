# @param {String[]} words
# @return {String[]}
def string_matching(words)
    h = Hash.new { |h, k| h[k] = [] }
    words.each { |word| h[word.size] << word}
    keys = h.keys.sort
    res = []
    (0...keys.size).each do |index|
        h[keys[index]].each do |word1|
            do_break = false
            ((index + 1)...keys.size).each do |index2|
                break if do_break
                h[keys[index2]].each do |word2|
                    break if do_break
                    if word2.include? word1
                        res << word1
                        do_break = true 
                    end
                end
            end
        end
    end
    res
end

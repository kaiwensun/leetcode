class Trie

=begin
    Initialize your data structure here.
=end
    def initialize()
        @trie = TrieNode()
    end
    
    def TrieNode()
        Hash.new { |h, k| h[k] = TrieNode() }
    end


=begin
    Inserts a word into the trie.
    :type word: String
    :rtype: Void
=end
    def insert(word)
        p = @trie
        word.each_char do |c|
            p = p[c]
        end
        p["#"] = true
    end
    


=begin
    Returns if the word is in the trie.
    :type word: String
    :rtype: Boolean
=end
    def search(word)
        p = @trie
        word.each_char do |c|
            if p.include? c
                p = p[c]
            else
                return false
            end
        end
        p.include? "#"
    end


=begin
    Returns if there is any word in the trie that starts with the given prefix.
    :type prefix: String
    :rtype: Boolean
=end
    def starts_with(prefix)
        p = @trie
        prefix.each_char do |c|
            if p.include? c
                p = p[c]
            else
                return false
            end
        end
        true
    end


end

# Your Trie object will be instantiated and called as such:
# obj = Trie.new()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.starts_with(prefix)

class MyHashSet

=begin
    Initialize your data structure here.
=end
    def initialize()
        @@PRIME = 99991
        @array = []
    end


=begin
    :type key: Integer
    :rtype: Void
=end
    def add(key)
        if !contains(key)
            hash = key % @@PRIME
            @array[hash] = [] if @array[hash].nil?
            @array[hash] << key
        end
    end


=begin
    :type key: Integer
    :rtype: Void
=end
    def remove(key)
        if contains(key)
            hash = key % @@PRIME
            @array[hash].delete(key)
        end
    end


=begin
    Returns true if this set contains the specified element
    :type key: Integer
    :rtype: Boolean
=end
    def contains(key)
        hash = key % @@PRIME
        !@array[hash].nil? && @array[hash].include?(key)
    end


end

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet.new()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

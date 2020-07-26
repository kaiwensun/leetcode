class LRUCache
    class Node
        attr_accessor :key, :value, :prev, :next
        def initialize(key, value)
            @key = key
            @value = value
            @prev = nil
            @next = nil
        end
        
        def remove
            @prev.next = @next
            @next.prev = @prev
        end
    end

=begin
    :type capacity: Integer
=end
    def initialize(capacity)
        @capacity = capacity
        @map = {}
        @head = LRUCache::Node.new(-1, -1)
        @tail = LRUCache::Node.new(-1, -1)
        @head.next = @tail
        @tail.prev = @head
        @size = 0
    end


=begin
    :type key: Integer
    :rtype: Integer
=end
    def get(key)
        value = @map.fetch(key, @head).value
        if value != -1
            put(key, value)
        end
        value
    end


=begin
    :type key: Integer
    :type value: Integer
    :rtype: Void
=end
    def put(key, value)
        if @map.include? key
            @map[key].remove
            @size -= 1
        end
        node = LRUCache::Node.new(key, value)
        @map[key] = node
        node.prev = @tail.prev
        node.next = @tail
        @tail.prev.next = node
        @tail.prev = node
        @size += 1
        if @size > @capacity
            node = @head.next
            node.next.prev = @head
            @head.next = node.next
            @map.delete node.key
            @size -= 1
        end
    end


end

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache.new(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)

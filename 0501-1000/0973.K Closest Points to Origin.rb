# @param {Integer[][]} points
# @param {Integer} k
# @return {Integer[][]}
def k_closest(points, k)
    max_heap = Heap.new do |a, b|
        if !a.nil? && !b.nil?
            b[0] ** 2 + b[1] ** 2 - a[0] ** 2 - a[1] ** 2
        else
            -1
        end
    end
    for point in points
        max_heap.add(point)
        max_heap.pop if max_heap.size > k
    end
    max_heap.items
end

class Heap
    attr_reader :items
    def initialize(items=[], &block)
        @items = items
        @cmp = block
        items.each do |item|
          self.add(item)
        end
    end
    
    def add(item)
        @items << item
        i = @items.size - 1
        while i > 0 && @cmp.call(items[(i - 1) / 2], items[i]) > 0
            items[i], items[(i - 1) / 2] = items[(i - 1) / 2], items[i]
            i = (i - 1) / 2
        end
    end
    
    def peek()
        @items[0] if !@items.empty?
    end
    
    def size()
        @items.size
    end
    
    def pop()
        if !@items.empty?
            res = self.peek()
            item = @items.pop
            i = 0
            while i < @items.size
                @items[i] = item
                l, r = i * 2 + 1, i * 2 + 2
                litem, ritem = @items[l], @items[r]
                s = @cmp.call(litem, ritem) < 0 ? l : r
                break if @items[s].nil?
                break if @cmp.call(@items[i], @items[s]) <= 0
                item = @items[i]
                @items[i], @items[s] = @items[s], @items[i]
                i, s = s, i
            end
            res
        end
    end 
end

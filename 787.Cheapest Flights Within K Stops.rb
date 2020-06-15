# @param {Integer} n
# @param {Integer[][]} flights
# @param {Integer} src
# @param {Integer} dst
# @param {Integer} k
# @return {Integer}
def find_cheapest_price(n, flights, src, dst, k)
    graph = Hash.new { |h, k| h[k] = [] }
    for from, to, cost in flights
        graph[from] << [to, cost]
    end
    heap = [[0, src, k + 1]]
    while heap.any?
        item = heappop(heap)
        if dst == item[1]
            return item[0]
        end
        next if item[2].zero?
        for neighbor, cost in graph[item[1]]
            heappush([item[0] + cost, neighbor, item[2] - 1], heap)
        end
    end
    return -1
end

def heappush(item, heap)
    i = heap.size
    heap << item
    until i == 0 || (heap[(i - 1) / 2][0] <= heap[i][0])
        heap[(i - 1) / 2], heap[i]  = heap[i], heap[(i - 1) / 2]
        i = (i - 1) / 2
    end
end

def heappop(heap)
    return heap.pop if heap.size == 1
    res = heap[0]
    heap[0] = heap.pop
    i = 0
    while true
        l = i * 2 + 1
        r = i * 2 + 2
        left = l < heap.size ? heap[l] : [1.0 / 0.0, 1.0 / 0.0]
        right = r < heap.size ? heap[r] : [1.0 / 0.0, 1.0 / 0.0]
        if left[0] <= right[0]
            m, min = l, left
        else
            m, min = r, right
        end
        break if heap[i][0] <= min[0]
        heap[i], heap[m] = heap[m], heap[i]
        i = m
    end
    res
end

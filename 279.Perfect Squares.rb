# @param {Integer} n
# @return {Integer}
def num_squares(n)
    steps = (1..Math.sqrt(n).to_i).map { |root| root ** 2 } .to_a
    seen = Array.new(n + 1)
    queue = Queue.new
    queue << 0 << "#"
    cnt = 0
    while true
        num = queue.pop
        if num == "#"
            cnt += 1
            queue.push "#"
        else
            for step in steps
                break if num + step > n
                next if seen[num + step]
                return cnt + 1 if num + step == n
                seen[num + step] = cnt
                queue.push (num + step)
            end
        end
    end
end

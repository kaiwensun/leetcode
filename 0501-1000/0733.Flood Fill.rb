# @param {Integer[][]} image
# @param {Integer} sr
# @param {Integer} sc
# @param {Integer} new_color
# @return {Integer[][]}
DELTA = [1, 0, -1, 0, 1]
def flood_fill(image, sr, sc, new_color, old_color=nil)
    puts "#{[sr, sc]}"
    old_color = image[sr][sc] if old_color.nil?
    if !(sr < 0 || sr >= image.size || sc < 0 || sc >= image[0].size) && image[sr][sc] == old_color && new_color != old_color
        image[sr][sc] = new_color
        for i in (0...4)
            flood_fill(image, sr + DELTA[i], sc + DELTA[i + 1], new_color, old_color)
        end
    end
    image
end

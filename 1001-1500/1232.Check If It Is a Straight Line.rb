# @param {Integer[][]} coordinates
# @return {Boolean}
def check_straight_line(coordinates)
    ref = coordinates[0]
    slopes = coordinates[1..-1].map { |cord| cord.zip(ref).map { |x| x[0] - x[1] } }.map { |cord| cord[1].to_f / cord[0] }
    slopes = Set.new(slopes)
    slopes.size == 1 || slopes == Set.new([1.0/0, -1.0/0])
end

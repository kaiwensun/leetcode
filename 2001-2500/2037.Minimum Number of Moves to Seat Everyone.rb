# @param {Integer[]} seats
# @param {Integer[]} students
# @return {Integer}
def min_moves_to_seat(seats, students)
    seats.sort.zip(students.sort).map{ |x, y| (x - y).abs }.sum
end


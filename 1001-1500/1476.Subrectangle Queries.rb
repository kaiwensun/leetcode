class SubrectangleQueries

=begin
    :type rectangle: Integer[][]
=end
    def initialize(rectangle)
        @initial = rectangle
        @history = []
    end


=begin
    :type row1: Integer
    :type col1: Integer
    :type row2: Integer
    :type col2: Integer
    :type new_value: Integer
    :rtype: Void
=end
    def update_subrectangle(row1, col1, row2, col2, new_value)
        @history << [row1, col1, row2, col2, new_value]
    end


=begin
    :type row: Integer
    :type col: Integer
    :rtype: Integer
=end
    def get_value(row, col)
        for row1, col1, row2, col2, new_value in @history.reverse
            if row1 <= row && row <= row2 && col1 <= col && col <= col2
                return new_value
            end
        end
        return @initial[row][col]
    end


end

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries.new(rectangle)
# obj.update_subrectangle(row1, col1, row2, col2, new_value)
# param_2 = obj.get_value(row, col)

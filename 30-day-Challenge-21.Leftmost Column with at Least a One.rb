# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix
# 	def get(x, y)
# 		@return {Integer}
# 	end
#
# 	def dimensions()
# 		@return {List[Integer]}
# 	end
# end

# @param {BinaryMatrix} binaryMatrix
# @return {Integer}
def leftMostColumnWithOne(binaryMatrix)
    m, n = binaryMatrix.dimensions
    j = n
    (0...m).each do |i|
        j = getLeftMost1Index(binaryMatrix, i, j)
    end
    j == n ? -1 : j
end

def getLeftMost1Index(binaryMatrix, row_index, ending)
    lo, hi = 0, ending
    while lo < hi
        mid = (lo + hi) / 2
        value = binaryMatrix.get(row_index, mid)
        if value == 1
            hi = mid
        else
            lo = mid + 1
        end
    end
    hi
end

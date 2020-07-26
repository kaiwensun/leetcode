minimum(left, right):
  left = left + n
  right = right + n
  minimum = Integer.MAX_VALUE
  while left < right:
    if left is odd:
      // left is out of range of parent interval, check value of left node first, then shift it right in the same level
      minimum = min(minimum, segmentTree[left])
      left = left + 1
    if right is odd:
      // right is out of range of current interval, shift it left in the same level and then check the value
      right = right - 1
      minimum = min(minimum, segmentTree[right])
    // move left and right one level up
    left = left / 2
    right = right / 2

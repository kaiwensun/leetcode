class FirstUnique

=begin
    :type nums: Integer[]
=end
    def initialize(nums)
        @dup = Hash.new 0
        @nums = nums
        @index = 0
        nums.each { |num| @dup[num] += 1 }
    end


=begin
    :rtype: Integer
=end
    def show_first_unique()
        while @index < @nums.size && @dup[@nums[@index]] > 1
            @index += 1
        end
        @index < @nums.size ? @nums[@index] : -1
    end


=begin
    :type value: Integer
    :rtype: Void
=end
    def add(value)
        @dup[value] += 1 
        if @dup[value] == 1
            @nums << value
        end
    end


end

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique.new(nums)
# param_1 = obj.show_first_unique()
# obj.add(value)


=begin
test

#input1=["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
#input2=[[[2,3,5]],[],[5],[],[2],[],[3],[]]

#input1=["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
#input2=[[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]

input1=["FirstUnique","showFirstUnique","add","showFirstUnique"]
input2=[[[809]],[],[809],[]]


def execute(input1, input2)
  for i in (0...input1.size)
      if input1[i] == "FirstUnique"
        s = FirstUnique.new(input2[i][0])
      elsif input1[i] == "showFirstUnique"
          puts s.show_first_unique()
      else
        s.add(input2[i][0])
        puts "add #{input2[i][0]}"
      end
  end
end

execute(input1, input2)
=end

# @param {Integer[][]} people
# @return {Integer[][]}
def reconstruct_queue(people)
    groups = people.group_by &:first
    res = []
    for key in groups.keys.sort.reverse
        for person in groups[key].sort
            res.insert(person[1], person)
        end
    end
    res
end

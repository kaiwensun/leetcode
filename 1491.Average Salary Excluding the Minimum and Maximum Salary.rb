# @param {Integer[]} salary
# @return {Float}
def average(salary)
    (salary.sum - salary.min - salary.max) / (salary.size - 2).to_f     
end

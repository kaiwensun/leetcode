require 'date'
# @param {String} date
# @return {String}
def reformat_date(date)
    Date.parse(date).to_s
end

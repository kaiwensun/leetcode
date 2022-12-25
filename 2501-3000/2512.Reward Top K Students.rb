# @param {String[]} positive_feedback
# @param {String[]} negative_feedback
# @param {String[]} report
# @param {Integer[]} student_id
# @param {Integer} k
# @return {Integer[]}
def top_students(positive_feedback, negative_feedback, report, student_id, k)
    pos_hash = positive_feedback.to_set
    neg_hash = negative_feedback.to_set
    points = Hash.new 0
    report.zip(student_id).each do |rpt, sid|
        points[sid] += 3 * rpt.split.filter { |word| pos_hash.include? word }.count
        points[sid] -= rpt.split.filter { |word| neg_hash.include? word }.count
    end
    points.each.sort { |a, b| b[1] == a[1] ? a[0] - b[0] : b[1] - a[1] }.map(&:first).first(k)
end


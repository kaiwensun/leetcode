# @param {String} ransom_note
# @param {String} magazine
# @return {Boolean}
def can_construct(ransom_note, magazine)
    cntNote, cntMag = Hash.new(0), Hash.new(0)
    ransom_note.each_char { |c| cntNote[c] += 1 }
    magazine.each_char { |c| cntMag[c] += 1}
    cntNote.all? { |k, v| cntMag[k] >= v }
end

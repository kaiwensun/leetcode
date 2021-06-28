/**
 * @param {string} s
 * @param {string} part
 * @return {string}
 */
var removeOccurrences = function(s, part) {
    let i = s.indexOf(part);
    while (i >= 0) {
        s = s.slice(0, i) + s.slice(i + part.length);
        i = s.indexOf(part);
    }
    return s;
};


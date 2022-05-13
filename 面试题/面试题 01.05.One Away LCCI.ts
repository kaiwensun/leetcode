/**
 * @param {string} first
 * @param {string} second
 * @return {boolean}
 */
var oneEditAway = function(first, second) {
    if (first.length === second.length) {
        let diff = false;
        for (i = 0; i < first.length; i++) {
            if (first[i] !== second[i]) {
                if (diff) return false;
                diff = true;
            }
        }
        return true;
    } else if (Math.abs(first.length - second.length) !== 1) {
        return false;
    } else {
        if (first.length > second.length) {
            const tmp = first; first = second; second = tmp;
        }
        let i = 0, j = 0;
        console.log(first);
        console.log(second);
        while (i < first.length) {
            if (first[i] != second[j] && i == j) {
                j++;
            }
            if (first[i] != second[j]) {
                return false;
            }
            i++;
            j++;
        }
        return true;
    }
};


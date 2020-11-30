/**
 * @param {string} num
 * @param {number} k
 * @return {string}
 */
var removeKdigits = function(num, k) {
    let buff = num.substring(k).split("");
    for (let i = k - 1; i >= 0; i--) {
        let char = num[i];
        for (let j = 0; j < buff.length && char !== undefined && char <= buff[j]; j++) {
            let tmp = char; char = buff[j]; buff[j] = tmp;
        }
    }
    while (buff.length && buff[0] == "0") {
        buff.shift();
    }
    return buff.length ? buff.join("") : "0";
};

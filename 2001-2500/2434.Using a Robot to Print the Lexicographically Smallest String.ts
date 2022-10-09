function robotWithString(s: string): string {
    const counter:{ [key: string]: number }  = {};
    [...s].forEach(c => {
        counter[c] ||= 0;
        counter[c]++;
    });
    const stack = ['{'];
    const res = [];
    const alphabet = [..."abcdefghijklmnopqrstuvwxyz"];
    let i = 0;
    while (stack.length) {
        while (alphabet.length && !counter[alphabet[0]]) {
            alphabet.shift();
        }
        if (alphabet.length && alphabet[0] < stack[stack.length - 1]) {
            const c = s[i++];
            stack.push(c);
            counter[c]--;
        } else {
            res.push(stack.pop());
        }
    }
    res.pop();
    return res.join('');
};


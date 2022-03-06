function sortJumbled(mapping: number[], nums: number[]): number[] {
    const translate = num => parseInt(String(num).split('').map(d => mapping[parseInt(d)]).join(''));
    // As of ECMAScript 2019, the specification requires that the builtin sort() method perform a stable sort
    // https://v8.dev/features/stable-sort
    return nums.sort((a, b) => translate(a) - translate(b));
};


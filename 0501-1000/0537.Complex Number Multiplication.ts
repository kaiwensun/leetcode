function complexNumberMultiply(num1: string, num2: string): string {
    function str2nums(num: string) {
        const nums = num.split('+');
        return [parseInt(nums[0]), parseInt(nums[1].slice(0, -1))];
    }
    const [real1, imag1] = str2nums(num1);
    const [real2, imag2] = str2nums(num2);
    const result = [
        real1 * real2 - imag1 * imag2,
        real1 * imag2 + real2 * imag1
    ];
    return `${result[0]}+${result[1]}i`;
};


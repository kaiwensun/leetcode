function removeDigit(number: string, digit: string): string {
    let i: number, remove_i = 0;
    for (i = 0; i < number.length; i++) {
        if (number[i] === digit) {
            remove_i = i;
            if (number[i] < number[i + 1]) {
                break
            }
        }
    }
    return number.substring(0, remove_i) + number.substring(remove_i + 1);
};


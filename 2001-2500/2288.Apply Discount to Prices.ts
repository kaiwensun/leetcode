function discountPrices(sentence: string, discount: number): string {
    const arr = sentence.split(' ');
    for (let i = 0; i < arr.length; i++) {
        if (/^\$\d+$/.test(arr[i])) {
            arr[i] = `$${(parseInt(arr[i].substr(1)) * (100 - discount) / 100).toFixed(2)}`
        }
    }
    return arr.join(' ');
};


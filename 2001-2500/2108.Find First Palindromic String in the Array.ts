function firstPalindrome(words: string[]): string {
    function isPalindromic(word: string) {
        let l = 0, r = word.length - 1;
        while (l < r) {
            if (word[l++] !== word[r--]) {
                return false;
            }
        }
        return true
    }
    for (let word of words) {
        if (isPalindromic(word)) {
            return word;
        }
    }
    return "";
};


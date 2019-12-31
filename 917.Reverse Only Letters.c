bool isLetter(char c) {
    return ('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z');
}

char * reverseOnlyLetters(char * S){
    if (!*S) return S;
    char *l, *r;
    l = r = S;
    while (*++r);
    while (l < r) {
        while(l < r && !isLetter(*l)) l++;
        while(l < r && !isLetter(*r)) r--;
        if (l < r) {
            char tmp = *l; *l = *r; *r = tmp;
        }
        l++; r--;
    }
    return S;
}

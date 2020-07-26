char* reverseWord(char *s) {
    if (*s == 0) return s;
    char *tail = s;
    while (*(++tail) != 0 && *tail != ' ');
    char *p = tail - 1;
    while (s < p) {char tmp = *s; *s++ = *p; *p-- = tmp;}
    return tail;
}

char * reverseWords(char * s){
    char* p = s;
    do {
        p = reverseWord(p);
    } while (*p++ != 0);
    return s;
}

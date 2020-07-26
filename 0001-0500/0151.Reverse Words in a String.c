char *reverseWord(char *s){
    char* tail = s;
    while (*(++tail) != ' ' && *tail != '\0');
    char *p = tail, *q = s - 1;
    while (++q < --p) {
        char tmp = *p; *p = *q; *q = tmp;
    }
    return tail;
}

void cleanSpaces(char *head) {
    if (*head == 0) return;
    char *fast = head, *slow = head;
    while (*fast == ' ') fast++;
    while (*fast != 0) {
        *slow++ = *fast++;
        while (*fast == ' ') fast++;
        if (*fast != 0 && *(fast - 1) == ' ') {
            *(slow++) = ' ';
        }
    }
    *slow = '\0';
}

char *reverseWords(char *s){
    cleanSpaces(s);
    if (*s == '\0') return s;
    char *p = s - 1;
    while (*(p = reverseWord(p + 1)) != '\0');
    char *q = s - 1;
    char *tail = p;
    while (--p > ++q) {char tmp = *p; *p = *q; *q = tmp;}
    return s;
}


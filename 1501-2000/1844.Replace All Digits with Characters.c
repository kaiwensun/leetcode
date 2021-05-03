char shift(char c, char x) {
    return 'a' + (c - 'a' + x - '0') % 26;
}

char * replaceDigits(char * s){
    for (char* p = s; *p != '\0' && *(p + 1) != '\0'; p += 2) {
        *(p + 1) = shift(*p, *(p + 1));
    }
    return s;
}


int compress(char* chars, int charsSize){
    char *p, *q, *cur;
    char buffer[5];
    p = q = chars;
    do {
        cur = p;
        int cnt = 0;
        while (p == chars + charsSize || (++p < chars + charsSize && *cur == *p)) {
            cnt++;
        }
        *q++ = *cur;
        if (p - cur > 1) {
            sprintf(buffer, "%d", p - cur);
            char *b = buffer;
            while (*b != '\0') {
                *(q++) = *(b++);
            }
        }
    } while(p != chars + charsSize);
    return q - chars;
}


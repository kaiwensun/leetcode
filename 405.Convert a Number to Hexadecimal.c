char * toHex(int num){
    char dec2hex[] = "0123456789abcdef";
    unsigned int unum = (unsigned)num;
    char* str = calloc(9, sizeof(char));
    char* p = str + 8;
    while (str != p) {
        *(--p) = dec2hex[unum & 0xF];
        unum >>= 4;
    }
    while (*p == '0' && *(p + 1) !='\0') p++;
    return p;
}

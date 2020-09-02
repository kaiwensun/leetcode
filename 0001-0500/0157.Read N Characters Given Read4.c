/**
 * The read4 API is defined in the parent class Reader4.
 *     int read4(char *buf4);
 */

/**
 * @param buf Destination buffer
 * @param n   Number of characters to read
 * @return    The number of actual characters read
 */

int read4(char *buf4);

int _read(char* buf, int n) {
    char* dst = buf;
    char buff4[5];
    char* src = buff4 + 4;
    int res = 0, size = 0;
    for (int i = 0; i < n && dst < buf + res + 1; i++) {
        if (src == buff4 + 4) {
            res += read4(buff4);
            src = buff4;
        }
        *(dst++) = *(src++);
    }
    *dst = '\0';
    return res;
}


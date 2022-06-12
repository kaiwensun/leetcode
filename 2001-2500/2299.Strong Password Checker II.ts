function strongPasswordCheckerII(password: string): boolean {
    if (password.length >= 8 &&
        /[A-Z]/.test(password) &&
        /[a-z]/.test(password) &&
        /[0-9]/.test(password) &&
        /[!@#\$%\^&\*\(\)\-\+]/.test(password)
    ) {
        for (let i = 1; i < password.length; i++) {
            if (password[i] === password[i - 1]) {
                return false;
            }
        }
        return true;
    }
    return false;
};


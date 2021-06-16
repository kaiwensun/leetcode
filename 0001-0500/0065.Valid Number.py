from collections import Counter
class Solution:
    def isNumber(self, s: str) -> bool:
        def isUnsignedInt(s):
            for c in s:
                if not '0' <= c <= '9':
                    return False
            return len(s) != 0

        def isFloat(s):
            cnt = Counter(s)
            if cnt["."] == 1:
                return all(map(isUnsignedInt, s.split(".")))
            return False
        
        def isFreeSideFloat(s):
            if not s:
                return False
            if s[0] == ".":
                s = s[1:]
            elif s[-1] == ".":
                s = s[:-1]
            return isUnsignedInt(s)

        def removeSign(s):
            if s and s[0] in "+-":
                return s[1:]
            return s

        s = s.replace("E", "e").strip()
        cnt = Counter(s)
        if cnt["e"] == 0:
            s = removeSign(s)
            return isUnsignedInt(s) or isFreeSideFloat(s) or isFloat(s)
        elif cnt["e"] == 1:
            dec, exp = s.split("e")
            dec = removeSign(dec)
            if not (isUnsignedInt(dec) or isFreeSideFloat(dec) or isFloat(dec)):
                return False
            exp = removeSign(exp)
            if not isUnsignedInt(exp):
                return False
        else:
            return False
        return True


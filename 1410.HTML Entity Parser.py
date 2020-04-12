class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
        i = 0
        res = []
        trans = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }
        while i < len(text):
            if text[i] == "&":
                for k, v in trans.iteritems():
                    if text[i:i + len(k)] == k:
                        res.append(v)
                        i += len(k)
                        break
                else:
                    res.append(text[i])
                    i += 1
            else:
                res.append(text[i])
                i += 1
        return "".join(res)

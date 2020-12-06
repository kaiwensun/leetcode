class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        def tokenize(command):
            i = 0
            while i < len(command):
                if command[i] == "G":
                    yield "G"
                    i += 1
                elif command[i + 1] == ")":
                    yield "o"
                    i += 2
                else:
                    yield "al"
                    i += 4
        return "".join(token for token in tokenize(command))


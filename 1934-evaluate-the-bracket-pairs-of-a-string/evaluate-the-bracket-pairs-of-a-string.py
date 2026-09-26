class Solution:
    def evaluate(self, s, knowledge):
        values = dict(knowledge)

        result = ""
        i = 0

        while i < len(s):
            if s[i] == '(':
                j = s.index(')', i)
                key = s[i + 1:j]

                if key in values:
                    result += values[key]
                else:
                    result += "?"

                i = j + 1

            else:
                result += s[i]
                i += 1

        return result
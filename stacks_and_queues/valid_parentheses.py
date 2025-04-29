# leetcode: https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def isValid(self, s: str) -> bool:
        # KEY: only first half of parentheses as key, closing parenthesis as value
        parentheses = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        stack = []
        for p in s:
            if p in parentheses.keys():
                stack.append(p)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if parentheses[top] == p:
                    stack.pop()
                else:
                    return False

        if stack:
            return False

        return True


class MySolution:
    def isValid(self, s: str) -> bool:
        char_dic = {'(': ')',
                    ')': '(',
                    '{': '}',
                    '}': '{',
                    '[': ']',
                    ']': '['}
        length = len(s)

        for i in range(length):
            if char_dic[s[i]] == s[-(1+i)]:
                continue
            elif (i+1) <= length-1 and char_dic[s[i]] == s[i+1]:
                continue
            elif char_dic[s[i]] == s[i-1]:
                continue
            else:
                return False
        return True


# print(MySolution().isValid("([{}])"))
print(MySolution().isValid("()[]{}"))

from typing import string
# leetcode: https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def isValid(self, s: string) -> bool:
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

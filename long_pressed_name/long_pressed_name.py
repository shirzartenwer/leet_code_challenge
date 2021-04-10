'''https://leetcode.com/problems/long-pressed-name/
'''
from collections import Counter
from typing import Counter
import string

# My solution that doesn't solve the edge case that keys are not in the right order
# class Solution:
#     def isLongPressedName(self, name: str, typed: str) -> bool:
#         name_count = Counter(list(name))
#         typed_count = Counter(list(typed))
#         print(typed_count)
#         for key in typed_count.keys():
#             print(typed_count.keys().index(key))
#             if typed_count[key] >= name_count[key]:
#                 continue
#             else:
#                 return False
        
#         if name_count.keys() == typed_count.keys():
#             return True
#         else:
#             return False
            
# The right solution
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        # two pointers to the "name" and "typed" string respectively
        np, tp = 0, 0

        # advance two pointers, until we exhaust one of the strings
        while np < len(name) and tp < len(typed):
            if name[np] == typed[tp]:
                np += 1
                tp += 1
            elif tp >= 1 and typed[tp] == typed[tp-1]:
                tp += 1
            else:
                return False

        # if there is still some characters left *unmatched* in the origin string,
        #   then we don't have a match.
        # e.g.  name = "abc"  typed = "aabb"
        if np != len(name):
            return False
        else:
            # In the case that there are some redundant characters left in typed
            # we could still have a match.
            # e.g.  name = "abc"  typed = "abccccc"
            while tp < len(typed):
                if typed[tp] != typed[tp-1]:
                    return False
                tp += 1

        # both strings have been consumed
        return True
        
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.isLongPressedName("alex", "aaleex"))
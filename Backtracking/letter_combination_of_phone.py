#  https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class BruteForceSolution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {"2": ["a", "b", "c"],
                     "3": ["d", "e", "f"],
                     "4": ["g", "h", "i"],
                     "5": ["j", "k", "l"],
                     "6": ["m", "n", "o"],
                     "7": ["p", "q", "r", "s"],
                     "8": ["t", "u", "v"],
                     "9": ["w", "x", "y", "z"]}

        result = []

        if len(digits) == 0:
            return []

        if len(digits) == 1:
            return digit_map[digits]

        if len(digits) == 2:
            for ele_1 in digit_map[digits[0]]:
                for ele_2 in digit_map[digits[1]]:
                    result.append(ele_1+ele_2)

        if len(digits) == 3:
            for ele_0 in digit_map[digits[0]]:
                for ele_1 in digit_map[digits[1]]:
                    for ele_2 in digit_map[digits[2]]:
                        result.append(ele_0 + ele_1 + ele_2)

        if len(digits) == 4:
            for ele_0 in digit_map[digits[0]]:
                for ele_1 in digit_map[digits[1]]:
                    for ele_2 in digit_map[digits[2]]:
                        for ele_3 in digit_map[digits[3]]:
                            result.append(ele_0 + ele_1 + ele_2 + ele_3)
        return result


class BackTrackingSolution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {"2": ["a", "b", "c"],
                     "3": ["d", "e", "f"],
                     "4": ["g", "h", "i"],
                     "5": ["j", "k", "l"],
                     "6": ["m", "n", "o"],
                     "7": ["p", "q", "r", "s"],
                     "8": ["t", "u", "v"],
                     "9": ["w", "x", "y", "z"]}

        answer = []

        if digits == "":
            return []

        def backtrack(cur, index):
            if len(cur) == len(digits):
                answer.append(cur)
                return

            candidate_list = digit_map[digits[index]]
            for i in range(len(candidate_list)):
                cur = cur+candidate_list[i]
                backtrack(cur, index+1)
                # If the follwoing line is missing, this function will not return when it should, for example
                # it should be backtrack("ae", 2), where it just return, but instead, it becomes ("ade", 2),
                # and it doesn't return, but keep going to the line candidate_list = digit_map[digits[2]]
                # which gives index error.
                cur = cur[:-1]

        backtrack("", 0)
        return answer


print(BackTrackingSolution().letterCombinations(digits="23"))

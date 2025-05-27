# https://leetcode.com/problems/push-dominoes/?envType=daily-question&envId=2025-05-02


# ".L.R...LR..L.."
# "LL.RR.LLRRLL.."

class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        def modify_string(string: list):
            if len(string) <= 1:
                return string

            changes_list = []
            for index in range(len(string)):
                if string[index] == ".":
                    if index > 0 and index < len(string)-1:
                        if string[index-1] == "R":
                            if string[index+1] != "L":
                                changes_list.append((index, "R"))
                        #  if there is nothing from left side that pushes to the right,
                        #  then only possiblility of of changes is something on the right side that pushes you to the elft
                        elif string[index+1] == "L":
                            changes_list.append((index, "L"))

                    elif index == 0:
                        if string[index+1] == "L":
                            changes_list.append((index, "L"))

                    elif index == len(dominoes) - 1:
                        if string[index-1] == "R":
                            changes_list.append((index, "R"))

            if len(changes_list) == 0:
                return string
            else:
                for ele in changes_list:
                    string[ele[0]] = ele[1]
                return modify_string(string)

        string_list = list(dominoes)
        string = modify_string(string_list)
        return "".join(string)


# print(Solution().pushDominoes("RR.L"))
# print(Solution().pushDominoes(".L.R...LR..L.."))
print(Solution().pushDominoes("R.R.L"))

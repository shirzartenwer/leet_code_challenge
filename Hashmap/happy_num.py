

class Solution:
    def isHappy(self, n: int) -> bool:
        try:
            str_list = sorted(str(n))
            total_sum = sum((int(ele) ** 2 for ele in str_list))

            if total_sum == 1:
                return True
            else:
                return self.isHappy(total_sum)
        # This will try out the maximuim recursion depth.
        #  This will work, but its not the purpose of this exercise.
        # The purpose is to detect the endless loop early
        # https://en.wikipedia.org/wiki/Cycle_detection
        except RecursionError:
            return False


print(Solution().isHappy(37))

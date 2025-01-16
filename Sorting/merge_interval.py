# https://leetcode.com/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-interview-150


# key points:
# 1. the right end of the interval is always greater than the left end
class Solution:
    def merge(self, list_of_interval: list) -> list:
        list_of_interval.sort()
        final_list = [list_of_interval[0]]

        for ele in list_of_interval[1:]:
            if final_list[-1][-1] >= ele[0] and final_list[-1][0] < ele[0]:
                if final_list[-1][-1] > ele[1]:
                    final_list[-1] = [final_list[-1][0], final_list[-1][-1]]
                else:
                    final_list[-1] = [final_list[-1][0], ele[1]]
            elif final_list[-1][-1] >= ele[0] and final_list[-1][0] >= ele[0]:
                if final_list[-1][-1] > ele[1]:
                    final_list[-1] = [ele[0], final_list[-1][-1]]
                else:
                    final_list[-1] = [ele[0], ele[1]]
            else:
                final_list.append([ele[0], ele[1]])

        return final_list


intervals = [[1, 3], [15, 18], [8, 10], [2, 6]]
intervals.sort()
print(intervals)

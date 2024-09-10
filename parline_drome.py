# https://leetcode.com/problems/palindrome-number/

class Solution:

    def isPalindrome(self, x: int) -> bool:
        number_list = list(str(x))
        if len(number_list) == 1:
            return True

        len_list = len(number_list)
        if len_list % 2 == 0:
            middle = len_list//2
        else:
            middle = len_list//2 + 1
        for index in range(middle, len_list):
            if number_list[index] == number_list[len_list-index-1]:
                continue
            else:
                return False
        return True

    def isPalindrome_recursion(self, x: int) -> bool:
        # Convert number to a list of characters (digits)
        number_list = list(str(x))

        # Base case: If the list is empty or has only one element, it's a palindrome
        if len(number_list) <= 1:
            return True

        # Recursive case: Check the first and last characters
        if number_list[0] == number_list[-1]:
            # Remove the first and last characters and call recursively
            return self.isPalindrome(int("".join(number_list[1:-1])))
        else:
            # If the first and last characters don't match, it's not a palindrome
            return False


sol = Solution()
sol.isPalindrome(121)
sol.isPalindrome(-10)

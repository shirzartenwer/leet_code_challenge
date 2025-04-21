# https://leetcode.com/problems/palindrome-number/


class Solution:
    # time complexity O(n)
    # space complexity O(n)
    def isPalindrome(self, s: str) -> bool:
        s_striped = ''.join(char.lower() for char in s if char.isalnum())
        s_striped_reverse = s_striped[::-1]
        return s_striped == s_striped_reverse


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

    # isalnum
    # two pointers
    def isPalindrome(s: int) -> bool:
        if s == '':
            return True

        s = s.lower()

        left = 0
        right = len(s)-1
        s_left = ''
        s_right = ''

        while left <= len(s)-1:
            s_left += s[left]
            s_right += s[right]
            left += 1
            right -= 1

        return s_left == s_right


# Parlindrome alphanumeric

class Solution2:

    def isPalindrome(self, s: str) -> bool:
        if s == '':
            return True

        s = s.lower()

        s_new = []
        for char in s:
            if char.isalnum():
                s_new.append(char)

        left = 0
        right = len(s_new)-1
        s_left = ''
        s_right = ''

        while left <= len(s_new)-1:
            s_left += s_new[left]
            s_right += s_new[right]
            left += 1
            right -= 1

        return s_left == s_right


# sol = Solution()
# sol.isPalindrome(121)
# sol.isPalindrome(-10)


sol2 = Solution2()
print(sol2.isPalindrome("A man, a plan, a canal: Panama"))
print(sol2.isPalindrome("race a car"))
print(sol2.isPalindrome("0P"))

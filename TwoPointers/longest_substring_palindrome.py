# https://leetcode.com/problems/longest-palindromic-substring/editorial/

class Solution:
    def isPalindrome(self, s: str) -> bool:
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

    def check_palindrom(self, s, left, right):
        ans = ""
        while left >= 0 and right <= len(s)-1:
            if self.isPalindrome(s[left:right+1]):
                ans = s[left:right+1]
                left = left - 1
                right = right + 1
            else:
                break

        return ans

    def longestPalindrome(self, s: str) -> str:
        #  the key here is to use the middle of the string and keep expanding the palindrome, when it is a Palindrome
        list_of_ans = []
        for index in range(len(s)):
            if index+1 <= len(s)-1 and s[index+1] == s[index]:
                list_of_ans.append(self.check_palindrom(s, index, index+1))
            list_of_ans.append(self.check_palindrom(s, index, index))

        max_l = 0
        result = ''
        for element in list_of_ans:
            if len(element) > max_l:
                max_l = len(element)
                result = element

        return result

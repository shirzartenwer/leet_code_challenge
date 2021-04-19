# https://leetcode.com/problems/reverse-vowels-of-a-string/

from typing import * 

# TODO: check why this code is not working
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels_set = ['a', 'e', 'i','o', 'u', 
                      'A','E', 'I', 'O', 'U']
        str_list = list(s)
        i = 0
        j = len(str_list)-1
        while i <=j:
            if str_list[i] in vowels_set:
                if str_list[j] in vowels_set:
                    exchange = str_list[i]
                    str_list[i] = str_list[j]
                    str_list[j] = exchange
                else:
                    j -=1
                    continue
            elif str_list[j] in vowels_set:
                i +=1
                continue
            else:
                i +=1
                j -=1
                continue
            
            
        str = ''.join(str_list)
        return str
                
                

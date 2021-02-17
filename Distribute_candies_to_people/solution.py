"""Problems: We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.
"""

from typing import *         

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        turn = 1
        left_over_candies = candies
        stopping_criteria = candies
        result = [0]*num_people
        while stopping_criteria > 0:
            for people_index in range(num_people):
                base = num_people * (turn - 1)
                if left_over_candies >= (people_index+1+base):
                    result[people_index] += people_index+1+base
                    stopping_criteria = left_over_candies - (people_index+1+base)
                else: 
                    result[people_index] += left_over_candies
                    stopping_criteria = 0
                    break
                left_over_candies = left_over_candies - result[people_index]
                if left_over_candies <=0:
                    break
            turn +=1    
        return result
        
print(Solution.distributeCandies(Solution, 10, 3))
        
        


    
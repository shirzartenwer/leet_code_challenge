"""Problems: We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.
"""

# class Solution:
#     def distributeCandies(self, candies: int, num_people: int) -> List[int]:
#         List = []
#         turn = 1
#         base = num_people * (turn - 1)
#         left_over_candies = candies
#         while left_over_candies > 0:
#             for people_index in range(num_people):
#                 List[people_index] += people_index+1+base
#             turn +=1
#             base = num_people * (turn - 1)
#             left_over_candies = candies - sum(List) 
            

        

# in each round, the consumed candies are n*(n+1)/2, n = len(num_people)
                
                
            

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        expected_consumption = num_people * (num_people - 1) / 2 
      
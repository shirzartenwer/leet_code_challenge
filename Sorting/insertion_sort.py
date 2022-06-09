from typing import List
def insertion_sort(least: List):
    for i in range(1, len(least)):
        j = i-1
        min_element = least[i]
        while j >=0 and least[j] > min_element:
            least[j+1]= least[j]
            j -=1
        least[j+1] = min_element
    return least
        
random_list = [8, 9 ,1, 4, 5]

result = insertion_sort(random_list)

print(f"The result of the sort is {result}")
                

            
         
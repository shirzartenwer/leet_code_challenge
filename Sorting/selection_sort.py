from typing import List

def selectionsort(lst: List):
    for i in range(len(lst)):
        min_element_index = i
        
        for j in range(i+1, len(lst)):
            if lst[min_element_index] > lst[j]:
                min_element_index = j 
        
        lst[i], lst[min_element_index] = lst[min_element_index], lst[i]
        
    return lst


random_list = [8, 9 ,1, 4, 5]

result = selectionsort(random_list)

print(f"The result of the sort is {result}")
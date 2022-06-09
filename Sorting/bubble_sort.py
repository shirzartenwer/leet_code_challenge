from typing import List

def bubble_sort(least: List):
    for i in range(len(least)):
        for j in range(0, len(least) - i -1):
            if least[j] > least [j+1]:
                least[j], least[j+1] = least [j+1], least[j]
                
    return least

random_list = [8, 9 ,1, 4, 5]

result = bubble_sort(random_list)

print(f"The result of the sort is {result}")
                

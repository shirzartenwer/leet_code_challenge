from typing import List

# TODO: 
# 1. this needs to be run through white board once
# 2. Is this essentially implementing a tree?

def merge_sort(least: List):
    if len (least) > 1:
        mid = len (least) // 2
        left = least[:mid]
        right = least [mid:]
        
        # sort the following divided array recursively 
        merge_sort(left)
        merge_sort(right)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j< len(right):
            if left[i] < right[j]:
                least[k] = left[i]
                i+=1
            else:
                least[k] = right[j]
                j+=1
            k+=1
            
        while i < len(left):
            least[k] = left[i]
            i+=1
            k+=1
            
        while j < len(right):
            least[k] = right[j]
            j+=1
            k+=1
    return least
                    
                    
if __name__ == "__main__":
    given_list = [5 ,2 ,6, 1, 3, 4]
    print(f"The result of sorting is {merge_sort(given_list)}")
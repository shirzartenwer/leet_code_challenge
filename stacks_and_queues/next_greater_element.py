from stack import MyStack


# TODO: This is a great solution. Needs to rehearse. 
def next_greater_element(lst):
    stack = MyStack()
    res = [-1] * len(lst)
    # Reverse iterate list
    for i in range(len(lst) - 1, -1, -1):
        ''' While stack has elements and current element is greater 
        than top element, pop all elements '''
        while not stack.is_empty() and stack.peek() <= lst[i]:
            stack.pop()
        ''' If stack has an element, top element will be 
        greater than ith element '''
        if not stack.is_empty():
            res[i] = stack.peek()
        # push in the current element in stack
        stack.push(lst[i])
    for i in range(len(lst)):
        print(str(lst[i]) + " -- " + str(res[i]))
    return res

if __name__ == "__main__" :
    nge = next_greater_element([4, 6, 3, 2, 8, 1, 9, 9, 9])



# Time Complexity#
# Since we make one iteration over the list of n elements, the algorithm will work in O(n).
# This is a significant improvement over the brute force method’s runtime complexity of O(n2).
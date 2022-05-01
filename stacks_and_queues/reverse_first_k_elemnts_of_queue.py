# problem set is here: https://www.educative.io/module/lesson/data-structures-in-python/B8Q9l3j6zVx



from queue import MyQueue
from stack import MyStack

# My solution
def reverseK(queue, k):
    # Write your code here
    if k < 0:
        return None
    if k > queue.size():
        return None

    new_stack = MyStack()
    for i in range(0, k):
        element = queue.dequeue()
        new_stack.push(element)
        i +=1

    new_queue = MyQueue()
    for i in range(0, k):
        element = new_stack.pop()
        new_queue.enqueue(element)
        i +=1

    for i in range(0, queue.size()):
        new_queue.enqueue(queue.dequeue())
        i +=1

    return new_queue

        
        


# Better solution

def reverseK(queue, k):
    # Handling invalid input
    # TODO: checking the edge cases!
    if queue.is_empty() is True or k > queue.size() or k < 0:
        return None

    stack = MyStack()
    for i in range(k):
        stack.push(queue.dequeue())
    # TODO: pushing into a queue while poping it is pretty smart and time saving 
    while stack.is_empty() is False:
        queue.enqueue(stack.pop())
    size = queue.size()
    for i in range(size - k):
        queue.enqueue(queue.dequeue())

    return queue

# Time complexity: O(N)
class Solution:
    def fib(self, n: int) -> int:
        if n <=1:
            return n 
        else:
            return (self.fib(n-1) + self.fib(n-2))
            
        

# Complexity analysis: 
# Time complexity: O(2^N), This is the slowest way to solve the Fibonacci Sequence 
# because it takes exponential time. The amount of operations needed, 
# for each level of recursion, grows exponentially as the depth approaches N.

# Spatail Complexity: O(N), We need space proportionate to N to account for the max size of the stack, 
# in memory. This stack keeps track of the function calls to fib(N). 
# This has the potential to be bad in cases that there isn't enough physical memory to 
# handle the increasingly growing stack, leading to a StackOverflowError. 
# The Java docs have a good explanation of this, describing it as an error that occurs because an application recurses too deeply.
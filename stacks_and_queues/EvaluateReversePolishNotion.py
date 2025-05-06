class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for ele in tokens:
            if ele == "+":
                stack.append(stack.pop() + stack.pop())
            elif ele == "*":
                stack.append(stack.pop() * stack.pop())
            elif ele == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif ele == "/":
                b, a = stack.pop(), stack.pop()
                # NOTE: the questions demand the result to be round towards 0.
                # which is the same thing as rounding down when it's positive, so we can use //
                # but for negative numbers, it's wrong. But int() conversion rounds towards 0
                stack.append(int(float(a) / b))
            else:
                stack.append(int(ele))

        return stack.pop()

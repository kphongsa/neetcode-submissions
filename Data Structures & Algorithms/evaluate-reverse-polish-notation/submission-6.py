class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        evals = {"+", "-", "*", "/"}
        stack = []

        for i in tokens:

            if i in evals:
                second = int(stack.pop())
                first = int(stack.pop())

                if i == '+':
                    res = first + second
                elif i == '-':
                    res = first - second
                elif i == '*': 
                    res = first * second
                else:
                    res = int(first / second)

                stack.append(res)
            else:
                stack.append(int(i))
            
            print(stack)

        return stack[0]
            
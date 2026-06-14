class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        elementStack = [];
        operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": lambda a,b: int(a/b)};
        result = 0
        for i in tokens:
            if i in operators:
                b = elementStack.pop() 
                a = elementStack.pop() 
                result = operators[i](a, b)
                elementStack.append(result)
            else:
                elementStack.append(int(i))
        return int(elementStack[-1])
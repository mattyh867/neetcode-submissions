class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return tokens[0]

        tmp = []
        for i in tokens:
            if i.isdigit():
                tmp.append(int(i))
                continue

            operand2 = tmp.pop()
            operand1 = tmp.pop()
            if i == "+":
                tmp.append(operand2 + operand1)
            if i == "-":
                tmp.append(operand2 - operand1)
            if i == "*":
                tmp.append(operand2 * operand1)
            if i == "/":
                tmp.append(operand2 // operand1)
            
        return tmp[0]

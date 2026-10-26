class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return tokens[0]

        tmp = []
        for i in tokens:
            if i.isdigit():
                tmp.append(int(i))
                print(f'i={i} tmp={tmp}')
                continue

            operand1 = tmp.pop()
            operand2 = tmp.pop()
            if i == "+":
                tmp.append(operand2 + operand1)
            if i == "-":
                tmp.append(operand2 - operand1)
            if i == "*":
                tmp.append(operand2 * operand1)
            if i == "/":
                tmp.append(operand2 // operand1)
            print(f'i={i} tmp={tmp}')
            
        return tmp[0]

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

            if i == "+":
                result = 0
                while tmp:
                    result = result + tmp.pop()
                tmp.append(result)
            if i == "-":
                result = tmp[0]+tmp[0]
                while tmp:
                    result = result - tmp.pop()
                tmp.append(result)
            if i == "*":
                result = 1
                while tmp:
                    result = result * tmp.pop()
                tmp.append(result)
            if i == "/":
                result = 1
                while tmp:
                    result = result // tmp.pop()
                tmp.append(result)
            print(f'i={i} tmp={tmp}')
            
        return tmp[0]

def calculate(s: str) -> int:
    s=s+'+'
    operator = '+'
    current = 0
    stack = []
    if s[0]=='-':
        operator = '-'

    for i in range(len(s)):
        while s[i].isdigit()==True:
            current=(current*10)+int(s[i])
            i+=1
        else:
            if operator == '+':
                stack.append(current)
            elif operator == '-':
                stack.append(-current)
            elif operator == '*':
                stack.append(current*stack.pop())
            elif operator == '/':
                stack.append(stack.pop()//current)
            current=0
            operator=s[i]
    return sum(stack)

print(calculate('14-3/2'))


# print(-3//2)

# print(3//2)
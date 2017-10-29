from Stack import Stack # my stack class

# this class takes in postfix strings and evaluates them via the stack class
class Parse():
    def __init__(this, string):
        this.chars = string.split()

    def evaluate(this):
        stack = Stack()

        for char in this.chars:
            if char.isdigit():
                stack.push(int(char))

            else:    
                operand1 = stack.pop()
                operand2 = stack.pop()

                if char == '+':
                    stack.push(operand2 + operand1)

                if char == '-':
                    stack.push(operand2 - operand1)
                    
                if char == '*':
                    stack.push(operand2 * operand1)
                    
                if char == '/':
                    stack.push(operand2 / operand1)

        return stack.peek()    
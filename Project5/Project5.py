from stack import Stack

def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    else:
        return -1

def eval_postfix(expr):
    pass

def in2post(expr):
    #check if expr is a string and valid
    #Create an empty stack
    stack = Stack()
    expr_postfix = ""
    #loop through each character in the infix expression
    for char in expr:
        if char == '(':
            #if the character is '(', push it onto the stack
            stack.push(char)
        elif char == ')':
            #if the character is ')', pop from the stack to the postfix expression until '(' is found
            while not stack.is_empty() and stack.top() != '(':
                expr_postfix += stack.pop()
            stack.pop()
        elif char.isalnum():
            #if the character is an operand, add it to the postfix expression
            expr_postfix += char
        else:
            #while the stack is not empty and the precedence of the operator at the top of the stack is greater than or equal to the precedence of the current operator
            while (not stack.is_empty() and precedence(stack.top()) >= precedence(char)):
                #pop the operator from the stack and add it to the postfix expression
                expr_postfix += stack.pop()
            stack.push(char)
    #pop all the operators from the stack and add them to the postfix expression
    while not stack.is_empty():
        expr_postfix += stack.pop()
    stack.clear()

def main():
    with open ("data.txt", "r") as infile:
        for line in infile:
            line = line.strip()
            if line:
                postfix_expr = in2post(line)
                result = eval_postfix(postfix_expr)
    
                print(f"infix: {line}")
                print(f"postfix: {postfix_expr}")
                print(f"answer: {result}")
    
if __name__=="__main__":
    main()
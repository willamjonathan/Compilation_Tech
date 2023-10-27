# ASSIGNMENT 2
# WILLIAM JONATHAN MULYADI & ALEXANDRO JOE CLAUDIO

# translating program to python (80) 
import sys

token = ''
position = 0

# for early error detection (10)
class SyntaxError(Exception):
    pass

def expr():
    global token, position
    try:
        temp = term()
        while position < len(token) and token[position] in ('+', '-'):
            if token[position] == '+':
                position += 1
                temp += term()
            elif token[position] == '-':
                position += 1
                temp -= term()
        return temp
    except SyntaxError:
        raise SyntaxError("Invalid syntax")

def term():
    # adding extra mat operations (2)
    global token, position
    try:
        temp = factor()
        while position < len(token) and token[position] == '/':
            position += 1
            temp /= factor()
        while position < len(token) and token[position] == '*':
            position += 1
            temp *= factor()
        while position < len(token) and token[position] == '%':
            position += 1
            temp %= factor()
        return temp
    except SyntaxError:
        raise SyntaxError("Invalid syntax")

def factor():
    global token, position
    if position < len(token) and token[position] == '(':
        position += 1
        temp = expr()
        if position < len(token) and token[position] == ')':
            position += 1
        else:
            raise SyntaxError("Unmatched parenthesis")
    elif position < len(token) and token[position].isdigit():
        start = position
        while position < len(token) and token[position].isdigit():
            position += 1
        temp = int(token[start:position])
    else:
        raise SyntaxError("Invalid token")
    return temp

# parse tree construction (12)
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def tokenize_expression(expression):
    operators = ['+', '-', '*', '/','%']
    tokens = []
    current_token = ""
    for char in expression:
        if char in operators:
            if current_token:
                tokens.append(current_token)
            tokens.append(char)
            current_token = ""
        else:
            current_token += char
    if current_token:
        tokens.append(current_token)
    return build_expression_tree(tokens)

def build_expression_tree(tokens):
    if len(tokens) == 1:
        return TreeNode(tokens[0])
    else:
        operator = tokens.pop(1)
        return TreeNode(operator, build_expression_tree(tokens[:1]), build_expression_tree(tokens[1:]))

def print_expression_tree(node, indent=""):
    if node:
        print(indent+ node.value)
        if node.left:
            print_expression_tree(node.left)
        if node.right:
            print_expression_tree(node.right, indent + " " * len(node.value))


        
if __name__ == "__main__":
    result = 0
    print("A RECURSIVE-DESCENT CALCULATOR.")
    print("\t the valid operations are +, - and *")
    user_input = input("Enter the calculation string, e.g. '34+6*56': ")
    # removing white space (2)
    user_input = user_input.replace(" ", "")
    parse_tree = tokenize_expression(user_input)
    print_expression_tree(parse_tree)
    
    token = user_input + ' '  

    try:
        result = expr()
        if position == len(token) - 1:
            print(f"Result = {result}")
        else:
            # early error detection 
            print( "Early error detection! ")
            print("Syntax Error: Invalid input")
    except SyntaxError as e:
        print( "Early error detection! ")
        print(f"Error: {e}")
        

equations = []
multipleLine = []
while True:
    eq = input("Input an equation (or 'exit' to finish): ")
    
    if eq.lower() == 'exit':
        break

    equations.append(eq)

line_number = 1  # Initialize line number

for eq in equations:
    i = 0
    while i < len(eq):
        if eq[i].isnumeric():
            j = i
            while j < len(eq) and (eq[j].isnumeric() or eq[j].isalpha()):
                j += 1
            token = eq[i:j]
            if any(c.isalpha() for c in token):
                print(f"Unidentified token on Line {line_number}, Index {i+1} -> {token}")
            else:
                print(token, "-> Number")
            i = j

        elif eq[i] == "+":
            print(eq[i], "-> Addition")
            i += 1

        elif eq[i] == "-":
            print(eq[i], "-> Subtraction")
            i += 1

        elif eq[i] == "*":
            print(eq[i], "-> Multiplication")
            i += 1

        elif eq[i] == "(":
            print(eq[i], "-> Left parantheses")
            i += 1

        elif eq[i] == ")":
            print(eq[i], "-> Right parantheses")
            i += 1
        
        elif eq[i] == "[":
            print(eq[i], "-> Left square bracket")
            i += 1
        
        elif eq[i] == "]":
            print(eq[i], "-> Right square bracket")
            i += 1

        elif eq[i] == "!":
            print(eq[i], "-> Factorial")
            i += 1
        
        elif eq[i] == "|":
            print(eq[i], "-> Straigh bracket")
            i += 1
        
        elif eq[i] == "%":
            print(eq[i], "-> Percentage")
            i += 1

        elif eq[i] == '&':
            print(eq[i], "-> Unidentified symbol")
            i += 1
        
        elif eq[i] == '@':
            print(eq[i], "-> Unidentified symbol")
            i += 1
        
        elif eq[i] == '#':
            print(eq[i], "-> Unidentified symbol")
            i += 1
        
        elif eq[i] == '~':
            print(eq[i], "-> Unidentified symbol")
            i += 1
        
        elif eq[i] == '?':
            print(eq[i], "-> Unidentified symbol")
            i += 1

        elif eq[i] == '"':
            print(eq[i], "-> Unidentified symbol")
            i += 1
        
        elif eq[i] == "'":
            print(eq[i], "-> Unidentified symbol")
            i += 1

        elif eq[i] == ":":
            if i + 1 < len(eq) and eq[i + 1] == "=":
                print(eq[i:i+2], "-> assign")
                i += 2
            else:
                print(eq[i], "-> Double dot")
                i += 1

        elif eq[i] == "/":
            if i + 1 < len(eq) and eq[i + 1] == "/":
                print(eq[i:], "-> Comment")
                break
            elif i + 1 < len(eq) and eq[i + 1] == "*":
                multipleLine.append(eq[i:])
                break
            elif i + 1 >= len(eq) or not (eq[i + 1].isnumeric() or eq[i + 1].isalpha()):
                print(eq[i], "-> Unidentified symbol")
            else:
                print(eq[i], "-> Division")
            i += 1

        elif eq[i].isalpha():
            j = i
            while j < len(eq) and (eq[j].isnumeric() or eq[j].isalpha()):
                j += 1
            print(f"{eq[i:j]} -> id")
            i = j
            
        else:
            i += 1

    line_number += 1  # Increment line number after processing each line

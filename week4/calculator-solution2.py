equations = []
multipleLine = []
temp_multiline= []
is_multiple_line = False

stores_multiline = []
# line_number = 1  # Initialize line number

while True:
    eq = input("Input an equation (or 'exit' to finish): ")
    
    if eq.lower() == 'exit':
        break

    equations.append(eq)
    # line_number += 1  

line_number = 1  # Initialize line number

for eq in equations:
    i = 0
    while i < len(eq):
        if is_multiple_line:
            temp_multiline.append(eq[i])
            # stores_multiline.append(temp_multiline)
            i += 1
            if i < len(eq) and eq[i] == "*" and i + 1 < len(eq) and eq[i + 1] == "/":
                is_multiple_line = False
                temp_multiline.append("*")
                temp_multiline.append("/")
                i += 2
        else:
            if eq[i].isnumeric():
                j = i
                while j < len(eq) and (eq[j].isnumeric() or eq[j].isalpha()):
                    j += 1
                token = eq[i:j]
                if any(c.isalpha() for c in token):
                    print(f"Unidentified token on Line {line_number}, Index {i+1} -> {token}")
                else:
                    print(token, "-> Number",eq[i])
                i = j

            elif eq[i] == "+":
                print("Addition -> ",eq[i])
                i += 1

            elif eq[i] == "-":
                print("Subtraction -> ",eq[i])
                i += 1

            elif eq[i] == "*":
                print("Multiplication -> ",eq[i])
                i += 1

            elif eq[i] == "(":
                print( "-> Left parantheses -> ",eq[i])
                i += 1

            elif eq[i] == ")":
                print( "-> Right parantheses -> ",eq[i])
                i += 1
            
            elif eq[i] == "[":
                print( "-> Left square bracket -> ",eq[i])
                i += 1
            
            elif eq[i] == "]":
                print( "-> Right square bracket -> ",eq[i])
                i += 1

            elif eq[i] == "!":
                print( "-> Factorial -> ",eq[i])
                i += 1
            
            elif eq[i] == "|":
                print( "-> Straigh bracket -> ",eq[i])
                i += 1
            
            elif eq[i] == "%":
                print( "-> Percentage -> ",eq[i])
                i += 1

            elif eq[i] == '&':
                print( "-> Unidentified symbol -> ",eq[i])
                i += 1
            
            elif eq[i] == '@':
                print( "-> Unidentified symbol -> ",eq[i])
                i += 1
            
            elif eq[i] == '#':
                print( "-> Unidentified symbol -> ",eq[i])
                i += 1
            
            elif eq[i] == '~':
                print( "-> Unidentified symbol -> ",eq[i])
                i += 1
            
            elif eq[i] == '?':
                print( "-> Unidentified symbol -> ",eq[i])
                i += 1

            elif eq[i] == '"':
                print("-> Unidentified symbol -> ",eq[i])
                i += 1
            
            elif eq[i] == "'":
                print("Unidentified symbol -> ", eq[i])
                i += 1

            elif eq[i] == ":":
                if i + 1 < len(eq) and eq[i + 1] == "=":
                    print(eq[i:i+2], "-> assign")
                    i += 2
                else:
                    print( "-> Double dot")
                    i += 1

            elif eq[i] == "/":
                if i + 1 < len(eq) and eq[i + 1] == "*":
                    is_multiple_line = True
                    temp_multiline.append("/")
                    temp_multiline.append("*")
                    i += 2
                    continue
                elif i + 1 < len(eq) and eq[i + 1] == "/":
                    print(" Comment -> ", eq[i:])
                    break
                elif i + 1 >= len(eq) or not (eq[i + 1].isnumeric() or eq[i + 1].isalpha()):
                    print(" Unidentified symbol ->",eq[i])
                else:
                    print("Division -> ", eq[i])
                i += 1

            elif eq[i].isalpha():
                j = i
                while j < len(eq) and (eq[j].isnumeric() or eq[j].isalpha()):
                    j += 1
                print(f"id -> {eq[i:j]}")
                i = j
                
            else:
                i += 1
    
    multiline = ''.join(temp_multiline)
    stores_multiline.append(multiline)
    line_number +=1
    temp_multiline.clear()
    multiline =""

    if is_multiple_line == False:
        if temp_multiline != []:
            # print(multiline, "-> Multi-line comment")
            temp_multiline.clear()

    if (stores_multiline[line_number-2]!=""):
        print(" Multi-line comment ->",stores_multiline[line_number-2])


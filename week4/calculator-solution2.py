equations = []

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
                # print(f"Line {line_number}, Index {i+1}: {token} -> Unidentified Token")
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
        elif eq[i] == "/":
            if i + 1 < len(eq) and eq[i + 1] == "/":
                print(eq[i:len(eq)], "-> Comment")
                break
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

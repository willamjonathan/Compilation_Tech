print("\n")
print("\t Calculator assignment")
print("William Jonathan Mulyadi & Alexandro Joe Claudio")
print("\n")

def userinput():
    print("Please input a mathematical equation!")
    user_input = input("Enter your expression: ")
    print("\n")
    return user_input

def scanner():
    # The map is for the all of the char from a to z is recognized as id
    valid_identifiers = ['Celsius', 'Fahrenheit', 'Kelvin'] + list(map(chr, range(97, 123))) + list(map(chr, range(65, 91)))
    # Unidentified symbols
    unidentified_symbols = ['&', '@', '#','~','"',"'","?"]  
    tokens = {
        **{var: 'id' for var in valid_identifiers},  
        ':=': 'assign',
        '(': 'lparen',
        ')': 'rparen',
        '/': 'div',
        '*': 'times',
        '+': 'plus',
        '-': 'minus',
        ':': 'double-dot',
        '[': 'left-squared-bracket',
        ']': 'right-squared-bracket',
        '!': 'factorial',
        '|': 'straight-bracket',
        '%': 'percentage',
        'NUM_PLACEHOLDER': 'number',
        # For the unidentified strings 
        'UNIDENTIFIED': 'unidentified'
    }
    # Taking user input
    user_input = userinput()
    # Processing the user input
    cur_token = ''
    input_token = []
    # For storing the actual number that is got from the user input
    nomor = []  

    # Iterates over the expression
    for char in user_input:
        #using isalnum to return character that is alphanumeric
        #jadi space gak kebaca
        if char.isalnum() or char in unidentified_symbols:
            cur_token += char
        else:
            if cur_token:
                if cur_token.isdigit():
                    nomor.append(int(cur_token))
                    input_token.append(('number', cur_token))
                elif cur_token in valid_identifiers:
                    input_token.append(('id', cur_token))
                else:
                    input_token.append(('unidentified', cur_token))
                cur_token = ''
            if char in tokens:
                input_token.append((tokens[char], char))

    if cur_token:
        if cur_token.isdigit():
            nomor.append(int(cur_token))
            input_token.append(('number', cur_token))
        elif cur_token in valid_identifiers:
            input_token.append(('id', cur_token))
        else:
            input_token.append(('unidentified', cur_token))

    for i, (lexeme, token_value) in enumerate(input_token):
        if lexeme == 'number':
            input_token[i] = ('number', str(nomor.pop(0)))

    for lexeme, token_value in input_token:
        print(f"{lexeme} -> {token_value}")


while True:
    scanner()
    print("\n")
    print("1. Do you want to try again?")
    print("2. Exit")
    
    while True:
        choice = int(input("Choose your number: "))
        if choice == 1:
            break  
        elif choice == 2:
            print("Thank you for using our program. Goodbye!")
            exit() 
        else:
            print("Invalid choice. ")
            print("Please choose between 1 or 2!")
            continue

        
        

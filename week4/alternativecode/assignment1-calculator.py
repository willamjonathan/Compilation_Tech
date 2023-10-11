# please access this link for prove of working code
# https://github.com/willamjonathan/Compilation_Tech/tree/main/week4

print("\n")
print("\t Calculator assignment")
print("William Jonathan Mulyadi & Alexandro Joe Claudio")
print("\n")

line_invalid = []
global_col_invalid = []
global_column_invalid = []
z = 0

def userinput():
    global line_invalid
    global global_col_invalid
    global z

    print("Please input a mathematical equation!")
    print("Write done if you want input to end!")
    response = []
    while True:
        user_input = input("Enter your expression: ")
        if user_input == "done":
            line_invalid = []
            global_col_invalid = []
            global_column_invalid = []
            z = 0
            break
        else:
            response.append(user_input)
    print("\n")
    return response

def linebyline(array):
    # taking multiple input of user
    global z
    for i in array:
        z += 1
        scanner(i)
        print("\n")

def scanner(indexofline):
    # The map is for the all of the char from a to z is recognized as id
    # valid_identifiers = ['Celsius', 'Fahrenheit', 'Kelvin'] + list(map(chr, range(97, 123))) + list(map(chr, range(65, 91)))
    # Unidentified symbols
    global z
    unidentified_symbols = ['&', '@', '#', '~', '"', "'", "?"]
    tokens = {
        ':=': 'assign',
        '(': 'lparen',
        ')': 'rparen',
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
        'UNIDENTIFIED': 'unidentified'
    }


    user_input = indexofline
    cur_token = ''
    input_token = []
     # For storing the actual number that is got from the user input
    nomor = []
    unidentified_indices = []  # Keep track of indices of unidentified tokens
    index_invalid = []
    tempcol_invalid = []
    chartempcol_invalid = []

    in_single_line_comment = False
    in_multi_line_comment = False

    i = 0
    while i < len(user_input):
        if in_multi_line_comment:
            if user_input[i:i+2] == '*/':
                in_multi_line_comment = False
                i += 2  # Skip the '*/' characters
                continue
            else:
                i += 1
                continue
        elif in_single_line_comment:
            if user_input[i] == '\n':
                in_single_line_comment = False
            i += 1
            continue

        if user_input[i:i+2] == '//':
            in_single_line_comment = True
            input_token.append(('comment', '//' + user_input[i+2:]))  # Include everything after '//' as a comment
            break
        elif user_input[i:i+2] == '/*':
            in_multi_line_comment = True
            i += 2  # Skip the '/*' characters
            continue

        char = user_input[i]
        #using isalnum to return character that is alphanumeric
        #jadi space gak kebaca
        if char.isalnum() or char in unidentified_symbols:
            cur_token += char
        else:
            if cur_token:
                if cur_token.isdigit():
                    nomor.append(int(cur_token))
                    input_token.append(('number', cur_token))
                else:
                    input_token.append(('id', cur_token))
                cur_token = ''
            if cur_token and cur_token in unidentified_symbols:
                input_token.append(('unidentified', cur_token))
                cur_token = ''
            if char in tokens:
                input_token.append((tokens[char], char))
            if char == '/':
                if i > 0 and i + 1 < len(user_input) and user_input[i - 1].isdigit() and user_input[i + 1].isdigit():
                    input_token.append(('div', '/'))
                else:
                    input_token.append(('unidentified', '/'))
        i += 1

    if cur_token:
        if cur_token.isdigit():
            nomor.append(int(cur_token))
            input_token.append(('number', cur_token))
        else:
            input_token.append(('id', cur_token))

    for i, (lexeme, token_value) in enumerate(input_token):
        if lexeme == 'number':
            input_token[i] = ('number', str(nomor.pop(0)))
        elif lexeme == 'id' and token_value[0].isdigit():
            input_token[i] = ('unidentified', token_value)

    invalid = 0
    col = 0
    col2 = 0
    for lexeme, token_value in input_token:
        print(f"{lexeme} -> {token_value}")
        invalid += 1
        if lexeme == 'unidentified':
            index_invalid.append(invalid)
            col = col - len(token_value)
            for char in range(len(token_value)):
                col2 += 1

        for char in range(len(token_value)):
            col += 1

        if lexeme == 'unidentified':
            if len(tempcol_invalid) == 0:
                tempcol_invalid.append(col)
            else:
                for i in range(len(tempcol_invalid)):
                    col += chartempcol_invalid[i]
                    tempcol_invalid.append(col)
        if lexeme == 'unidentified':
            chartempcol_invalid.append(col2)
            line_invalid.append(z)

    global_col_invalid.append(tempcol_invalid)
    for i in range(len(tempcol_invalid)):
        global_column_invalid.append(tempcol_invalid[i])

while True:
    temp_line = []
    linebyline(userinput())
    # buat nyamain index nya nanti dipanggil di for bawahnya
    for i in line_invalid:
            temp_line.append(i)
    for i in range(len(global_column_invalid)):
            print("Unidentified at line:", temp_line[i], "index", global_column_invalid[i])

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

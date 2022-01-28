result = None
operand = None
operator = None
wait_for_number = True

while True:
    if wait_for_number:
        character = input()
        try:
            if operator == "+":
                result = operand + float(character)
                operand = result
            elif operator == "-":
                result = operand - float(character)
                operand = result
            elif operator == "/":
                result = operand / float(character)
                operand = result
            elif operator == "*":
                result = operand * float(character)
                operand = result
            else:
                operand = float(character)
            wait_for_number = False
        except ValueError:
            print("You should enter the number")    
    else:
        character = input()
        if character in "+-/*":
            operator = character
            wait_for_number = True
        elif character == "=":
            print(result)
            break
        else:
            print("Should be '+-/*='")

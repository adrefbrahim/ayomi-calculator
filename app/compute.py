def compute_npi(expression: str):
    stack = []
    elements = expression.split()
    #print(elements)
    for element in elements:
        if element.isdigit():
            stack.append(float(element))
        else:
            # Verify if we have the suffisant elemnts to integrate in the computation
            print(stack)
            if len(stack) < 2:
                raise ValueError('Invalid Expression here')
            
            # (x 'operator' y) like (x + y)
            x = stack.pop()
            y = stack.pop()

            if element == '+':
                stack.append(x + y)
            elif element == '-':
                stack.append(x - y)
            elif element == '*':
                stack.append(x * y)
            elif element == '/':
                # Verfiy the div by zero
                if y == 0: 
                    raise ValueError('Div by zero')
                stack.append(x / y)
            else: 
                raise ValueError('Invalid Operator')
            # Verify the len of the stack for a valid expression we will finish with one element
    if len(stack) != 1:
        raise ValueError('Invalid Expression')
    return stack[0]




if __name__ == '__main__':
    expression = '5 2 + 16 1 * +'
    print(compute_npi(expression))
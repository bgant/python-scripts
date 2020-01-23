# Reverse Polish Notation Calculator
# Supercharged Python, page 80
#
# RPN Rules:
#    1) if the next item is a number, push to the of stack (end of list)
#    2) if the next item is an operator (+-*/), pop the top two off the stack (last two off the list), apply operator, and push the result

the_stack = []  # Empty global list / stack

def main():
    loop_state = True
    while loop_state:
        try:
            equation = input('Enter RPN string: ')
            if not equation:  
                break  # Exit calculator if input is blank
            print(rpn(equation))
        except KeyboardInterrupt:
            print()  # Print newline
            loop_state = False  # Exit from loop without importing sys.exit(0) module
        except:
            print('Not a valid RPN expression')

def push(item):
    the_stack.append(item)  # Push item to end of list / top of stack

def pop():
    return the_stack.pop()  #  Pop item to end of list / top of stack

def rpn(string):
    a_list = string.split() 
    if a_list[-1] not in '+-*/':  # If last item in list is not an operator (+-*/)
        return 'Not a valid RPN expression'
    else:
        for item in a_list:
            if item in '+-*/':
                op2 = pop()
                op1 = pop()
                push(eval(str(op1) + item + str(op2)))  # Execute/Evaluate string as Python command
            else:
                push(float(item))
        return pop()


if __name__ == '__main__':
    main()

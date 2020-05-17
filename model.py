from collections import deque
import numbers

ERROR_MSG = 'ERROR'

def evaluateExpression(expression):

    def _evaluateExpression(expression):
        try:
            return str(eval(expression, {}, {}))
        except Exception:
            return ERROR_MSG

    d = deque()
    str_digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    signs = {'+', '-', '*', '/'}
    float_num = False

    if expression[0] in str_digits:
        d.append(expression[0])
    elif expression[0] == '(':
        d.append(expression[0])
    else:
        return ERROR_MSG

    for el in expression[1:]:
        if el == '(' and (d[-1] == '(' or d[-1] in signs):
            d.append(el)
        elif el in str_digits:
            if d[-1] == '(' or d[-1] in signs or d[-1] in str_digits or d[-1] == '.':
                d.append(el)
        elif el in signs:
            if d[-1] in str_digits or d[-1] == ')':
                d.append(el)
        elif el == ')' and (d[-1] in str_digits or d[-1] in signs):
            d.append(el)
        elif el == '.' and d[-1] in str_digits:
            d.append(el)
        else:
            return ERROR_MSG

    return _evaluateExpression(''.join(d))


if __name__ == '__main__':
    print(evaluateExpression('(63.2-5)/6'))
    print(evaluateExpression('(24+3)*(3+2)'))
    print(evaluateExpression('69.3*3-(69/2)'))

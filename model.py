ERROR_MSG = 'ERROR'


def evaluateExpression(expression):
    try:
        return str(eval(expression, {}, {}))
    except Exception:
        return ERROR_MSG

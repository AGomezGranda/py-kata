#If else solution
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1+value2
    elif operator == '-':
        return value1-value2
    elif operator == '/':
        return value1/value2
    elif operator == '*':
        return value1*value2
    else:
        return None

#Eval solution
def basic_op_eval(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))
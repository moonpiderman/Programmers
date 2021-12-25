from itertools import permutations
def list_sort(opertator) :
    t = list(permutations(opertator, len(opertator)))
    answer_list = [ 0 for i in range(len(t)) ]
    return t, answer_list

def solution_fail(expression):
    operator = []
    expression = list(expression)

    for val in expression :
        if not val.isnumeric() :
            if val in operator :
                continue
            else :
                operator.append(val)
    # operator sort
    permu, answer_list = list_sort(operator)
    return max(answer_list)

def calcul(operator, n, ex) :
    if n == 2 :
        return str(eval(ex))
    if operator[n] == '+' :
        result = eval('+'.join([calcul(operator, n+1, e) for e in ex.split('+')]))
    if operator[n] == '-' :
        result = eval('-'.join([calcul(operator, n+1, e) for e in ex.split('-')]))
    if operator[n] == '*' :
        result = eval('*'.join([calcul(operator, n+1, e) for e in ex.split('*')]))

    return str(result)

def solution(expression) :
    answer = 0
    operators = [
        ('+', '-', '*'),
        ('+', '*', '-'),
        ('*', '-', '+'),
        ('*', '+', '-'),
        ('-', '*', '+'),
        ('-', '+', '*')
    ]
    for oper in operators :
        r = int(calcul(oper, 0, expression))
        answer = max(answer, abs(r))

    return answer


if __name__ == '__main__' :
    expression_1 = "100-200*300-500+20"
    expression_2 = "50*6-3*2"

    print(solution(expression_1))
    # print(solution(expression_2))
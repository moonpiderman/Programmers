def solution(s):
    dic = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    ret = []
    chk = []

    for i in s:
        if i.isdigit() == True:
            ret.append(i)
        elif i.isalpha() == True:
            chk.append(i)
        change = ''.join(chk)
        change.lower()
        if change in dic.keys():
            sol = dic[change]
            chk.clear()
            ret.append(sol)

    answer = int(''.join(ret))
    return answer


s = "23four5six7"

dic = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

ret = []
chk = []

for i in s :
    if i.isdigit() == True :
        ret.append(i)
    elif i.isalpha() == True :
        chk.append(i)
    change = ''.join(chk)
    if change in dic.keys():
        sol = dic[change]
        chk.clear()
        ret.append(sol)

return_value = int(''.join(ret))
print(return_value)
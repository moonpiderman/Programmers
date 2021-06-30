def solution(dartResult):
    dart_list = list(dartResult)
    point = []
    i = -1

    for x in range(len(dart_list)) :
        if dart_list[x].isdigit() :
            if dart_list[x + 1].isdigit() :
                point.append(10)
            elif dart_list[x - 1].isdigit() :
                continue
            else :
                point.append(int(dart_list[x]))
            i += 1

        else :
            if dart_list[x] == 'D':
                point[i] = pow(point[i], 2)
            elif dart_list[x] == 'T':
                point[i] = pow(point[i], 3)
            elif dart_list[x] == '*':
                if len(point) == 1:
                    point[i] *= 2
                else :
                    point[i] *= 2
                    point[i - 1] *= 2
            elif dart_list[x] == '#':
                point[i] *= -1

    return sum(point)

if __name__ == '__main__' :
    dartResult_1 = "1S2D*3T"
    dartResult_2 = "1D2S#10S"
    dartResult_3 = "1D2S0T"
    dartResult_4 = "1S*2T*3S"
    dartResult_5 = "1D#2S*3S"
    dartResult_6 = "1T2D3D#"
    dartResult_7 = "1D2S3T*"

    print(solution(dartResult_7))
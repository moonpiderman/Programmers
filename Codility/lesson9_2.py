def sol(A):
    parti = 0
    maxi = -1000000

    for val in A:
        maxi = max(maxi, parti + val)
        parti = max(0, parti + val)
    return maxi

if __name__ == '__main__':
    A = [3, 2, -6, 4, 0]
    print(sol(A))
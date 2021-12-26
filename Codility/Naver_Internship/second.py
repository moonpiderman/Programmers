# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from extratypes import Tree  # library with types used in the task


def tree(T, initial):
    if T.r == None and T.l == None:
        return initial
    elif T.r == None:
        if T.l.x not in initial:
            initial.append(T.l.x)
            return tree(T.l, initial)
        else:
            return tree(T.l, initial)

    elif T.l == None:
        if T.r.x not in initial:
            initial.append(T.r.x)
            return tree(T.r, initial)
        else:
            return tree(T.r, initial)
    else:
        left = tree(T.l, initial)
        right = tree(T.r, initial)
        if len(left) > len(right):
            return tree(T.l, initial)
        elif len(left) < len(right):
            return tree(T.r, initial)
        else:


def solution(T):
    initial = [T.x]
    tree(T, initial)
    return len(initial)


if __name__ == '__main__':

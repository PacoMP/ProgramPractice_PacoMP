

a, lst = int(input()), input().split()
lst = [int(ch) for ch in lst]

#========MAIN==============

def is_modal(a, lst):
    i = 1
    for i in range(i, a):
        if not (lst[i - 1] < lst[i]):
            break
    else:
        return "YES"

    for i in range(i, a):
        if not (lst[i - 1] == lst[i]):
            break
    else:
        return "YES"

    for i in range(i, a):
        if not (lst[i - 1] > lst[i]):
            return "NO"
    else:
        return "YES"

print(is_modal(a, lst))

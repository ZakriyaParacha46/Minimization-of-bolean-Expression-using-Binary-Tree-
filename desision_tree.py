from itertools import product


size = 6
val = ["A", "B", "C", "D", "E", "G"]
inputs = [list(item) for item in product([False, True], repeat=size)]
minterm = [0]

solution = ""


def min(s, inp):
    mint = list()
    for i in range(2**s):
        if (i in minterm):
            mint.append(inp[i])

    return mint


def entropy(inp):
    ent = [0]*len(inp[0])

    for x, i in enumerate(inp[0]):
        if (i == " "):
            ent[x] = 100

    f = [inp[0][0]]
    for i in inp[0]:
        f.append(i)

    for i in range(len(inp[0])):
        for j in inp:
            if(j[i] != f[i]):
                f[i] = not(f[i])
                ent[i] = ent[i]+1
    return ent


def minim(arr):
    index = 0
    value = 100
    for x, i in enumerate(arr):
        if (i < value):
            value = i
            index = x
    return index


def best_dev(solution, arr):

    flag = True
    for i in entropy(arr):
        if (i != 100):
            flag = False
    if (flag):
        return solution

    ind = minim(entropy(arr))
    left, right = [], []
    print("Break at:", val[ind])

    for j in arr:

        if(j[ind]):
            j[ind] = " "
            left.append(j)
        else:
            j[ind] = " "
            right.append(j)

    if (len(right) == 0):
        print("left", left)
        return best_dev(solution + val[ind], left)

    elif (len(left) == 0):
        print("Right", right)
        return best_dev(solution + "!" + val[ind], right)

    else:
        print("left", left, "right", right)
        if(right == left):
            return solution
        return best_dev(solution + val[ind], left) + "+ " + best_dev(solution + "!"+val[ind], right)


print(min(size, inputs))
print(best_dev(solution, min(size, inputs)))

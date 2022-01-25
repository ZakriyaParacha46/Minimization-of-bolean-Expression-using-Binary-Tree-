from sympy import *
from itertools import product
import copy
import random
import time
import numpy as np

val = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
       "O", "P", "Q", "R", "S", "T", "U", "V"]


# worsecase sinario
# minterm = [0, 3, 5, 6,  12, 15, 9, 10,  17, 18, 20, 23, 29, 30, 24, 27]
# minterm = [0, 3, 5, 6,  12, 15, 9, 10,  17, 18, 20, 23, 29, 30, 24, 27]
# minterm = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 31]


class B_tree:
    def entropy(self, inp):
        ent = [0]*len(inp[0])
        for x, i in enumerate(inp[0]):
            if (i == " "):
                ent[x] = 100

        f = [i for i in inp[0]]

        for i in range(len(inp[0])):
            for j in inp:
                if(j[i] != f[i]):
                    f[i] = not(f[i])
                    ent[i] = ent[i]+1
        return ent

    def tight(self, s1, s2, sol):
        l1 = s1.split("+")
        l2 = s2.split("+")

        try:
            l1.remove("")
        except:
            pass

        try:
            l2.remove("")
        except:
            pass

        for l, m in enumerate(l1):
            if (m not in l2):
                l1[l] = sol+m

        for n, k in enumerate(l2):
            if (k not in l1):
                l2[n] = sol+k

        # print("Tight:", s1, s2)
        return("+".join(list(set(l1+l2))))

    def possible(self, l):
        global c
        if(len(l) == 1):
            return false
        return true
        for x in l:
            for y in l:
                m = 0
                print(x, y)
                for i, j in zip(x, y):
                    print(i, j)
                    if (i != j):
                        m = m+1

                if (m != 1):
                    return true

        return false

    def arrtostr(self, arr):
        a = ""
        for x, i in enumerate(arr):
            if (i == 1):
                a = a+val[x]
            elif (i == 0):
                a = a+"!"+val[x]

        return a

    def best_dev(self, solution, arr, memo={}):
        if (not self.possible(arr)):
            for i in arr:
                solution = solution + self.arrtostr(i)
            return solution

        if (str(arr) in memo.keys()):
            #print("memo", memo)
            # print(str(arr))
            # print("y")
            return self.tight(memo[str(arr)][0], memo[str(arr)][1], solution)

        global c
        c = c+1

        temp = copy.deepcopy(arr)
        ind = self.entropy(arr).index(min(self.entropy(arr)))
        left, right = [], []
        # print("Break at:", val[ind])
        for j in arr:
            if(j[ind]):
                j[ind] = " "
                left.append(j)
            else:
                j[ind] = " "
                right.append(j)

       # catch for repetition inlft right block
        if(right == left):
            return solution

        if (len(right) == 0):
            # print("left", left)
            memo[str(temp)] = [self.best_dev(val[ind], left, memo), ""]
            return self.tight(memo[str(temp)][0], memo[str(temp)][1], solution)

        elif (len(left) == 0):
            # print("Right", right)
            memo[str(temp)] = ["", self.best_dev("!"+val[ind], right, memo)]
            return self.tight(memo[str(temp)][0], memo[str(temp)][1], solution)

        else:
            # print("left", left, "right", right)
            # memo[str(arr)] = self.best_dev(solution + val[ind], left) + \
            #    "+" + self.best_dev(solution + "!"+val[ind], right)

            memo[str(temp)] = [self.best_dev(val[ind], left, memo),
                               self.best_dev("!"+val[ind], right, memo)]

            return self.tight(memo[str(temp)][0], memo[str(temp)][1], solution)


size = 3
inputs = [list(item) for item in product([False, True], repeat=size)]

"""
c = 0
minterm = [0, 1]
print(minterm)
mint = [inputs[i] for i in range(2**size) if i in minterm]
b = B_tree()
bd = b.best_dev("", copy.deepcopy(mint))
print("Implicants:", bd)
print(c)
"""

arrc = []
arrt = []
for i in range(50):
    minterm = list(np.random.randint(
        low=1, high=(2**size) - 1, size=random.randrange(1, 2**(size-1))))

    mint = [inputs[i] for i in range(2**size) if i in minterm]

    c = 0
    print()
    print(str(i)+"_________________________-")
    print(set(minterm))
    # print(mint)

    start_time = time.time()
    b = B_tree()
    bd = b.best_dev("", copy.deepcopy(mint), {})
    print("Implicants:", bd)
    print("count=: ", c)
    arrc.append(c)
    print("_________________________-")
    end_time = time.time()
    arrt.append(end_time - start_time)

print("no of data:", len(arrc), "\n\navgtime:", sum(
    arrt)/len(arrt), "\nmintime:", min(arrt), "\nmax:", max(arrt))

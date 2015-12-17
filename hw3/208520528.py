#Skeleton file for HW3 - Winter 2015-2016 - extended intro to CS

#Add your implementation to this file

#You may add other utility functions to this file,
#but you may NOT change the signature of the existing ones.

#Change the name of the file to your ID number (extension .py).

############
# QUESTION 2
############


def find_root(f, a, b, EPS=0.001):
    fa = f(a)
    fb = f(b)
    if not (fa < 0 < fb) and not (fa > 0 > fb):
        return None

    is_below_zero = fa < 0
    for e in range(1, int((b-a)/EPS+1)):
        val = f(a + e*EPS)
        if val == 0 or (is_below_zero and val > 0) or (not is_below_zero and val < 0):
            return a + e*EPS

    return None


############
# QUESTION 3
############

# b
def multi_merge_v2(lst_of_lsts):
    size = 0
    for l in lst_of_lsts:
        size += len(l)

    indices = len(lst_of_lsts)*[0]
    result = []
    while len(result) < size:
        minimum_index = 0
        for i in range(1, len(lst_of_lsts)):
            if not indices[minimum_index] < len(lst_of_lsts[minimum_index]):
                minimum_index = i
            elif lst_of_lsts[i][indices[i]] \
                    < lst_of_lsts[minimum_index][indices[minimum_index]]:
                minimum_index = i

        result.append(lst_of_lsts[minimum_index][indices[minimum_index]])
        indices[minimum_index] += 1

    return result


def merge(lst1, lst2):
    """ merging two ordered lists using
        the two pointer algorithm """
    n1 = len(lst1)
    n2 = len(lst2)
    lst3 = [0 for i in range(n1 + n2)]  # alocates a new list
    i = j = k = 0  # simultaneous assignment
    while (i < n1 and j < n2):
        if (lst1[i] <= lst2[j]):
            lst3[k] = lst1[i]
            i = i +1
        else:
            lst3[k] = lst2[j]
            j = j + 1
        k = k + 1  # incremented at each iteration
    lst3[k:] = lst1[i:] + lst2[j:]  # append remaining elements
    return lst3


# c
def multi_merge_v3(lst_of_lsts):
    m = len(lst_of_lsts)
    merged = []

    for l in lst_of_lsts:
        merged = merge(merged, l)

    return merged



############
# QUESTION 5
############
def sort_num_list(lst):
    count = [0]*200001

    for i in lst:
        val = int(format(i, '.2f').replace('.', ''))
        count[val + 100000] += 1

    result = []
    for i in range(200001):
        result.extend([(i - 100000)/100]*count[i])

    return result

############
# QUESTION 6
############

from random import *

def diff_param(f,h=0.001):
    return (lambda x: (f(x+h)-f(x))/h)


def NR(func, deriv, epsilon=10**(-8), n=100, x0=None):
    if x0 is None:
        x0 = uniform(-100.,100.)
    x=x0; y=func(x)
    for i in range(n):
        if abs(y)<epsilon:
            #print (x,y,"convergence in",i, "iterations")
            return x
        elif abs(deriv(x))<epsilon:
            #print ("zero derivative, x0=",x0," i=",i, " xi=", x)
            return None
        else:
            #print(x,y)
            x = x- func(x)/deriv(x)
            y = func(x)
    #print("no convergence, x0=",x0," i=",i, " xi=", x)
    return None


# b1
def source(f,y):
    return NR(lambda x: f(x)-y, diff_param(f))


# b2
def inverse(f):
    return lambda y: source(f, y)


########
# Tester
########

def test():

    f1 = lambda x : x - 1
    res = find_root(f1 , -10, 10)
    EPS=0.001
    if res == None or abs(f1(res)) > EPS  or \
       find_root(lambda x : x**2  , -10, 10) != None:
        print("error in find_root")


    if multi_merge_v2([[1,2,2,3],[2,3,5],[5]]) != [1, 2, 2, 2, 3, 3, 5, 5] :
        print("error in multi_merge_v2")

    if multi_merge_v3([[1,2,2,3],[2,3,5],[5]]) != [1, 2, 2, 2, 3, 3, 5, 5] :
        print("error in multi_merge_v3")


    if sort_num_list([18.33, -2.5, 0.0, 12.57, -30.0, 0.0]) \
       != [-30.0, -2.5, 0.0, 0.0, 12.57, 18.33]:
        print("error in sort_num_list")


    lin = lambda x: x+3
    if source(lin,5) == None or abs(source(lin,5) - 2.0000000003798846) > 10**-7:
        print("error in source")

    if inverse(lin) == None or abs(inverse(lin)(5) - 1.9999999998674198) > 10**-7:
        print("error in inverse")


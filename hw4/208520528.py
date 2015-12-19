# Skeleton file for HW4 - Winter 2015-2016 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to your ID number (extension .py).

import random


############
# QUESTION 1
############
def max1(L):
    if len(L) == 1:
        return L[0]
    return max(L[0], max1(L[1:]))


def max11(L, left, right):
    if left == right:
        return L[left]
    return max(L[left], max11(L, left + 1, right))


def max_list11(L):
    return max11(L, 0, len(L) - 1)


def max2(L):
    if len(L) == 1:
        return L[0]
    l = max2(L[:len(L) // 2])
    r = max2(L[len(L) // 2:])
    return max(l, r)


def max22(L, left, right):
    if left == right:
        return L[left]
    sep = left + ((right - left + 1) // 2)
    l = max22(L, left, sep - 1)
    r = max22(L, sep, right)
    return max(l, r)


def max_list22(L):
    return max22(L, 0, len(L) - 1)


############
# QUESTION 2
############
def optimal_cruise(ship_prices):
    lst = [-1] * len(ship_prices)
    optimal_cruise_internal(ship_prices, 0, lst)
    return lst[0]


def optimal_cruise_internal(ship_prices, start, lst):
    if start == len(ship_prices) - 1:
        lst[start] = ship_prices[start][len(ship_prices)]
        return

    optimal_cruise_internal(ship_prices, start + 1, lst)
    minimum = min(range(start + 1, len(lst)), key=lst.__getitem__)
    lst[start] = min(ship_prices[start][minimum] + lst[minimum],
                     ship_prices[start][len(ship_prices)])


def optimal_cruise_seasick(toilet_prices):
    return optimal_cruise_seasick_internal(toilet_prices, 0)[0]


def optimal_cruise_seasick_internal(toilet_prices, start):
    n = len(toilet_prices)

    if start == len(toilet_prices) - 3:
        return [toilet_prices[n - 1], toilet_prices[n - 1]]

    lst = optimal_cruise_seasick_internal(toilet_prices, start + 1)
    return [min(toilet_prices[start + 1] + lst[0], toilet_prices[start + 2] + lst[1]),
            lst[0]]


############
# QUESTION 3
############
def solve_puzzle(lst):
    mem = [0] * len(lst)
    visited = [False] * len(lst)
    return solvable(lst, 0, mem, visited)


def solvable(lst, i, mem, visited):
    visited[i] = True

    if lst[i] == 0:
        return True

    if i + lst[i] < len(lst) and not visited[i + lst[i]]:
        return solvable(lst, i + lst[i], mem, visited)

    if i - lst[i] >= 0 and not visited[i - lst[i]]:
        return solvable(lst, i + lst[i], mem, visited)

    return False


############
# QUESTION 4
############
def choose_sets(lst, k):
    return choose_sets_internal(lst, 0, k)


def choose_sets_internal(lst, start, k):
    if k == 0:
        return [[]]
    if len(lst) - start < k:
        return []

    including = choose_sets_internal(lst, start + 1, k-1)
    for i in range(0, len(including)):
        including[i].insert(0, lst[start])

    excluding = choose_sets_internal(lst, start + 1, k)

    including.extend(excluding)

    return including


############
# QUESTION 5
############
def is_prime(m, show_witness=False):
    """ probabilistic test for m's compositeness """
    for i in range(0, 100):
        a = random.randint(1, m - 1)  # a is a random integer in [1..m-1]
        if pow(a, m - 1, m) != 1:
            if show_witness:  # caller wishes to see a witness
                print(m, "is composite", "\n", a, "is a witness, i=", i + 1)
            return False
    return True


def density_primes(n, times=10000):
    count = 0
    for i in range(0, times):
        tested = random.randint(2 ** (n - 1), 2 ** n - 1)
        if is_prime(tested):
            count += 1

    return count / times


########
# Tester
########
def test():
    # Q1 basic tests

    if max_list22([1, 20, 3]) != 20:
        print("error in max22()")
    if max_list22([1, 20, 300, 400]) != 400:
        print("error in max22()")

    # Q2 basic tests
    if optimal_cruise([[0, 20, 30], [0, 0, 60]]) != 30:
        print("error in optimal_cruise()")
    if optimal_cruise([[0, 20, 3000], [0, 0, 60]]) != 80:
        print("error in optimal_cruise()")
    if optimal_cruise_seasick([10, 200, 30, 100]) != 130:
        print("error in optimal_cruise_seasick()")
    if optimal_cruise_seasick([10, 20, 30, 100]) != 120:
        print("error in optimal_cruise_seasick()")

    # Q3 basic tests
    if solve_puzzle([3, 1, 2, 3, 0]) != False:
        print("error in solvable()")
    if solve_puzzle([4, 18, 1, 5, 3, 4, 9, 2, 1, 0]) != True:
        print("error in solvable()")

    # Q4 basic tests
    if choose_sets([1, 2, 3, 4], 0) != [[]]:
        print("error in choose_sets()")
    tmp = choose_sets(['a', 'b', 'c', 'd', 'e'], 4)
    if tmp == None:
        print("error in choose_sets()")
    else:
        tmp = sorted([sorted(e) for e in tmp])
        if tmp != [['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'e'], ['a', 'b', 'd', 'e'], ['a', 'c', 'd', 'e'],
                   ['b', 'c', 'd', 'e']]:
            print("error in choose_sets()")

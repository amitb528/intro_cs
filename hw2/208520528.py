# Skeleton file for HW2 - Winter 2015-2016 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to your ID number (extension .py).

import math

############
# QUESTION 1
############


# 1c
def reverse_sublist(lst, start, end):
    for i in range(0, (end - start) // 2):
        temp = lst[i + start]
        lst[i + start] = lst[end - 1 - i]
        lst[end - 1 - i] = temp


# 1d
def divide_list(lst):
    if len(lst) == 0:
        return

    pivot = lst[0]
    pivot_index = 0
    for i in range(1, len(lst)):
        val = lst[i]
        if val < pivot:
            lst[pivot_index] = val
            pivot_index += 1
            lst[i] = lst[pivot_index]
            lst[pivot_index] = pivot


############
# QUESTION 2b
############

def power_new(a, b):
    """ computes a**b using iterated squaring """
    result = 1
    b_bin = bin(b)[2:]
    reverse_b_bin = b_bin[::-1]
    for bit in reverse_b_bin:
        if int(bit) % 2 == 1:
            result *= a
        a = a*a
    return result


############
# QUESTION 3b
############

def inc(b):
    l = list(b)
    for i in reversed(range(len(l))):
        if l[i] == '1':
            l[i] = '0'
        else:
            l[i] = '1'
            return str.join('', l)
    return '1'+str.join('', l)

############
# QUESTION 4b
############


def sum_divisors(n):
    if n == 1:
        return 0
    s = 0
    for i in range(1, math.floor(math.sqrt(n)) + 1):
        d = n/i
        if d.is_integer():
            s += i
            if d < n and d != i:
                s += int(d)
    return s


def is_finite(n):
    if n in is_finite.list:
        is_finite.list = list()
        return False
    s = sum_divisors(n)
    if s == 0:
        is_finite.list = list()
        return True
    else:
        is_finite.list.append(n)
        return is_finite(s)
is_finite.list = list()


def cnt_finite(limit):
    s = 0
    for i in range(1, limit+1):
        if is_finite(i):
            s += 1
    return s


############
# QUESTION 5
############

def largest_subnumber(n, k):
    l = [int(x) for x in str(n)]
    bigest = n//pow(10, len(l)-k)
    bigest_index = 0
    prev = bigest
    power = pow(10, k-1)
    for i in range(1, len(l)-k + 1):
        prev = (prev - l[i-1] * power)*10 + l[i-1+k]
        if bigest < prev:
            bigest = prev
            bigest_index = i
    return bigest_index

########
# Tester
########


def test():
    lst = [1, 2, 3, 4, 5]
    reverse_sublist(lst, 0, 4)
    if lst != [4, 3, 2, 1, 5]:
        print("error in reverse_sublist()")
    lst = ["a", "b"]
    reverse_sublist(lst, 0, 1)
    if lst != ["a", "b"]:
        print("error in reverse_sublist()")

    lst = [1, 2, 3, 4, 5]
    divide_list(lst)
    if lst[0] != 1:
        print("error in divide_list()")
    lst = [3, 2, 1, 4, 5]
    divide_list(lst)
    if lst[0] >= 3 or \
                    lst[1] >= 3 or \
                    lst[2] != 3 or \
                    lst[3] <= 3 or \
                    lst[4] <= 3:
        print("error in divide_list()")

    if power_new(2, 3) != 8:
        print("error in power_new()")

    if inc("0") != "1" or \
                    inc("1") != "10" or \
                    inc("101") != "110" or \
                    inc("111") != "1000" or \
                    inc(inc("111")) != "1001":
        print("error in inc()")

    if sum_divisors(6) != 6 or \
                    sum_divisors(4) != 3:
        print("error in sum_divisors()")

    if is_finite(6) or \
            not is_finite(4):
        print("error in is_finite()")

    if cnt_finite(6) != 5:
        print("error in cnt_finite()")

    if largest_subnumber(37295, 4) != 1 or \
                    largest_subnumber(37295, 2) != 3 or \
                    largest_subnumber(7 ** 23489, 9925) != 2325 or \
                    largest_subnumber(int('1' * len(str(7 ** 23489))), 9925) != 0:
        print("error in largest_subnumber()")

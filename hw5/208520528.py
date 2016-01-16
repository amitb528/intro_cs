# Skeleton file for HW5 - Winter 2016 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to your ID number (extension .py).


############
# QUESTION 1
############

class DoublyLinkedNode:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.value)


class Deque:
    def __init__(self):
        self._head = None  # type: DoublyLinkedNode
        self._tail = None  # type: DoublyLinkedNode
        self._len = 0

    def __len__(self):
        return self._len

    def __repr__(self):
        def nxt():
            n = self._head
            while n is not None:
                yield str(n.value)
                n = n.next

        return " ".join(nxt())

    def head_insert(self, item):
        node = DoublyLinkedNode(item)
        if self._head is None:
            self._head = node
            self._tail = self._head
        else:
            node.next = self._head
            self._head.prev = node

            self._head = node

        self._len += 1

    def tail_insert(self, item):
        node = DoublyLinkedNode(item)
        if self._tail is None:
            self._head = node
            self._tail = self._head
        else:
            node.prev = self._tail
            self._tail.next = node

            self._tail = node

        self._len += 1

    def head_remove(self):
        if self._head is None:
            return

        if self._head is self._tail:
            self._head = self._tail = None
        else:
            nxt = self._head.next
            nxt.prev = None
            self._head = nxt

        self._len -= 1

    def tail_remove(self):
        if self._tail is None:
            return

        if self._head is self._tail:
            self._head = self._tail = None
        else:
            prev = self._tail.prev
            prev.next = None
            self._tail = prev

        self._len -= 1

    def head(self):
        if self._head is None:
            return None
        else:
            return self._head.value

    def tail(self):
        if self._tail is None:
            return None
        else:
            return self._tail.value

    def __getitem__(self, k):
        return self.get_node(k).value

    def __setitem__(self, k, item):
        self.get_node(k).value = item

    def get_node(self, k):
        assert 0 <= k < self._len

        if k <= self._len - 1 - k:
            i = 0
            n = self._head
            while i < k:
                n = n.next
                i += 1
        else:
            i = self._len - 1
            n = self._tail
            while i > k:
                n = n.prev
                i -= 1

        return n


############
# QUESTION 2
############


### Tree node class - code from lecture ###
class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None  # type: TreeNode
        self.right = None  # type: TreeNode

    def __repr__(self):
        return "[" + str(self.left) + \
               " (" + str(self.key) + "," + str(self.val) + ") " \
               + str(self.right) + "]"


### Binary search tree  ###
class BSearch_tree():
    def __init__(self):
        self.root = None  # type: TreeNode

    def insert(self, key, val):
        if self.root is None:
            self.root = TreeNode(key, val)
            return

        def internal(node, key, val):
            if node.key == key:
                node.val = val
            elif key < node.key:
                if node.left is None:
                    node.left = TreeNode(key, val)
                else:
                    internal(node.left, key, val)
            else:
                if node.right is None:
                    node.right = TreeNode(key, val)
                else:
                    internal(node.right, key, val)

        internal(self.root, key, val)

    def lookup(self, key):
        def internal(node, key):
            if node is None:
                return None

            if key == node.key:
                return node.val
            elif key < node.key:
                return internal(node.left, key)
            else:
                return internal(node.right, key)

        return internal(self.root, key)

    def min(self):
        if self.root is None:
            return None

        def internal(node):
            if node.left is not None:
                return internal(node.left)
            else:
                return node.key

        return internal(self.root)

    def find_closest_key(self, search_key):
        if self.root is None:
            return None

        def internal(node, search_key):
            if search_key < node.key:
                if node.left is None:
                    return node.key
                compare = internal(node.left, search_key)
            else:
                if node.right is None:
                    return node.key
                compare = internal(node.right, search_key)

            if abs(node.key - search_key) <= abs(compare - search_key):
                return node.key
            else:
                return compare

        return internal(self.root, search_key)

    def is_balanced(self):
        if self.root is None:
            return None

        def internal(node):
            if node.left is None and node.right is None:
                return 0

            if node.left is not None:
                left = internal(node.left)
                if node.right is not None:
                    right = internal(node.right)
                    if left != -1 and right != -1 and abs(left - right) <= 1:
                        return max(left, right) + 1
                    else:
                        return -1
                else:
                    return 1 if left == 0 else -1
            else:
                right = internal(node.right)
                return 1 if right == 0 else -1

        return internal(self.root) != -1


############
# QUESTION 3
############

#########################################
### SimpleDict CODE ###
#########################################
class SimpleDict:
    def __init__(self, m, hash_func=hash):
        """ initial hash table, m empty entries """
        self.table = [[] for i in range(m)]
        self.hash_mod = lambda x: hash_func(x) % m

    def __repr__(self):
        L = [self.table[i] for i in range(len(self.table))]
        return "".join([str(i) + " " + str(L[i]) + "\n" for i in range(len(self.table))])

    def items(self):
        return [item for chain in self.table for item in chain]

    def values(self):
        return [item[1] for chain in self.table for item in chain]

    def find(self, key):
        """ returns value if key in hashtable, None otherwise  """
        h = self.hash_mod(key)
        chain = self.table[h]
        for item in chain:
            if item[0] == key:
                return item[1]
        return None

    def insert(self, key, value):
        """ insert an item into table
            if key already exists - update value
            key must be hashable """
        h = self.hash_mod(key)
        chain = self.table[h]
        for item in chain:
            if item[0] == key:
                item[1] = value
                return
        chain.append([key, value])


#########################################
### SimpleDict CODE ###
#########################################


def clean(text):
    ''' converts text to lower case, then replaces all characters except
       letters, spaces, newline and carriage return by spaces '''
    letter_set = "abcdefghijklmnopqrstuvwxyz \n\r"
    text = str.lower(text)
    cleaned = ""
    for letter in text:
        if letter in letter_set:
            cleaned += letter
        else:
            cleaned += " "
    return cleaned


def count_words(words):
    d = SimpleDict(200)
    for word in words:
        count = d.find(word)
        d.insert(word, count + 1 if count is not None else 1)
    return d


def sort_by_cnt(count_dict):
    return sorted([tuple(item) for item in count_dict.items()],
                  key=lambda x: x[1], reverse=True)


############
# QUESTION 4
############

def SomePairs():
    i = 1
    j = 0
    while True:
        while j < i:
            yield (i, j)
            j += 1
        i += 1
        j = 0


def RevGen(PairsGen):
    g = PairsGen()
    while True:
        couple = next(g)
        yield (couple[1], couple[0])


def UnionGenerators(gen1, gen2):
    while True:
        yield next(gen1)
        yield next(gen2)


def EqPairs():
    n = 0
    while True:
        yield (n, n)
        n += 1


def AllPairs():
    greater_smaller = SomePairs()
    smaller_greater = RevGen(SomePairs)
    equal = EqPairs()
    gen = UnionGenerators(greater_smaller, smaller_greater)
    gen = UnionGenerators(gen, equal)
    while True:
        yield next(gen)


############
# QUESTION 5
############

from matrix import *


# a
def upside_down(im):
    n, m = im.dim()
    im2 = Matrix(n, m)
    for i in range(n):
        for j in range(m):
            im2[i, j] = im[n-i-1, j]
    return im2


# b
## Local denoising methods
def copy(mat):
    ''' brand new copy of matrix '''
    n, m = mat.dim()
    new = Matrix(n, m)
    for i in range(n):
        for j in range(m):
            new[i, j] = mat[i, j]
    return new


def items(mat):
    '''flatten mat elements into a list'''
    n, m = mat.dim()
    lst = [mat[i, j] for i in range(n) for j in range(m)]
    return lst


def local_operator(A, op, k=1):
    n, m = A.dim()
    res = copy(A)  # brand new copy of A
    for i in range(k, n - k):
        for j in range(k, m - k):
            res[i, j] = op(items(A[i - k:i + k + 1, j - k:j + k + 1]))
    return res


def modified_local_medians(A, k=1):
    return local_operator(A, modified_median, k)


def modified_median(lst):
    px = lst[len(lst)//2]
    l = list()
    if px < 5:
        for i in lst:
            if i >= 5:
                l.append(i)
        return median(l) if len(l) != 0 else px
    elif px > 250:
        for i in lst:
            if i <= 250:
                l.append(i)
        return median(l) if len(l) != 0 else px
    else:
        return px


def average(lst):
    l = len(lst)
    return round(sum(lst)/l)


def median(lst):
    sort_lst = sorted(lst)
    l = len(sort_lst)
    if l%2==1:    # odd number of elements. well defined median
        return sort_lst[l//2]
    else:         # even number of elements. average of middle two
        return (int(sort_lst[-1+l//2]) + int(sort_lst[l//2])) // 2


def local_means(A, k=1):
    return local_operator(A, average, k)


def local_medians(A, k=1):
    return local_operator(A, median, k)


########
# Tester
########

def test():
    # Question 1
    dq = Deque()
    dq.head_insert(1)
    dq.head_insert(2)
    dq.head_insert(3)
    if (dq.__repr__() != "3 2 1"):
        print("error in Deque")
    dq.tail_insert(4)
    if (dq.__repr__() != "3 2 1 4"):
        print("error in Deque")
    dq.head_remove()
    if (dq.__repr__() != "2 1 4"):
        print("error in Deque")
    dq.tail_remove()
    if (dq.__repr__() != "2 1"):
        print("error in Deque")
    if (dq.head() == None):
        print("error in Deque")
    if (dq.head() != None and dq.head() != 2):
        print("error in Deque")
    if (dq.tail() == None):
        print("error in Deque")
    if (dq.tail() != None and dq.tail() != 1):
        print("error in Deque")
    dq.head_insert(4)
    dq.head_insert(5)
    if (dq[1] != 4):
        print("error in Deque")
    dq[1] = 30
    if (dq.__repr__() != "5 30 2 1"):
        print("error in Deque")

    # Question 2

    bin_tree = BSearch_tree()
    bin_tree.insert(2, "hi")
    bin_tree.insert(4, "bye")
    bin_tree.insert(1, "hello")
    bin_tree.insert(3, "lovely")

    if (bin_tree.min() != 1):
        print("error in BSearch_Tree")
    if (bin_tree.lookup(3) != "lovely"):
        print("error in BSearch_Tree")
    if (bin_tree.lookup(100) != None):
        print("error in BSearch_Tree")
    if (bin_tree.find_closest_key(5) != 4):
        print("error in BSearch_Tree")
    if (bin_tree.is_balanced() != True):
        print("error in BSearch_Tree")
    bin_tree.insert(5, "dear")
    if (bin_tree.is_balanced() != True):
        print("error in BSearch_Tree")
    bin_tree.insert(6, "tea")
    if (bin_tree.is_balanced() != False):
        print("error in BSearch_Tree")

    # Question 3
    dc = SimpleDict(5)
    dc.insert("a", 10)
    dc.insert("b", 20)
    if (dc.find("a") != 10):
        print("error in SimpleDict.find()")
    if (dc.find(10) != None):
        print("error in SimpleDict.find()")
    dc.insert("a", 100)
    if (dc.find("a") != 100):
        print("error in SimpleDict.find()")
    if (dc.values() == None):
        print("error in SimpleDict.values()")
    if (dc.values() != None and sorted(dc.values()) != [20, 100]):
        print("error in SimpleDict.values()")

    h = SimpleDict(200)
    h.insert("ab", 2)
    h.insert("ef", 1)
    h.insert("cd", 3)
    if len(h.items()) != 3:
        print("error in SimpleDict.insert()")
    if h.find("ab") != 2:
        print("error in SimpleDict.find()")
    if h.find("ef") != 1:
        print("error in SimpleDict.find()")
    if h.find("cd") != 3:
        print("error in SimpleDict.find()")
    if h.find("xx") != None:
        print("error in SimpleDict.find()")

    d = count_words(["ab", "cd", "cd", "ef", "cd", "ab"])
    if d is None:
        print("error in count_words()")
    if d != None and d.items() != None and len(d.items()) != 3:
        print("error in count_words()")
    if d != None and d.find("ab") != 2:
        print("error in count_words()")
    if d != None and d.find("ef") != 1:
        print("error in count_words()")
    if d != None and d.find("cd") != 3:
        print("error in count_words()")
    if d != None and sort_by_cnt(d) != [('cd', 3), ('ab', 2), ('ef', 1)]:
        print("error in sort_by_cnt()")

    # Question 4
    def f():
        return ((i, 2 * i) for i in range(4))

    gen = RevGen(f)
    if gen is None:
        print("error in RevGen()")
    if gen != None and {(x, y) for (x, y) in gen} != {(6, 3), (4, 2), (0, 0), (2, 1)}:  # order of pairs does not matter
        print("error in RevGen()")

    gen = SomePairs()
    l = list()
    for i in range(1000):
        l.append(next(gen))
    if (4, 2) not in l or (7, 2) not in l or (2, 2) in l \
            or (3, 1) not in l:
        print("error in SomePairs()")

    gen = RevGen(SomePairs)
    l = list()
    for i in range(1000):
        val = next(gen)
        if val[0] > val[1]:
            print("error in RevGen() i > j")
        l.append(val)
    if (4, 7) not in l or (2, 8) not in l or (2, 2) in l:
        print("error in RevGen()")

    gen = AllPairs()
    l = list()
    for i in range(10000):
        l.append(next(gen))
    i = 5
    if (5, 5) not in l or (2, 6) not in l or \
            (7, 8) not in l or (9, 2) not in l:
        print("error in AllPairs()")

    print("done")


def test_images():
    im = Matrix.load('atallbuilding.bitmap')
    for i in range(1,4):
        im2 = im
        im2 = modified_local_medians(im2, i)
        im2.display('env'+str(i))

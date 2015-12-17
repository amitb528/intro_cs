import amit
import math

print("2.1;")
print(amit.find_root(lambda x: x - 2.5, -10, 10))
print(amit.find_root(lambda x: pow(x, 2) - 4.2, -1, 9))
print(amit.find_root(lambda x: math.log(x, 5) - 1.88, 10, 30))
print()

print("3.2")
print(amit.multi_merge_v2([[1,2,3],[1,6,8],[4,6,8]]))
print(amit.multi_merge_v2([[1,2,3],[1,2,3],[1,2,3]]))
print(amit.multi_merge_v2([[1,2,3],[4,5,6],[1,7,8]]))
print()

print("3.3")
print(amit.multi_merge_v3([[1,2,3],[1,6,8],[4,6,8]]))
print(amit.multi_merge_v3([[1,2,3],[1,2,3],[1,2,3]]))
print(amit.multi_merge_v3([[1,2,3],[4,5,6],[1,7,8]]))
print()

print("5")
print(amit.sort_num_list([1,2,3,5,6,6,7]))
print(amit.sort_num_list([1,7,3,8,435,8,43,87,34,87,23]))
print(amit.sort_num_list([6,4,3,2,8,4,2,7,4,35,6,66,6,4]))
print(amit.sort_num_list([1,7,3,1000,435,1000,-1000,87,34,87,23]))
print(amit.sort_num_list([18.33, -2.5, 0.0, 12.57, -30.0, 0.0]))
print()

print("DONE")



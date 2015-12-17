#Question 3
in_file = open("our_input.txt", 'r')
out_file = open("output.txt", 'w')
#Add the rest of your code here.
#Assume the file in_file exists in the same folder as the current file

for line in in_file:
    out_file.write(str(0 if line == '\n' else len(line.split(' '))))
    out_file.write('\n')

out_file.close()

#**************************************************************
#Question 5
k = 3
n = 100
#Add the rest of your code here.

i = 1
while i <= n:
    if i % k == 0:
        if str(k) in str(i):
            print("boom-boom!")
        else:
            print("boom!")
    else:
        if str(k) in str(i):
            print("boom!")
        else:
            print(str(i))
    i += 1





#**************************************************************
#Question 6
num = int(input("Please enter a positive integer: "))
#Add the rest of your code here.
#It should handle any positive integer num
#at the end, the variables named 'length', 'start' and 'seq'
#should hold the answers and be printed below

max_count = 0
max_start = -1
count = 0
start = -1
s = str(num)
for i in range(len(s)):
    c = int(s[i])
    if c % 2 == 1:
        if count == 0:
            start = i
            count = 1
        else:
            count += 1
        if count > max_count:
            max_count = count
            max_start = start
    else:
        count = 0
        start = -1

length = max_count
start = max_start
seq = s[max_start:max_start+max_count]

print("The maximal length is", length)
print("Sequence starts at", start)
print("Sequence is", seq)
import sys

add = 0.0

# get length of command line args
n = len(sys.argv)
print(f'\n{n} args')
# sys.argv is a list of args;
# skip [0] as that is the filename;
# we just want the numbers, onward
for i in range(1, n):
    add += float(sys.argv[i])

print(f'\nthe sum is: {add}')

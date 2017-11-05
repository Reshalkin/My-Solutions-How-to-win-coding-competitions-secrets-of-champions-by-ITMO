import sys

input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')


n = int(input_file.readline())
T = [int(x)/60.0 for x in input_file.readline().split()]

T = sorted(T)


total_time = sum(T)

i = 0
while total_time > 300.0:
    i += 1
    total_time -= T[len(T)-i]

output_file.write(str(len(T) - i))

input_file.close()
output_file.close()
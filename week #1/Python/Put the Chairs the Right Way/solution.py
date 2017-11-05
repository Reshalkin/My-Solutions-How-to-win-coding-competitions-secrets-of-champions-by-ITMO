import sys

input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

A = [int(x) for x in input_file.readline().split()]

print(sum(A)/6.0)
output_file.write(str(sum(A)/6.0))
input_file.close()
output_file.close()





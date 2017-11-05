import sys

input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

A = [int(x) for x in input_file.readline().split()]
B = [int(x) for x in input_file.readline().split()]
C = [int(x) for x in input_file.readline().split()]

efficiency = []

for i in range(3):
    for j in range(3):
        for k in range(3):
            if j!=i:
                if k!=j and k!=i:
                    efficiency.append((A[i]**2 + B[j]**2 + C[k]**2)**0.5)

output_file.write(str(max(efficiency)))
input_file.close()
output_file.close()



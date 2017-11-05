import sys

input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

def number_of_divisors(K):
    limit = K
    nod = 0

    if K == 1:
        return 1

    for i in range(1, limit):
	for i in range(1, limit):
        if K % i == 0:
            limit = K / i
            if limit != i:
                nod += 1
            nod += 1

    return nod
                

K = int(input_file.readline())

max_div = 0
ind = 0
for i in range(1, K+1):
    nod = number_of_divisors(i)
    if nod > max_div:
        max_div = nod
        ind = i

output_file.write(str(K - ind + 1))

input_file.close()
output_file.close()






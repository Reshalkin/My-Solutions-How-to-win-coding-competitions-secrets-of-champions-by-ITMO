import sys

input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

t0, t1, t2, n = [int(x) for x in input_file.read().split()]

if n > 2:
	for i in range(3, n+1):
		t = t2 + t1 - t0
		t0 = t1
		t1 = t2
		t2 = t
elif n == 0:
		t = t0
elif n == 1:
		t = t1
elif n == 2:
		t = t2
		
output_file.write(str(t))
input_file.close()
output_file.close()





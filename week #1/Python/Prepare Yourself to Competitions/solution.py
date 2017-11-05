import sys

input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

n  = int(input_file.readline())
T = [int(x) for x in input_file.readline().split()]
P = [int(x) for x in input_file.readline().split()]

flag_t = False
flag_p = False
ability = 0
res = []

for i in range(n):
    if flag_t == True and flag_p == True:
        ability += max(T[i], P[i])
        res.append(abs(T[i] - P[i]))
    elif flag_t == False and max(T[i], P[i]) == T[i]:
        flag_t = True
        ability += max(T[i], P[i])
        res.append(abs(T[i] - P[i]))
    elif flag_p == False and max(T[i], P[i]) == P[i]:
        flag_p = True
        ability += max(T[i], P[i])
        res.append(abs(T[i] - P[i]))
    elif flag_t == True and max(T[i], P[i]) == T[i]:
        ability += max(T[i], P[i])
        res.append(abs(T[i] - P[i]))
    elif flag_p == True and max(T[i], P[i]) == P[i]:
        ability += max(T[i], P[i])
        res.append(abs(T[i] - P[i]))
        
if flag_t == False or flag_p == False:
    ability -= min(res)
        
print(T)
print(P)
print(res)
print(ability)
print(flag_p, flag_t)
output_file.write(str(ability))
input_file.close()
output_file.close()
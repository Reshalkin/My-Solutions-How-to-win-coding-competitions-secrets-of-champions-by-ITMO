import sys

input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

keyboard = {}
text = ['','','']
languages = []

w, h = [int(x) for x in input_file.readline().split()]

for i in range(h):
    kb_line = list(input_file.readline().rstrip())
    for j in range(w):
        keyboard[kb_line[j]] = (h-i, j+1)


for i in range(0,3):
    languages.append(input_file.readline().rstrip())
    str_line = input_file.readline().rstrip()
    if str_line == '%TEMPLATE-START%':
        while str_line != '%TEMPLATE-END%':
            if str_line != '%TEMPLATE-START%':
                text[i] += str_line.replace(" ", "")
            str_line = input_file.readline().rstrip()


time = []

for i in range(3):
    t = 0 
    if len(text[i]) > 1:
        for j in range(1, len(text[i])):
            if text[i][j] not in [' ', '  ', '   ']:
                t += max(abs(keyboard[text[i][j]][0] - keyboard[text[i][j-1]][0]), abs(keyboard[text[i][j]][1] - keyboard[text[i][j-1]][1]))
    time.append(t)

min_time = time[0]
min_index = 0
for i in range(1,3):
    if time[i]<min_time:
        min_time = time[i]
        min_index = i

output_file.write(str(languages[min_index])+'\n')
output_file.write(str(min_time))
input_file.close()
output_file.close()




# coding: utf-8

# In[4]:

import sys

in_f = open('input.txt', 'r')
out_f = open('output.txt', 'w')

a,b = in_f.read().split()

out_f.write(str(int(a) + int(b)*int(b)))
in_f.close()
out_f.close()


# In[ ]:




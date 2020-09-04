#!/usr/bin/env python
# coding: utf-8

# In[28]:


a,b=input().split(' ')
i=int(input())
from itertools import product as pr
comb=pr(list(range(int(a),int(b)+1)),repeat=i)
count=0
for j in comb:
    if sum(j)%2==0:
        count=count+1
print(count%1000000007)


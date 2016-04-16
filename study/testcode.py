# -*- coding: utf-8 -*-

result= [7,8]

for kk in zip([0] + result, result + [0]):
    print kk

print kk

g= [sum(i) for i in zip([0] + result, result + [0])]

print g


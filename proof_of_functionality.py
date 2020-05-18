#!/usr/bin/env python
from collections import OrderedDict
import time
times = 0
# for times in range(10):
items = []
i = 0
size = 100
half = size/2
for i in range(size):
    if i < half:
        items.insert( i, str(i) + "@mail.com")     
    else:
        items.insert(i, str(int(i/2)) + "@mail.com")   

print("List with duplicates" + str(items))
# start = time.time()
print(" List without duplicated" + str(list(OrderedDict.fromkeys(items))))
# end = time.time()
# time_taken = end - start
# print("time:"+ str(time_taken))
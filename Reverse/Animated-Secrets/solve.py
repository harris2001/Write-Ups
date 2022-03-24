# 49157593271891 = 13 · 37 · 53 · 439 · 4392433
import math

divisors = []
for i in range(1,math.floor(math.sqrt(49157593271891))):
    if 49157593271891 %i==0:
        divisors.append(i)
        divisors.append(49157593271891//i)

for i in divisors:
    print(i,len(str(i)))
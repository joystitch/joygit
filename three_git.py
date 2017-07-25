#! /usr/bin/python3

for i in range(1,5):
    for j in range(1,5):
        for m in range(1,5):
            if (i != j and i != m and j !=m ):
                s = 100*i +10*j + m
                print(s)

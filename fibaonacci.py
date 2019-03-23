#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print(sys.argv[0], "<natural number>")
    sys.exit(1)

first = 0
second = 1
thesum = first + second
count = int(sys.argv[1])

if count < 0:
    print(sys.argv[0], "<natural number>")
    sys.exit(1)

thecount = 2 

if count == 0:
    print("No numbers", end="")

if count == 1:
    print("0", end="")

if count > 1:
    print("0 1 ", end="")

while thecount < count:
    print(thesum, end="")

    if thecount < count - 1:
        print(" ", end="")

    first = second
    second = thesum
    thesum = first + second
    thecount = thecount + 1

print("")


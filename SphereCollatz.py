#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

import sys


cacheSize = 10000
cache = [0] * cacheSize

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert i > 0
    assert i < 1000000
    assert j > 0
    assert j < 1000000
    if i > j :
       i,j = j,i
    e = j // 2 + 1
    if i < e :
       i = e
    m = 0
    for n in range(i,j+1) :
        m = max(m,cycle_length(n))
    assert m > 0
    return m


def cycle_length (n) :
    assert n > 0
    global cache
    n0 = n
    
    if n < cacheSize and cache[n] != 0 :
        return cache[n]
        
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
            c += 1
        else :
            n = n + (n >> 1) + 1
            c += 2
    assert c > 0
    if n0 < cacheSize :
        cache[n0] = c
    return c


# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)



# ----
# main
# ----

if __name__ == "__main__" :
    collatz_solve(sys.stdin, sys.stdout)

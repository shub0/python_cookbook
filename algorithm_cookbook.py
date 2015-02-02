#! /usr/bin/python


def unique_no_order(sequence):
    # elements in sequence are hashable O(N)
    try:
        return list(set(sequence))
    except TypeError:
        pass
    # elements in sequence are with full comparision O(NlogN)
    t = list(sequence)
    try:
        t.sort()
    except TypeError:
        del t
    else:
        return [x for x, i in enumerate(t) if not i or x != t[i-1]]
    # brute force search o(N^2)
    u = []
    for x in sequence:
        if x not in u:
            u.append(x)
    return u

# Support user-defined hash functions
def unique_with_order(sequence, hash_function=None):
    if hash_function is None:
        def hash_function(x): return x
    element_set = set()
    unique_sequence = []
    for element in sequence:
        marker = hash_function(element)
        if marker not in element_set:
            element_set.add(marker)
            unique_sequence.append(element)
    return unique_sequence

import random
def sample_with_replacement(population, _choose=random.choice):
    while True: yield _choose(population)

def sample(n, r):
    rand = random.random
    pop = n
    for sample in xrange(r, 0, -1):
        cum_prob = 1,0
        x = rand()
        while x < cum_prob:
            cum_prob -= cum_prob * sample / pop
            pop -= 1
        yield n-pop-1

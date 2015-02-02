 #! usr/bin/python
import sys
import random

animals = []
number_of_felines = 0

def dict_from_list(keys_and_values):
    return dict(zip(keys_and_values[::2], keys_and_values[1::2]))

def pair_wise(iterable):
    itnext = iter(iterable).next
    while True:
        yield itnext(), itnext()

def dict_from_sequence(seq):
    return dict(pair_wise(seq))

def sub_dict(a_dict, keys, default=None):
    return dict([ (key, a_dict.get(key, default)) for key in keys ])

def sub_dict_remove(a_dict, keys, default=None):
    return dict([ (key, a_dict.pop(key, default)) for key in keys ])

def invert_dict(a_dict):
    return dict([ (value, key) for key, value in a_dict.iteritems() ])

def ass_multiple_values_with_key(key, value):
    a_dict = {}
    a_dict.setdefault(key, []).append(value)
#    b_dict = {}
#    b_dict.setdefault(key, {}).[value] = 1
    c_dict = {}
    c_dict.setdefault(key, set()).add(value)

def _deal_with_a_cat():
    global number_of_felines
    print 'meow'
    animals.append('feline') 
    number_of_felines += 1
def _deal_with_a_dog():
    print 'bark'
    animals.append('canine')
def _deal_with_a_bear():
    print 'watch out for the "HUG"!'
    animals.append('ursine')
def dispatch_functions():
    token_dict = {
        'cat':    _deal_with_a_cat,
        'dog':    _deal_with_a_dog,
        'bear':   _deal_with_a_bear
        }
    words = ['cat', 'bear', 'cat', 'dog']
    for word in words:
        token_dict[word]()
    nf = number_of_felines
    print 'We met %d feline(s).' % nf
    print 'The animals we met were: ', ','.join(animals)

def union(a_dict, b_dict):
    return dict(a_dict, **b_dict)

def intersect(a_dict, b_dict):
    return dict.fromkeys([ x for x in a_dict if x in b_dict ])

def printf(format, *args):
    sys.stdout.write(format % args)

def random_pick(a_list, probabilities):
    x = random.uniform(0, 1)
    cumlative_probability = 0.0
    for item, item_probability in zip(a_list, probabilities):
        cumlative_probability += item_probability
        if x < cumlative_probability: break
    return item

if __name__ == '__main__':
    dispatch_functions()

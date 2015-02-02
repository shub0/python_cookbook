#! /usr/bin/python
import operator

def sort_dict_values(a_dict):
    keys = a_dict.keys()
    keys.sort()
    return [a_dict[key] for key in keys]

def case_insensitive_sort(string_list):
    auxiliary_list = [(x.lower(), x) for x in string_list]
    auxiliary_list.sort()
    return [ x[i] for x in auxiliary_list ]

def case_insensitive_sort_fase(string_list):
    return sorted(string_list, key=str.lower)

def _sort_by_attr_1(seq, attr):
    intermed = [ (getattr(x, attr), i, x) for i, x in enumerate(seq) ]
    intermed.sort()
    return [ x[-1] for x in intermed ]

def sort_by_attr_inplace_1(a_list, attr):
    a_list[:] = _sort_by_attr_1(a_list, attr)

def _sort_by_attr_2(seq, attr):
    return sorted(seq, key=operator.attrgetter(attr))

def _sort_by_attr_inplace_2(a_list, attr):
    a_list.sort(key=operator.attrgetter(attr))


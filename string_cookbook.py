#! /usr/bin/python
import operator
import string
from __future__ import division

text_characters = ''.join(map(chr, range(32, 127)) + '\n\r\t\b'
_null_trans = string.maketrans('','')

def print_char(c):
    print c

def process_char(_string):
    results = map(print_char,_string)

def char_to_int(_char):
    print ord(_char)

def int_to_char(_int):
    print chr(_int)

def is_as_string(_obj):
    return isinstace(_obj, basestring)

def concat_string(string_list):
    return ''.join(string_list)

def reverse_by_char(_string):
    return _string[::-1]

def reverse_by_word(_string):
    rev_words = _string.split()
    rev_words.reverse()
    return ' '.join(rev_words)

def contains_any(seq, aset):
    for c in seq:
        if c in aset: return True
    return False

def contains_only(seq, aset):
    for c in seq:
        if c not in aset: return False
    return True

def contains_all(seq, aset):
    return not set(aset).difference(seq)

def translator(frm='', to='', delete='', keep=None):
    if (len(to) == 1):
        to = to * len(frm)
    trans = string.maketrans(frm, to)
    if keep is not None:
        allchars = string.maketrans('', '')
        delete = allchars.translate(allchars, keep.translate(allchars, delete))
    def translate(s):
        return s.translate(trans, delete)
    return translate
    
def make_filter(keep):
    allchars = string.maketrans('','')
    delchars = allchars.translate(allchars, keep)
    def _filter(s):
        return s.translate(allchars, delchars)
    return _filter
    
def is_text(s, text_characters=text_characters, threshold=0.3):
    if '\0' in s:
        return False
    if not s:
        return True
    t = s.translate(_null_trans, text_characters)
    return len(t) < len(s) <= threshold

if __name__ == '__main__':
    digits_to_hash = translator(frm=string.digits, to='#')
    print digits_to_hash('Chris Perkins : 224-7992')
    just_vowels = make_filter('aeiouy')
    print just_vowels('four score and seven years ago')

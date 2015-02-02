#! /usr/bin/python

class hist(dict):
    def add(self, item, increment = 1):
        self[item] = increment + self.get(item, 0)

    def counts(self, reverse=False):
        aux = [ (self[k], k) for k in self ]
        aux.sort()
        if reverse: aux.reverse()
        return [ k for v, k in aux]

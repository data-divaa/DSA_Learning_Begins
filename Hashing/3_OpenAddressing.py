'''
Date - 01 -july - 2025
Author - Data-Divaa
Desc - use open addressing for the search insert and removal
'''

class OpenAddress:
    def __init__(self,c):
        self.cap = c
        self.table = [-1] * c
        self.size = 0


    def Hash(self,x):
        return x % self.cap

    def search (self,x):
        t = self.table
        h = self.Hash(x)
        i = h
        while t[i] != -1 :
            if t[i] == x:
                return True
            i = (i +1) % self.cap
            if i == h :
                return False
        return False


    def insert(self,x):
        if self.cap == self.size:
            return False

        if self.search(x) == True:
            return False

        t = self.table
        h = self.Hash(x)
        i = h
        while t[i] not in (-1,-2):
            i = (i + 1) % self.cap
        t[i] = x
        self.size = self.size + 1
        return True

    def remove(self,x):
        t = self.table
        h = self.Hash(x)
        i = h
        while t[i] != -1:
            if t[i] == x:
                t[i] = -2
                return True
            i = (i +1) % self.cap
            if i == h :
                return False
        return False


h = OpenAddress(7)
h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)
print(h.search(56))
h.remove(56)
print(h.search(56))
h.remove(56)

class print:
    def prt(self,a):
        print(self)
        print(self.__class__)

p=print()
p.prt(1)

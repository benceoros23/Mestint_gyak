class Hanoi:
    def __init__(self,ke,c):
        self.kezdo=ke
        self.cel=c

    def celteszt (self,a): #a=(a1,a2,..., an)
        return a == self.cel

    def rakovetkezo (self, a):
        gyerekek=[]
        n = len(a) #korongok száma
        for melyiket in range(0,n):
            for hova in ['P', 'Q', 'R']: #átrak melyiket hova
               tmp=True
            if a[melyiket]!=hova:
                    for i in range(0,melyiket):
                        if a[i]!=a[melyiket] and a[i]!=hova:
                            tmp=True
                    else:
                            tmp=False
                            break
            else:
                tmp=False

            if tmp == True:
                uj_allapot=list(a)
                uj_allapot[melyiket]=hova
                gyerekek.append(tuple(uj_allapot))

        return gyerekek


if __name__ == '__main__':
   feladat= Hanoi(('P','P','P','P','P'),('R','R','R','R','R'))

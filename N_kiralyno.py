class Kiralyno:
    def __init__(self,ke,c):
        self.kezdo=ke;
        self.cel=c;
        self.N=len(ke)-1
    def celteszt(self,a): #a = (a1,a2,...,an,s)
        return a[self.N] == self.cel

    def rakovetkezo(self,a):
        gyerekek=[]
        s=a[self.N] # ebbe a sorba probálok rakni

        for i in range(1,self.N+1):
            elofeltetel=True # lerak (s, i) alkalmazható?
            for m in range(1,s): #bármely m<s esetén
                if a[m-1]!=i and abs(m-s) != abs (a[m-1]-i):
                    #elofeltetel=True
                    pass
                else:
                    elofeltetel=False
                    break

            if elofeltetel:
                uj_allapot=list(a)
                uj_allapot[s-1]=i
                uj_allapot[self.N]=s+1
                gyerekek.append(tuple(uj_allapot))

        return gyerekek





if __name__ == '__main__':
   feladat= Kiralyno((0,0,0,0,0,0,0,0,1),9)
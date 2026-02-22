# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def szokoevek(ev1, ev2):
    eredmeny = []
    for ev in range(ev1, ev2+1):
        if (ev % 4 == 0 and ev % 100 != 0) or (ev % 400 == 0):
            eredmeny.append(ev)
    return eredmeny

def is_palindrom(szam):
    eredeti= szam
    forditott = 0
    while szam !=0:
        szj = szam % 10
        szam = szam // 10 #egesz osztas hanyados
        forditott = forditott*10+szj
    return eredeti == forditott

#egy fv kap listat viassz eredmeny is lista ami paros szamok negyzetet adja vissza

def paros(szamok):
    return [x*x for x in szamok if x%2 == 0]

def min_max(szamok):
    return (min(szamok), max(szamok))

class Hallgato:
    def __init__(self, n, nk):
        self.nev = n
        self.nkod = nk
        self.jegyek = []
    def jegyek_hozzaad(self, jegy):
        if 1<= jegy <=5:
            self.jegyek.append(jegy)
    def atlag(self):
        if not self.jegyek:
            return 0.0

        return sum(self.jegyek)/len(self.jegyek)
    def __str__(self):
        return f"{self.nev} - atlag = {self.atlag()}"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(szokoevek(1890, 1025))
    print(is_palindrom(12321))
    eredmeny = min_max([2,-9,4,11])
    print(eredmeny)
    mikulas = ("piros alma", "dio" , 10, [2,35,-9])
    tmp = list(mikulas)
    tmp[3] = "mogyoro"
    mikulas2 = tuple(tmp)
    print(mikulas2)

    h = Hallgato("Deb ella" ,"AS012")
    h.jegyek_hozzaad(3)
    h.jegyek_hozzaad(4)
    print(h)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

class KancsoFeladat:
    def __init__(self, ke, c):
        self.kezdo = ke
        self.cel = c
        self.Max1=3
        self.Max2=5
        self.Max3=8

    def celteszt(self, a): #a=(a1,a2,a3) allapot
        return a[0] == self.cel or a[1] == self.cel or a[2] == self.cel

    def rakovetkezo(self, a): #a=(a1,a2,a3) allapot
        gyerekek = []
        a1,a2,a3 = a
        # tolt 1,2 operator alkalmazasi elofeltetele
        if a1 != 0 and a2 != self.Max2:
            T = min(a1, self.Max2 - a2)
            gyerekek.append(("tolt 1->2", (a1 - T, a2 + T, a3)))

        # tolt 1,3 operator alkalmazasi elofeltetele
        if a1 != 0 and a3 != self.Max3:
            T = min(a1, self.Max3 - a3)
            gyerekek.append(("tolt 1->3", (a1 - T, a2, a3 + T)))

        # tolt 2,1 operator alkalmazasi elofeltetele
        if a2 != 0 and a1 != self.Max1:
            T = min(a2, self.Max1 - a1)
            gyerekek.append(("tolt 2->1", (a1 + T, a2 - T, a3)))

        # tolt 2,3 operator alkalmazasi elofeltetele
        if a2 != 0 and a3 != self.Max3:
            T = min(a2, self.Max3 - a3)
            gyerekek.append(("tolt 2->3", (a1, a2 - T, a3 + T)))

        # tolt 3,1 operator alkalmazasi elofeltetele
        if a3 != 0 and a1 != self.Max1:
            T = min(a3, self.Max1 - a1)
            gyerekek.append(("tolt 3->1", (a1 + T, a2, a3 - T)))

        # tolt 3,2 operator alkalmazasi elofeltetele
        if a3 != 0 and a2 != self.Max2:
            T = min(a3, self.Max2 - a2)
            gyerekek.append(("tolt 3->2", (a1, a2 + T, a3 - T)))

        return gyerekek

if __name__ == '__main__':
    feladat = KancsoFeladat((0,0,8), 4)

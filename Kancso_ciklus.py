class KancsoFeladat:
    def __init__(self, ke, c):
        self.kezdo = ke
        self.cel = c
        self.Max1 = 3
        self.Max2 = 5
        self.Max3 = 8

    def celteszt(self, a):  # a=(a1,a2,a3) allapot
        return a[0] == self.cel or a[1] == self.cel or a[2] == self.cel

    def rakovetkezo(self, a):  # a=(a1,a2,a3) allapot
        gyerekek = []
        # A maximumokat egy listába tesszük a ciklushoz
        maximumok = [self.Max1, self.Max2, self.Max3]

        for i in range(3):  # Forrás kancsó indexe
            for j in range(3):  # Cél kancsó indexe
                if i != j:
                    # tolt i+1,j+1 operator alkalmazasi elofeltetele
                    if a[i] != 0 and a[j] != maximumok[j]:
                        T = min(a[i], maximumok[j] - a[j])

                        # Új állapot kiszámítása
                        uj = list(a)
                        uj[i] -= T
                        uj[j] += T

                        # Az i+1 és j+1 biztosítja a pl."tolt 1->2" jellegű megnevezést
                        gyerekek.append((f"tolt {i + 1}->{j + 1}", tuple(uj)))

        return gyerekek


if __name__ == '__main__':
    feladat = KancsoFeladat((0, 0, 8), 4)
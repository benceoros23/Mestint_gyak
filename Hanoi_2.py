class Hanoi:
    def __init__(self, kezdo, cel):
        self.kezdo = kezdo
        self.cel = cel

    def celteszt(self, allapot):
        return allapot == self.cel

    def rakovetkezo(self, allapot):
        gyerekek = []

        # Tudjuk, hogy 3 korongunk van
        korongok = [1, 2, 3]

        for melyiket in korongok:
            for hova in range(3):

                # 1. Megkeressük, hol van jelenleg a korong
                hol_van = -1
                for i in range(3):
                    if allapot[i] != 0 and melyiket in allapot[i]:
                        hol_van = i
                        break

                # Ha már a célrúdon van, ugrunk a következőre
                if hol_van == hova:
                    continue

                # 2. Előfeltételek vizsgálata
                # Levehető? (Ő a legkisebb a jelenlegi rúdján?)
                if melyiket != min(allapot[hol_van]):
                    continue

                # Letehető? (A célrúd üres, vagy nagyobb korong van rajta?)
                if allapot[hova] == 0 or melyiket < min(allapot[hova]):

                    # 3. Lépés végrehajtása (állapot másolása és módosítása)
                    uj_allapot = list(allapot)

                    # Levétel
                    uj_allapot[hol_van] = set(allapot[hol_van]) - {melyiket}
                    if not uj_allapot[hol_van]:  # Ha kiürült, legyen újra 0
                        uj_allapot[hol_van] = 0

                    # Feltevés
                    if uj_allapot[hova] == 0:
                        uj_allapot[hova] = {melyiket}
                    else:
                        uj_allapot[hova] = set(allapot[hova]) | {melyiket}

                    gyerekek.append(tuple(uj_allapot))

        return gyerekek


if __name__ == '__main__':
    feladat = Hanoi(({1, 2, 3}, 0, 0), (0, 0, {1, 2, 3}))

    print("Kezdőállapot:")
    print(feladat.kezdo)

    print("\nVégállapot (célállapot):")
    print(feladat.cel)
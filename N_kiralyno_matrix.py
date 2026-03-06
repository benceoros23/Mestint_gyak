class KiralynoMatrix:
    def __init__(self, N):
        self.N = N
        # Kezdőállapot (k): NxN nullás mátrix, és a 0. sorból indulunk (s=0)
        self.kezdo = ([[0] * N for _ in range(N)], 0)

    def celteszt(self, allapot):
        matrix, s = allapot
        # Célállapot (C): Ha az aktuális sor (s) eléri az N-t, kész vagyunk.
        return s == self.N

    def rakovetkezo(self, allapot):
        matrix, s = allapot
        gyerekek = []

        # Biztonsági ellenőrzés: ha már célban vagyunk, nincs következő lépés
        if s == self.N:
            return gyerekek

        # Operátorok (O): 'i' az oszlop indexe, ahova a királynőt próbáljuk tenni
        for i in range(self.N):
            utkozes = False

            # Előfeltétel vizsgálata: Végignézzük a felettünk lévő sorokat (m)
            for m in range(s):
                tavolsag = s - m  # Kiszámoljuk, milyen messze van a vizsgált sor felettünk

                # Ellenőrizzük az oszlopot és a két átlót egyetlen feltételben
                if matrix[m][i] == 1 or \
                        (i - tavolsag >= 0 and matrix[m][i - tavolsag] == 1) or \
                        (i + tavolsag < self.N and matrix[m][i + tavolsag] == 1):
                    utkozes = True
                    break

            # Alkalmazási függvény: Ha teljesül az előfeltétel (nincs ütközés)
            if not utkozes:
                # Lemásoljuk a mátrixot, hogy az eredeti ne változzon
                uj_matrix = [sor[:] for sor in matrix]
                # Letesszük a királynőt (1-es beírása)
                uj_matrix[s][i] = 1
                # Létrehozzuk az új állapotot a megnövelt sorindexszel (s+1)
                gyerekek.append((uj_matrix, s + 1))

        return gyerekek


if __name__ == '__main__':
    # Példa a 8 királynő problémára
    feladat = KiralynoMatrix(8)

    print("A feladat inicializálva!")
    print(f"Kezdőállapot sora: {feladat.kezdo[1]}")
    print(f"A 0. sorból {len(feladat.rakovetkezo(feladat.kezdo))} helyre léphetünk.")
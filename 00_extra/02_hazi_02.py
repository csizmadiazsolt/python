#!/usr/bin/python3
from random import randint
#egy veletlenszeru szamot hoz be

nev = input("Add meg a neved: ")
# a iba az volt h a nev-nek a baloldalon kell lennie
print("Üdvözöllek, " + nev)

print("\nKerüld el a csapdát!")

eletek = 5
arany = 0

while eletek > 0:
    print ("\nÚtelágazáshoz értél. \n Három út van előtted...")
    # --> \n Ezzel tudok sortörést betenni anélkül, h uj print sort raknék be
    print("De tudod , hogy az egyik csapdát rejt!")
    print("Merre indulsz?")

    csapda_ut = randint (1, 3)

    valasztott_ut = input("1, 2, vagy 3? ")
    valasztott_ut_szammal = int(valasztott_ut)
    #int --> szam tipusu valtozova lakit

    if valasztott_ut_szammal == csapda_ut:
        #azert van ==, mert azt vizsgalja h egyenlo-e, tehat egy relaciot vizsgal
        print("Csapda!")
        eletek = eletek - 1
        print("Csökkent az életeid száma eggyel, " + str(eletek) + " életed maradt.")
    else:
        kapott_arany = randint(1,3)
        arany = arany + kapott_arany
        print(str(kapott_arany) + " aranyat találtál!")
        print("Biztonságos út, mehetsz tovább...")

print("Összesen " + str(arany) + " aranyat találtál.")
print("Játsszunk legközelebb is!")
# itt nekem manualisan vissza kell huznom, mert csak a behuzast csinalja meg maga. a tagolashoz logikailag nekem kell tagolnom.
#mig phytonban a behuzas mukodik, mas programnyelvekben a kapcsos zarojel az elagazasok jelzoje{{}

#ha olyan szamot adok meg amire nem irtunk elif et akkor egyszeruen atugorja, de lefut
# if, elif, else mindig : zarodik
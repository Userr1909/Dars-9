# 4-masala. Bank hisob kalkulyatori.
# Depozit summasi, foiz stavkasi va yil sonini argument sifatida oladigan funksiya yozing va yakuniy summani qaytaring.
# Parametr: depozit=10000, foiz=24, yil=3
# Return: 17200
import os
os.system("cls")

def bank_kalkulyatori(depozit, foiz, yil):
    javob = depozit + (depozit * foiz* yil / 100)
    return int(javob)

natija = bank_kalkulyatori(10000, 24, 3)

print("natija:", natija)
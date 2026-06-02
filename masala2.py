# 2-masala. Lug'atda mahsulot nomi va narxlari bor ({"olma": [1200, 1300, 1100], ...}). 
# Har bir mahsulotning o'rtacha narxini chiqaruvchi funksiya yozing.
# Input: {
#     "olma": [13000, 14000, 15000],
#     "anor": [19000, 22000, 24000, 15000],
#     "gilos": [6000, 9000, 5000, 4000],
#     "banan": [30000, 28000]
# }
# Output: olma: 14000 
# 	anor: 20000 
# 	gilos: 6000 
# 	banan: 29000
import os 
os.system("cls")

def funk1(a):
    for i,j in a.items():
        javob = int(sum(j)/len(j))
        print(F"{i}: {javob}")

lugat = {
    "olma": [13000, 14000, 15000],
    "anor": [19000, 22000, 24000, 15000],
    "gilos": [6000, 9000, 5000, 4000],
    "banan": [30000, 28000]
}

funk1(lugat)
# tayyor
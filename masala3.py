# 3-masala.List ichida (kitob_nomi, janr) ko'rinishidagi tuple-lar bor. Har bir janr bo'yicha kitoblarni guruhlang.
# Input: books = [
#     ("O'tkan kunlar", "Roman"),
#     ("Mehrobdan chayon", "Roman"),
#     ("Shum bola", "Povest"),
#     ("Alkimyogar", "Roman"),
#     ("Boy va kambag'al", "Hikoya"),
#     ("Urush va tinchlik", "Roman"),
#     ("Kecha va kunduz", "Roman"),
#     ("Yulduzli tunlar", "Povest"),
#     ("Qorako'z Majnun", "Hikoya"),
#     ("Qalb ko'zi", "Hikoya")
# ]
# Output: {
#     "Roman": [
#         "O'tkan kunlar",
#         "Mehrobdan chayon",
#         "Alkimyogar",
#         "Urush va tinchlik",
#         "Kecha va kunduz"
#     ],
#     "Povest": [
#         "Shum bola",
#         "Yulduzli tunlar"
#     ],
#     "Hikoya": [
#         "Boy va kambag'al",
#         "Qorako'z Majnun",
#         "Qalb ko'zi"
#     ]
# }
import os
os.system("cls")

books = [
    ("O'tkan kunlar", "Roman"),
    ("Mehrobdan chayon", "Roman"),
    ("Shum bola", "Povest"),
    ("Alkimyogar", "Roman"),
    ("Boy va kambag'al", "Hikoya"),
    ("Urush va tinchlik", "Roman"),
    ("Kecha va kunduz", "Roman"),
    ("Yulduzli tunlar", "Povest"),
    ("Qorako'z Majnun", "Hikoya"),
    ("Qalb ko'zi", "Hikoya")
]
natija = {
    "Roman": [],
    "Povest": [],
    "Hikoya": []
}
for i,j in books:
    natija[j].append(i)

print(natija)
# tayyor
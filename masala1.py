# 1-masala. List ichida turli ism-familiyalar bor. Shu listdan erkaklarni alohida, ayollarni alohida listlarga ajratib bering.
# (Farqlashda familyalardan foydalaning, erkaklarda "ov","ev", ayollarda "va" bilan tugaudi)
# Input: 
# users = [
#     'Abdulla Abdullaev', 
#     'Samandar Asadov', 
#     'Shaxnoza Jurayeva', 
#     'Ikrom Karimov',
#     'Gulnora Xalilova',
#     'Ziyoda Yuldashova'
#     ]
# Output:
# men = [
#     'Abdulla Abdullaev',
#     'Samandar Asadov',
#     'Ikrom Karimov'
#     ]
# women = [
#     'Shaxnoza Jurayeva',
#     'Gulnora Xalilova',
#     'Ziyoda Yuldashova'
# ]

import os 
os.system("cls")

users = [
    'Abdulla Abdullaev', 
    'Samandar Asadov', 
    'Shaxnoza Jurayeva', 
    'Ikrom Karimov',
    'Gulnora Xalilova',
    'Ziyoda Yuldashova'
    ]
men = []
women = []
for i in users:
    if i.endswith("ov") or i.endswith("ev"):
        men.append(i)
    elif i.endswith("va"):
        women.append(i)
print(men)
print(women)
# tayyor
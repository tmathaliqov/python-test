# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 20:35:50 2023

@author: User
"""

menu = {'osh': 20000,
        'shorva': 18000,
        'mastava': 15000,
        'lagmon': 17000,
        'monti': 22000}
jami = 0
buyurtma =[]
while True: 
    zakaz = input("Nima zakaz qilmoqchisiz - ")
    buyurtma.append(zakaz)
    
    if zakaz == 'stop' :
        print("Sizni qilgan zakazlaringiz quyidagilar!")
        for zakaz in buyurtma:
             if zakaz == 'stop':
                break
             else:
                 print(f"{zakaz.title()} \n")  
        break
    else:
        print('Yanachi?')
        continue
for buyurtmasi in buyurtma:
    if buyurtmasi in menu:
        print(f"{buyurtmasi.title()} {menu[buyurtmasi]} so'm")
        jami += menu[buyurtmasi]
    else: 
        if buyurtmasi == 'stop':
            break
        else :
            print(f"Kechirasiz, bizda {buyurtmasi} yo'q.")
print(f" Jami summa = {jami} so'm bo'ldi !")
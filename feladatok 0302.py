from random import randint

szamok = []

for _ in range(20):
    szamok.append(randint(50, 150))

szamok.sort()

for n in szamok: print(n, end=' ')
print(end='\n')

print(f'számok összege: {sum(szamok)}')
print(f'számok átlaga: {sum(szamok) / len(szamok)}')

# 'megszámlálás tételének alkalmazása'
c = 0
for n in szamok:
    if n % 10 == 0:
        c += 1
print(f'nullára végződő számok száma: {c} db')
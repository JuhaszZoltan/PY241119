nevek:list[str] = ['Erika', 'Béla', 'Alma', 'Dénes', 'Cecil']

for nev in nevek: print(nev, end=' ')
print(end='\n')

magassagok:list[int] = []
for i in range(len(nevek)):
    magassagok.append(int(input(f'{nevek[i]} magassága (cm): ')))
# -----------
avg = sum(magassagok) / len(magassagok)
print(f'átlagmagasság: {avg:.2f} cm')

for i in range(len(nevek) - 1):
    for j in range(i+1, len(nevek)):
        if nevek[i] > nevek[j]:
            s1 = nevek[i]
            nevek[i] = nevek[j]
            nevek[j] = s1
            s2 = magassagok[i]
            magassagok[i] = magassagok[j]
            magassagok[j] = s2

print('--- névsorrendbe rendezés után ----')

for i in range(len(nevek)):
    print(f'{nevek[i]} {magassagok[i]} cm')

print('--- magasság szerint növekvőbe rendezve ----')

for i in range(len(magassagok) - 1):
    for j in range(i+1, len(magassagok)):
        if magassagok[i] > magassagok[j]:
            s1 = nevek[i]
            nevek[i] = nevek[j]
            nevek[j] = s1
            s2 = magassagok[i]
            magassagok[i] = magassagok[j]
            magassagok[j] = s2

for i in range(len(nevek)):
    print(f'{nevek[i]} {magassagok[i]} cm')

maxindex = 0
for i in range(len(magassagok)):
    if magassagok[i] > magassagok[maxindex]:
        maxindex = i

print(f'legmagasabb: {nevek[maxindex]} ({magassagok[maxindex]} cm)')


import random

# 'iteratív vezérlő' (vagy, "ciklus", "loop")

# 'homogén kollekció' -> azonos típusú értékeket tartalmazó összetett adatszerkezet

# szamok = [11, 26, 31, 7, 42, 101]

#            0        1        2         3
# szavak = ['kutya', 'cica', 'traktor', 'alma']
# szavak[2] = 'virágcserép'
# szavak.append('gitár')
# print(szavak)
# print(len(szavak))
# szo = 'cica'
# if szo in szavak: szavak.remove(szo)
# print(szavak)
# ures_lista = []

#            0        1        2         3
szavak = ['kutya', 'cica', 'traktor', 'alma']

# for: "bejáró" ciklus

# for szo in szavak:
#     print(f'a(z) {szo} benne van a listában')

# for i in range(len(szavak)):
#     print(f'a lista [{i}] indezű eleme: {szavak[i]}')
#     print(f'2^i = {2 ** i}')

# for _ in range(20):
#     print('ez a sor 20x lesz kiirva')

# "elöltesztelős ciklus", while loop

# x = 0
# while 2**x < 100000000:
#     print(f'2^{x} = {2 ** x}')
#     x += 1

password:str = 'Titkos123'
while input('írd be a jelszót: ') != password:
    print('neeeeeem :PPPPP')
print('ügyi vagy!')

# while <condition> -> true || false:
#     <ismetlodo sorok>
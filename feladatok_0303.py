nevek = []

for _ in range(5):
    nev = input(f'írd be a {len(nevek) + 1}. nevet: ')
    if nev == '': break
    nevek.append(nev)

nevek.sort()

print(nevek)